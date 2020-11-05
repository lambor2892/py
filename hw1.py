import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import json
import sys

def getatags(url):
    urls = []  # 在 function 的 scope 裡宣告變數 urls 才不會讓人混淆說這在哪裏被宣告
    data = req.get(url).content.decode('utf-8')
    a_tags = BeautifulSoup(data, "lxml").findAll("a")
    for a_tag in a_tags:
        urls.add(urljoin(url, a_tag["href"]))
    return urls


# url 改成 root_url 避免與下面的變數閱讀上混淆，也可避免變數污染造成除錯困難
root_url = sys.argv[1]   # 簡單這樣從 command line 取得 input，方便測試
                    # 更好的拿法可參考 https://docs.python.org/zh-tw/3/howto/argparse.html
urls = set()
urls.add(root_url)
getatags(root_url)  # NOTE: 思考如何將這一行移到 while 之中

userinput = sys.argv[2]  # 簡單這樣從 command line 取得 input，方便測試
count = 2
urlscopy = urls.copy()  # NOTE: 不需要特別 copy，是否有什麼理由呢？
while count <= userinput:
    # NOTE: 思考在這裡令一個變數 tmp_urls = [] 來儲存 getatags() 的結果

    # 並妥善運用 urls 與 urlscopy 的差別
    # urls 可以當成你搜集不重複的 URL 之用的籃子
    # urlscopy 命名若改成 jobs，用來存放下一層要繼續抓的 URL(s)，那麼你會怎麼繼續改進程式碼？
    for url in urlscopy:  # 應使用有意義的命名，與上面的 url 衝突？可改成別的名稱
        nexturls = getatags(url)
        for x in nexturls:
            urls.add(x)
    count += 1
    urlscopy = nexturls


# 單純的儲存需求，先暫時拉的離主程式遠一點
# NOTE: 可以寫一個 function 來儲存需求，試著想想看如何「結構化」你的程式碼
urls = list(urls)
urlsdict = {}
for c in urls:
    urlsdict[c] = c
print(urlsdict)
# 程式碼就像英文書寫，大部分都像英文書寫一樣的風格
# open() 的第二參數使用 "a"，雖然在這邊可以動，但需要你們自行去了解是什麼意思，並作修正
# ref: https://www.google.com/search?q=python+open
with open("urldata.json", "a", encoding="utf-8") as file:
    json.dump(urlsdict, file)
