# coding=utf-8
import requests
import random
import os
import time
import re

import json



for i in range(1,150000):
    url= 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,20&tags=%E7%94%B5%E5%BD%B1&start={}'.format(str(i*20))
    # if i>2:
    #     continue
    html = requests.get(url).text
    time.sleep(0.5)
    # html1 = r.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(r.text)[0])
    # print(html)
    #解析json数据
    text = json.loads(html)
    print('name_num:  ',i,'=====================','\n\n')
    print('**************  content  ****************\n\n',text,'\n\n')
    num = 0
    mo_list = text['data']
    for mo in mo_list:
        num+=1
        title = mo['title']
        url  = mo['url']
        # "title": "肖申克的救赎", "url": "https:\/\/movie.douban.com\/subject\/1292052\/",
        print(num,'***',title,'***',url,'***')
        with open('movie_DB_url.csv', 'a', encoding='utf-8') as w:
            w.write(url + '\n')
        # with open('movie_DB_name.csv', 'a', encoding='utf-8') as f:
        #     f.write(title + '\n')
print('ending...')


