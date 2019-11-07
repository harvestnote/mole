import requests
import re
import os
import wget

def get_url(url):
    pattern = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg")

    reponse = requests.get(url)
    content = reponse.text
    get_url_result = pattern.findall(content)

    url_data = []

    for url in get_url_result:
        test_url = requests.get(url)
        if test_url.status_code == 200:
            url_data.append(url)


    return url_data


if __name__ == "__main__":
    