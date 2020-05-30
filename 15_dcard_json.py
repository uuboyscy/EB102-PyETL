import requests
import json
from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555'

res = requests.get(url, headers=headers)

# print(res.text)
json_data = json.loads(res.text) # The string will be transformed to a list

# print(json_data[0])
# print(json_data[1])
# print(json_data[2])
#
# for k in json_data[1]:
#     print(k)

# Get title
for t in json_data:
    title_name = t['title']
    print(title_name)

    article_url = 'https://www.dcard.tw/f/game/p/' + str(t['id'])
    print(article_url)

    # get images url
    image_url_list = [img['url'] for img in t['mediaMeta']]

    image_url_list2 = []
    for img in t['mediaMeta']:
        image_url_list2.append(img['url'])

    print(image_url_list)
    for image_url in image_url_list:
        # request.urlretrieve(image_url, './dcardimg/' + image_url.split('/')[-1])
        res_img = requests.get(image_url, headers=headers)
        img_content = res_img.content
        with open('./dcardimg/' + image_url.split('/')[-1], 'wb') as f:
            f.write(img_content)



