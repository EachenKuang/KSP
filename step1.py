# the first step: raw data => words
# 对于每篇文章，将中文摘要与英文摘要分来（提取“摘要”与“摘要（翻译）”列中的字段）
# 分别处理中文与英文
import jieba
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def pre_process_en(corpora, low_freq_filter=True):
    """
    # 英文
    # 1、分词
    # 2、去掉停用词
    # 3、去掉标点符号
    # 4、处理为词干
    # 5、去除低频词
    a proprocess on courrses in English version
    :param corpora:
    :type [str,str,...]
    :param low_freq_filter: whether to filter low-frequence word
    :return: text
    :type [[],[],...]
    """
    # 分词
    texts_tokenized = [word_tokenize(document) for document in corpora]

    # 去除停用词
    texts_filtered_stopwords = [[word for word in document
                                 if word not in stopwords.words('english')]
                                for document in texts_tokenized]

    # 去除标点
    english_punctuations = \
        [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if word not in english_punctuations]
                      for document in texts_filtered_stopwords]

    # 处理为词干
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in document] for document in texts_filtered]

    # 去除过低频词
    if low_freq_filter:
        all_stems = sum(texts_stemmed, [])
        stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
        texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
    else:
        texts = texts_stemmed
    return texts


def pre_process_cn(corpora, low_freq_filter=True):
    """
    # 中文
    # 1、分词
    # 2、去掉停用词
    # 3、处理为词干
    # 4、去除低频词
    a proprocess on courrses in Chinese version
    :param corpora:
    :type [str,str,...]
    :param low_freq_filter: whether to filter low-frequence word
    :return: text
    :type [[],[],...]
    """
    # 分词
    texts_tokenized = [jieba.cut(document) for document in corpora]

    # 去除停用词(包含标点)
    stopwords_cn = []
    with open('stopwords_cn.txt', 'r') as reader:
        for line in reader.readlines():
            stopwords_cn.append(line.strip())

    texts_filtered_stopwords = [[word for word in document
                                 if word not in stopwords_cn]
                                for document in texts_tokenized]

    # 处理为词干
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in document] for document in texts_filtered_stopwords]

    # 去除过低频词
    if low_freq_filter:
        all_stems = sum(texts_stemmed, [])
        stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
        texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
    else:
        texts = texts_stemmed
    return texts


