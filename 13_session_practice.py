import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'

ss = requests.session()
print(ss.cookies)

# Session1
# res = requests.get(url, headers=headers)
res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
button = soup.select('button[class="btn-big"]')[0]
print(button)
print(button['name'])
print(button['value'])
print(ss.cookies)

hidden = soup.select('input')
print(hidden)

data = {}
data[button['name']] = button['value']
for k in hidden:
    data[k['name']] = k['value']
print(data)

# Session2
target_url = 'https://www.ptt.cc/ask/over18'
# res_target = requests.post(target_url, data=data, headers=headers)
res_target = ss.post(target_url, data=data, headers=headers)
print(ss.cookies)

# Session3
final_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# final_res = requests.get(final_url, headers=headers)
final_res = ss.get(final_url, headers=headers)
# print(final_res.text)

print(ss.cookies)