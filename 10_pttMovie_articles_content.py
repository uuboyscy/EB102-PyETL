import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('pttmovie'):
    os.mkdir('pttmovie')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0, 5):
    # HTML String
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    title_list = soup.select('div.title')
    # print(title_list)

    for title_soup in title_list:
        # print(title_soup)
        try:
            title = title_soup.select('a')[0].text
            title_url = 'https://www.ptt.cc' + title_soup.select('a')[0]['href']

            # Get article content
            res_article = requests.get(title_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, 'html.parser')
            # print(soup_article)
            article_content_list = soup_article.select('#main-content')
            article_content = article_content_list[0].text.split('※ 發信站')[0]
            # Save article
            try:
                with open('./pttmovie/%s.txt'%(title), 'w', encoding='utf-8') as f:
                    f.write(article_content)
            except FileNotFoundError as e:
                print(e)
                print(title)
                with open('./pttmovie/%s.txt'%(title.replace('/', '-')), 'w', encoding='utf-8') as f:
                    f.write(article_content)

            print(title)
            print(title_url)
            # print(article_content)
            print('===================================')
        except IndexError as e:
            print(title_soup)

    # Get last-page url
    page_url_soup = soup.select('a[class="btn wide"]')
    # print(page_url_soup)
    last_page_url = 'https://www.ptt.cc' + page_url_soup[1]['href']
    # print(last_page_url)

    url = last_page_url