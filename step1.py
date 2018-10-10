# the first step: raw data => words
# 对于每篇文章，将中文摘要与英文摘要分来（提取“摘要”与“摘要（翻译）”列中的字段）
# 分别处理中文与英文
import jieba
import logging
from gensim import models
from gensim import corpora
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
    with open(r'Data/RawData/stopwords_cn.txt', 'r', encoding="UTF8") as reader:
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


def save_dict(texts,filename=""):
    """
    保存字典以及数据集
    :param texts: 预处理后的数据
    :type [["","",..],[],..]
    :param filename: 个性化名称，用于区分
    :type str
    :return: void
    """
    dictionary = corpora.Dictionary(texts)
    dictionary.save(r"Data\Intermediate\dict_{0}.dict".format(filename))
    dictionary.save_as_text(r"Data\Intermediate\dict_text_{0}.dict".format(filename), False)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.BleiCorpus.serialize(r"Data\Intermediate\corpus_{0}.blei".format(filename), corpus)


if __name__ == '__main__':
    with open(r"Data\RawData\corpus_cn.txt", 'r', encoding="UTF8") as cn_Reader,\
            open(r"Data\RawData\corpus_en.txt", 'r', encoding="UTF8") as en_Reader:
        # 去除'\n'
        texts_en = [line.strip()for line in en_Reader.readlines()]
        texts_cn = [line.strip() for line in cn_Reader.readlines()]

        texts_pro_en = pre_process_en(texts_en)
        texts_pro_cn = pre_process_cn(texts_cn)

        save_dict(texts_pro_en,'en')
        save_dict(texts_pro_cn,'cn')


