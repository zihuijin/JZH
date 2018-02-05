# coding=utf-8
import requests
import random
import os
import time
import re
import bs4
from  bs4 import BeautifulSoup
import json


# url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1000&page_start=0'
classname_list = ['热门','最新','经典','可播放','豆瓣高分','冷门佳片','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','动画']

name_num = 0
for name in classname_list:
    name_num+=1
    # if name_num>2:
    #     continue

    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={}&sort=recommend&page_limit=1000&page_start=0'.format(name)
    # https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1100&page_start=0
    html = requests.get(url).text
    # html1 = r.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(r.text)[0])
    # print(html)
    #解析json数据
    text = json.loads(html)
    print('**************  name_num  ****************\n\n',text)
    num = 0
    mo_list = text['subjects']
    for mo in mo_list:
        num+=1
        title = mo['title']
        url  = mo['url']
        # "title": "肖申克的救赎", "url": "https:\/\/movie.douban.com\/subject\/1292052\/",
        print(num,'***',title,'***',url,'***')
        with open('movie_DB_url.csv', 'a', encoding='utf-8') as w:
            w.write(url + '\n')
        with open('movie_DB_name.csv', 'a', encoding='utf-8') as f:
            f.write(title + '\n')
print('ending...')
with open('movie_DB_name.csv') as f:
    name_list = f.readlines()
name_set = set(name_list)
print('name_QC_num:  ',len(name_list),len(name_set))
