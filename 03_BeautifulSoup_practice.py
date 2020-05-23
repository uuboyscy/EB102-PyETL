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
# print(soup)

# logo = soup.findAll('a', {'id': 'logo'})
# logo = soup.findAll('a', id='logo')
# logo = soup.select('a[id="logo"]')
logo = soup.select('a#logo')
print(logo)
print(logo[0])
print(logo[0].text)
print('https://www.ptt.cc' + logo[0]['href'])
