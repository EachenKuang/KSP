# step0 excel => corpus_cn + corpus_en
# RawData\superconductor.xls =>
# (1)   RawData\corpus_cn.txt
# (2)   RawData\corpus_en.txt
import xlrd
import logging
import nltk
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


CHINESE_CORPUS_FILE_PATH = r"Data\RawData\corpus_cn.txt"
ENGLISH_CORPUS_FILE_PATH = r"Data\RawData\corpus_en.txt"
EXCEL_FILE_PATH = r"Data\RawData\superconductor.xls"
NLTK_PACKAGE_PATH = r"nltkPackage.txt"


# 将中英文分别写入文件
def write_divided_abstract():
    excel_file = xlrd.open_workbook(EXCEL_FILE_PATH)
    sheet = excel_file.sheet_by_index(0)
    # print(sheet.name,sheet.nrows,sheet.ncols)
    ROW_NUM = sheet.nrows  # 在循环中需要去掉标题行
    cols1 = sheet.col_values(4)  # 摘要
    cols2 = sheet.col_values(5)  # 摘要（翻译）
    # print(type(cols1[1]))

    with open(CHINESE_CORPUS_FILE_PATH, 'w', encoding="UTF8") as cnWriter,\
            open(ENGLISH_CORPUS_FILE_PATH, 'w', encoding="UTF8") as enWriter:
        for i in range(1, ROW_NUM):
            if not cols1[i]:
                pass
            if len(cols1[i].split()) > len(cols2[i].split()):
                # 使用分割方法判断中英文：英文中的空格数一定大于中文中的空格
                cnWriter.write(cols2[i])
                enWriter.write(cols1[i])
            else:
                cnWriter.write(cols1[i])
                enWriter.write(cols2[i])
            cnWriter.write("\n")
            enWriter.write("\n")


def install_nltk_package():
    with open(NLTK_PACKAGE_PATH,'r') as Reader:
        for line in Reader.readlines():
            nltk.download(line.strip())


if __name__ == '__main__':
    # 安装nltk依赖包
    # install_nltk_package()
    # write_divided_abstract()
    pass



