import requests
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def upload(origin_file, text_file):
    url = "http://2d4f0cd9.ngrok.io/files/upload/beu1aom3uqu3i63q4s30"
    files = {"origin_file":open(origin_file,'rb'),"text_file":open(text_file,'rb')}
    data = {"Remark": "this   is a test"}
    headers = {"Content-type":"multipart/form-data"}
    response = requests.post(url, headers=headers,data=data, files=files)
    print(response.text)

rawfile = r"Data/RawData/stopwords_cn.txt"
upload(rawfile,rawfile)


url = "http://2d4f0cd9.ngrok.io/files/upload/beu1aom3uqu3i63q4s30"

payload = "Content-Disposition: form-data; name=\"origin_file\"; filename=\"=\"output.pdf\"" \
          "\r\"\r\nContent-Type: application/pdf\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "afc7cba1-d41e-4776-87a4-06f80cb59f40"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)