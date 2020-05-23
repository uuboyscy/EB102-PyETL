from urllib import request
from bs4 import BeautifulSoup
# For Mac
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

# print(res.read().decode('utf-8'))

soup = BeautifulSoup(res.read(), 'html.parser')

# print(soup.select('a'))
title = soup.select('div.title')
print(title[0])
print('=========')
print(title[0].select('a'))
print(title[0].select('a')[0])
print(title[0].select('a')[0].text)
print(title[0].a.text)
print(title[0].a)
print('https://www.ptt.cc' + title[0].select('a')[0]['href'])
