import requests
import re
import os
import wget
from collections import deque
import requests
from io import BytesIO
from PIL import Image




def get_url(start_url,url_data,url_patten):
    if requests.get(start_url).status_code == 200:
        print(start_url+"url ok......")

        reponse = requests.get(start_url)
        content = reponse.text

        get_url_resuit = url_pattern.findall(content)
        url_data.extend(get_url_resuit)
        print("url_data_num:" + str(len(url_data)))

        return url_data

def get_jpg_url(url_data, jpg_data, jpg_patten, count):
    print("count :" + str(count))
    if count<11:
        if requests.get(url_data[0]).status_code == 200:
            print(url_data[0]+"is  ok......")
            print("start_jpg_url: "+url_data[0])

            response = requests.get(url_data[0])
            content = response.text

            get_jpg_url_result = jpg_pattern.findall(content)

            jpg_data.extend(get_jpg_url_result)
            print("jpg_data_num:" + str(len(jpg_data)))



    else:
        return jpg_data

    return jpg_data
    #count+=1
    #get_jpg_url(url_data,jpg_data,jpg_pattern,count)

def download_Catalog():
    print("current Catalog is "+os.getcwd())
    if os.getcwd() != 'd:\mole\image':
        os.chdir("image")
        print("current Catalog is "+os.getcwd())

def download_jpg(jpg_data):
    for i in range(len(jpg_data)):
        print(i,end=" : ")
        print("jpg url is :"+jpg_data[i])
        response = requests.get(jpg_data[i])
        tmpIm = BytesIO(response.content)
        im = Image.open(tmpIm)
        if im.size[0] > 500 and im.size[1] > 500:
            wget.download(jpg_data[i])
        print("download end......")



if __name__ == "__main__":
    start_url = "https://www.520mojing.com/thread-33787-1-1.html"

    url_data = deque([])
    url_data.append(start_url)
    jpg_data = deque([])

    url_pattern = re.compile("[a-zA-z]+://[^\s]*")
    jpg_pattern = re.compile("[a-zA-z]+://[^\s]*.jpg")
    count = 0


    url_data = get_url(start_url, url_data, url_pattern)
    jpg_data = get_jpg_url(url_data, jpg_data, jpg_pattern, count=0)
    download_Catalog()
    download_jpg(jpg_data)
