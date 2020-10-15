import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import json
check = []
a = 0
url = "http://example.com"
with open("hw1.json", "a", encoding = "utf-8") as file:
    file.write(f'[\n    "{url}",\n')
data = req.get(url)
data = data.content.decode('utf-8')
data = BeautifulSoup(data, "lxml")
x = 1
y = 1
z = 1
for url1 in data.findAll("a"):
    if urljoin(url, url1["href"]) not in check:
        check.append(urljoin(url, url1["href"]))
    else:
        continue
    if url1["href"][0:4] != "http":
        url = urljoin(url, url1["href"])
    else:
        url = url1["href"]
    data = req.get(url)
    data = data.content.decode('utf-8')
    data = BeautifulSoup(data, "lxml")
    print(f'{url}   {x}')
    x += 1
    for url1 in data.findAll("a"):
        if urljoin(url, url1["href"]) not in check:
            check.append(urljoin(url, url1["href"]))
        else:
            continue
        if url1["href"][0:4] != "http":
            url = urljoin(url, url1["href"])
        else:
            url = url1["href"]
        data = req.get(url)
        data = data.content.decode('utf-8')
        data = BeautifulSoup(data, "lxml")
        print(f'{url}   {x}-{y}')
        y += 1
print(len(check))
