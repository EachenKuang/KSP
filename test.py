import nltk
import re
import jieba
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

"""
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext))
print(word_tokenize(mytext))

from nltk.corpus import wordnet
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))


# 中文分词
mytext = "我是匡奕臣，我的名字叫Eachen。我今天18岁了！"
text=nltk.text.Text(jieba.lcut(mytext))
"""
# text2 = "Pressure may be applied to the contacting material through the pressing tool,  and the contacting material may be heated inside the cavity. Pressure and heat may be applied simultaneously,  at least during part of the process. A superconducting connection structure including at least two superconducting wires,  each wire including at least one superconducting filament,  and a superconducting connection between the end pieces of the two wires is also disclosed. The connection may be formed of heated and compressed contacting material including MgB2."
# text = "A method for forming superconducting connection structure between at least two superconducting"
# text = "A method"
# print(list(nltk.ne_chunk_sents(text, binary=True)))
# print(list(nltk.ne_chunk_sents(text)))
document = "A system includes :  a chip (100) including a superconducting quantum computing circuit element (118);  a printed circuit board (102) including a laminate sheet (114) a first superconductor layer including a signal line (110) and a ground line (112) on a first side of the laminate sheet,  a second superconductor layer (122) on a second side of the laminate sheet,  the second side opposing the first side,  and a via (126) extending from the first superconductor layer through the laminate sheet to the second superconductor layer,  in which the via includes a third superconductor material (124) that electrically connects the first superconductor layer to the second superconductor layer;  and a superconductor coupling (element 116a),  (116b) that electrically couples the chip to the first superconductor layer of the printed circuit board."
document = "Two men are due to appear before the Special Criminal Court this morning charged in connection with the murder of Aidan 'The Beast' O'Driscoll in Cork in December 2016.\
The two men, aged 24 and 32, were arrested this morning in Cork.Aidan 'The Beast' O'Driscoll (37) died after he was ambushed and shot up to four times on December 7, 2016 as he walked in Blackpool in Cork city.In order to provide a superconducting wire rod connection structure having high connection strength and large superconducting critical current density,  a connection structure (100),  in which respective connection ends of first and second superconducting wire rods (10A,  10B) in each of which a superconducting conductor layer (3) is formed on one surface of a substrate (1) with an intermediate layer (2) therebetween are connected,  has a configuration in which the respective substrates of the first and second superconducting wire rods are joined by welding,  a connection wire rod (10C) having a superconducting conductor layer (3C) is laid between the superconducting conductor layers of the first and second superconducting wire rods,  and a separation part (6) formed by the connection ends and the connection wire rod being separate from each other is provided between the connection ends of the first and second superconducting wire rods joined by joining parts of the substrates and the connection wire rod."
# sentences = nltk.sent_tokenize(document)
# print("sentences"+"-"*30)
# print(sentences)
words = nltk.word_tokenize(document)
word_tag = nltk.pos_tag(words)
# print(word_tag)

# 使用NE分块器进行命名实体识别，返回Tree对象，
# Tree对象的label()方法可以查看命名实体的标签
for tree in nltk.ne_chunk(word_tag, binary=True).subtrees():
    # 过滤根树
    print(tree)

document_cn = "一种方法形成超导本发明公开了一种超导导线至少两个之间的连接结构，其中，每个导线包括至少一个超导细丝。每根超导导线的端件可位于空腔内的压紧治具。接点材料包括MgB2的MgB2和/或其前体材料也可以位于空腔内。压力可以施加到接触材料通过压合治具，所述接触材料可以加热腔内。压力和热量可被应用于同时，至少在部分的方法。包括至少两根超导线的超导连接结构，每个导线包括至少一个超导细丝，和所述端部构件之间的超导连接的两根导线也被公开。所述连接可以被加热并压缩形成接触材料包括mgb2。"
text=nltk.text.Text(jieba.lcut(document_cn))
word_tag = nltk.pos_tag(text)
for tree in nltk.ne_chunk(word_tag, binary=True).subtrees():
    # 过滤根树
    print(tree)
print(stopwords.words('english'))
