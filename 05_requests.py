# from urllib import request
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

res = requests.get(url, headers=headers)

# html string
print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
print(soup)