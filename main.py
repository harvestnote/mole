import requests
import re
import os
import wget
from collections import deque
import requests
from io import BytesIO
from PIL import Image


begian_url="https://www.520mojing.com/thread-13295-1-1.html"
url_data = deque([])
url_data.append(begian_url)
jpg_data = deque([])

def get_url(begian_url):
    if requests.get(begian_url).status_code == 200:
        print("url....ok")
        pattern = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.html")
        pattern_jpg = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg")

        reponse = requests.get(begian_url)
        content = reponse.text

        get_url_result = pattern.findall(content)
        get_jpg_result = pattern_jpg.findall(content)

        os.system("pause")

        print("begian_url: "+begian_url)
        del url_data[0]

        url_data.extend(get_url_result)
        jpg_data.extend(get_jpg_result)

        print("\n")
        print("jpg_data:" + str(len(jpg_data)))
        os.system("pause")

        if os.getcwd() != 'd:\mole\image':
            print(os.getcwd())
            os.chdir("image")

        for i in range(len(jpg_data)):
            print(i,end=":")
            print("get_jpg:"+jpg_data[i])
            response = requests.get(jpg_data[i])
            tmpIm = BytesIO(response.content)
            im = Image.open(tmpIm)
            if im.size[0] > 1000 and im.size[1] > 1000:
                wget.download(i)

        jpg_data.clear()

        get_url(url_data[0])
    else:
        print("url....false")
        del url_data[0]
        os.system("pause")
        get_url(url_data[0])


def test_url(url):
    if requests.get(url).status_code == 200:
        print("url....ok")
    else:
        print("url....false")


if __name__ == "__main__":
    get_url(begian_url)
