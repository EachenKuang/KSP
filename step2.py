# 使用spacy作为训练提取出专用词汇
import spacy
from spacy import displacy
from spacy.pipeline import EntityRecognizer


def pre_process_en(corpora=""):
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
    # Text: The original word text.
    # Lemma: The base form of the word.
    # POS: The simple part-of-speech tag.
    # Tag: The detailed part-of-speech tag.
    # Dep: Syntactic dependency, i.e. the relation between tokens.
    # Shape: The word shape – capitalisation, punctuation, digits.
    # is alpha: Is the token an alpha character?
    # is stop: Is the token part of a stop list, i.e. the most common words of the language?
    nlp = spacy.load('en_core_web_sm')
    text = "The present invention relates to the use of gallium beam lithography to form superconductive structures. Generally,  the method includes exposing a surface to gallium to form an implanted region and then removing material adjacent to and/or below that implanted region. In particular embodiments,  the methods herein provide microstructures and nanostructures in any useful substrate,  such as those including niobium,  tantalum,  tungsten,  or titanium."
    doc = nlp(text)

    # 文档分析
    print("doc")
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

    # 命名实体抽取
    print("doc.ents")
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

    # 名词短语
    print("doc.noun_chunks")
    for np in doc.noun_chunks:
        print(np.text)
        # print(np.text, np.root.dep_, np.root.head.text)
    # displacy.serve(doc, style='ent')

# pre_process_en()


nlp = spacy.load('en_core_web_sm')
with open(r"Data\RawData\corpus_en.txt", 'r', encoding="UTF8") as en_Reader,\
        open(r"Data\Other\word_en.txt", 'w', encoding="UTF8") as Writer:
    texts_en = [line.strip() for line in en_Reader.readlines()]
    i = 1
    for document in texts_en:
        print(i)
        Writer.write("第{0}篇:\n".format(i))
        i+=1
        doc = nlp(document)
        for np in doc.noun_chunks:
            print(np.text)
            Writer.write(np.text+"\n")

