import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import json



def getatags(url):
    data = req.get(url).content.decode('utf-8')
    a_tags = BeautifulSoup(data, "lxml").findAll("a")
    for a_tag in a_tags:
        urls.add(urljoin(url, a_tag["href"]))
    return urls

url = input("輸入網址: ")
urls = set()
urls.add(url)
getatags(url)

userinput = int(input("輸入需要統計的層數: "))
count = 2
urlscopy = urls.copy()
while count <= userinput: 
    for z in urlscopy:
        nexturls = getatags(z)
        for x in nexturls:
            urls.add(x)
    count += 1
    urlscopy = nexturls
urls = list(urls)
urlsdict = {}
for c in urls:
    urlsdict[c] = c
print(urlsdict)
with open("urldata.json","a", encoding = "utf-8") as file:
    json.dump(urlsdict, file)