#
import logging
from stanfordcorenlp import StanfordCoreNLP
# nlp = StanfordCoreNLP(r'StanfordCoreNLP',lang="zh", logging_level=logging.DEBUG)
nlp = StanfordCoreNLP(r'StanfordCoreNLP',lang="en", logging_level=logging.DEBUG)

sentence = "Physical superconducting qubits are controlled according to an “encoded” qubit scheme,  where a pair of physical superconducting qubits constitute an encoded qubit that can be controlled without the use of a microwave signal. For example,  a quantum computing system has at least one encoded qubit and a controller. Each encoded qubit has a pair of physical superconducting qubits capable of being selectively coupled together. Each physical qubit has a respective tunable frequency. The controller controls a state of each of the pair of physical qubits to perform a quantum computation without using microwave control signals. Rather,  the controller uses DC-based voltage or flux pulses."
# sentence = "物理超导量子位（qubits）按照“控制”量子位编码方案在那里，一对编码的物理超导量子位（qubits）构成的量子位可以被控制，而不使用微波信号。例如，量子计算的系统具有至少一个量子位编码和控制器。每个编码的量子位的物理超导量子位（qubits）具有一对可选择地连接在一起。每个物理具有各自的频率可调谐的量子位。控制器控制每个所述一对物理状态的量子位进行量子计算，而不需要使用微波控制信号。相反，该控制器使用基于DC电压或通脉冲。"
sentence="A multi-layer semiconductor structure includes a first semiconductor structure and a second semiconductor structure,  with at least one of the first and second semiconductor structures provided as a superconducting semiconductor structure. The multi-layer semiconductor structure also includes one or more interconnect structures. Each of the interconnect structures is disposed between the first and second semiconductor structures and coupled to respective ones of interconnect pads provided on the first and second semiconductor structures. Additionally,  each of the interconnect structures includes a plurality of interconnect sections. At least one of the interconnect sections includes at least one superconducting and/or a partially superconducting material."
print(nlp.word_tokenize(sentence))
print("-"*20+ "the part-of-speech (POS) tagger")
print(nlp.pos_tag(sentence))  # the part-of-speech (POS) tagger
print("-"*20 + "the named entity recognizer")
print(nlp.ner(sentence))  # the named entity recognizer
print("-"*20)
print(nlp.parse(sentence))
print("-"*20)
print(nlp.dependency_parse(sentence))
nlp.close()


