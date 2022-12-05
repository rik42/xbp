import urllib.request

imgname = "logo_courses_ai.png"

url = "https://aiacademy.jp/assets/images/" + imgname

# urlretrieveの第一引数はアップロードされている画像のURL、第二引数には保存したい画像ファイル名
urllib.request.urlretrieve(url, imgname)

print("保存完了")

from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://aiacademy.jp/assets/scraping/sample1.html")
data = html.read()
html = data.decode('utf-8')

# HTMLを解析
soup = BeautifulSoup(html, 'html.parser')

# 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
title = soup.find("title")
body = soup.find("body")

print("title: " + title.text)
print("body: " + body.text)
import requests
from bs4 import BeautifulSoup
url = "https://kulms.kanagawa-u.ac.jp/webclass/"


# 株価の取得
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
price = soup.find("span", attrs={'class':'mkc-stock_prices'})
print(price.text)