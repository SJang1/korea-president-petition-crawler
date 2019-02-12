import requests
from bs4 import BeautifulSoup
import time
import os

codes = ["522031"]

def crawl(code):
    url = "https://www1.president.go.kr/petitions/{}".format(code)
    data = requests.get(url)
    return data.content

def user(string):
    httprequest = BeautifulSoup(string, "html.parser")

    wrapuser = httprequest.find("h2", {"class":"petitionsView_count"})
    users = wrapuser.find("span", {"class":"counter"})

    title = httprequest.find("h3", {"class":"petitionsView_title"})

    timestamp = time.ctime()

    return {"time":timestamp,"title":title.text, "agrees":users.text}

def main():
    for code in codes:
        predata = user(crawl(code))

        f = open("output.txt", "a")
        f.write(os.linesep + str(predata))
        f.close()

    time.sleep(150)
    main()
main()
