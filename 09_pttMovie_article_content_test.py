import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

title_url = 'https://www.ptt.cc/bbs/movie/M.1590058721.A.C94.html'

res_article = requests.get(title_url, headers=headers)

soup_article = BeautifulSoup(res_article.text, 'html.parser')

# print(soup_article)
article_content_list = soup_article.select('#main-content')
article_content = article_content_list[0].text.split('※ 發信站')[0]
# print(article_content_list[0].text.split('※ 發信站')[0])
