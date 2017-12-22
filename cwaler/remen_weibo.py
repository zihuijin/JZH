
#coding:utf-8

import re
import time
import string
import sys
import os
import urllib
# import urllib2
from bs4 import BeautifulSoup
import bs4
import requests
from lxml import etree
import urllib.request
#得到页面，生成soup对象
def gethtml(url):
    try_time =1
    while try_time<20:
        try_time+=1
        cookie = {
            "Cookie": "_T_WM=f16f4a1bee6ff34ecda2868888ad6546; ALF=1515136067; SCF=AhRWkskDIqR__t_aafLb3KrbassNG8gLm-PlMan91r2qg2achRxqJydhiY2T0IgHeqVWdtF91_Qhe3uagRECTT8.; SUB=_2A253I-u6DeRhGeBM6VMW9ivMyDmIHXVU7_XyrDV6PUJbktANLWzZkW1NRRKNlV7rcvcouaHcPa2gRmcILoOhXd28; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Bzzm2qp5S0fdgcLv7fVCE5JpX5K-hUgL.FoqEeo2NSo-7e0-2dJLoI0zLxKBLBo.LBK5LxKqL1heLB-qLxKqL1h5LBKMLxK.L1-2L1K5LxKnLB.2LB-zN1K2fe5tt; SUHB=0M2Fb6wmyA2fQJ; SSOLoginState=1512545258; H5:PWA:UID=1; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D10000011%26lfid%3D1076031483330984"}
        html = requests.get(url, cookies=cookie).text
        if html=='':
            print('sleep......')
            time.sleep(2*60)
            continue
        # else:
        #     soup = BeautifulSoup(html, 'html.parser')
        return html


#热门微博

html = gethtml('https://weibo.cn/pub/topmblog')
soup = BeautifulSoup(html, 'html.parser')
print('html0:','******',str(html),'*******')
#评论

a2= soup.find_all('a',class_="cc")
print('a2_num  ',len(a2))

#遍历评论

pl_num = 0
for i in a2:
    pl_num +=1
    print('i', i)
    url_pl = str(i['href']).replace('https', '')
    url_pl = 'http' + str(re.match('^://wei.+?&', url_pl).group()) + 'rl=1' + '&page={}'
    # https://weibo.cn/comment/FyPC0yv0C?uid=1642591402&rl=1#cmtfrm
    # https://weibo.cn/comment/FyP6D3fnc?uid=5611361176&rl=1&page=2
    html = gethtml(url_pl.format(1))
    soup = BeautifulSoup(html, 'html.parser')
    try:
        page_sum = soup.select('input[name="mp"]')[0]['value']
    except IndexError:
        html = gethtml(url_pl.format(1))
        soup = BeautifulSoup(html, 'html.parser')
        print('html2:   ', '******', str(html), '*******')
        try:
            page_sum = soup.select('input[name="mp"]')[0]['value']
        except IndexError:
            page_sum = 2
    print('page_sum    ', page_sum)

    # 遍历评论页面

    for page_num in range(1, int(page_sum)):
        url = url_pl.format(page_num)
        print('\n', 'page:', pl_num, '-', page_num, '     url:   ', url, '**************************',
              '\n')
        # //*[@id="pagelist"]/form/div/text()[4]

        # url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%s&page=1'%('sousuo')
        # 搜索是%a%f得转码  ?????
        # .com
        # url = 'http://weibo.com/u/6221765035'
        html = gethtml(url)
        soup = BeautifulSoup(html, 'html.parser')
        print('html3', '******', str(html), '*******')
        # print(len(html))

        # if len(html) < 1024 * 5:------------------------
        #     pass
        # soup = BeautifulSoup(html)
        span_all = soup.find_all('span', class_="ctt")
        # 遍历评论页面所有评论

        for span in span_all:
            print(span)
            con_list = []
            for j in span.contents:
                if str(j) != '回复' and str(j) != ' ' and str(j) != ' \u200b\u200b\u200b' and type(
                        j) == bs4.element.NavigableString:
                    print('j   ', str(j).replace(':', ''))
                    con_list.append(str(j).replace(':', ''))
            con = ''.join(con_list)
            if con == '':
                continue
            print('con:   ', con)
            with open('pinglun.txt', 'a') as f:
                f.write(str(con).replace(':', '') + '\n')
