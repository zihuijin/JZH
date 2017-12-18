# coding=utf-8
import pandas as pd
import random
import re
import time
import sys, os
from scrapy.selector import Selector

def replaceAll(text):
    return str(text).replace("\n"," ").replace("\'"," ").replace("["," ").replace("]"," ").replace('，',' ')


# 信息抽取的函数，抽取内容同命名
def extractJDInformation(html):

    id1 = Selector(text=str(html)).xpath('//div[@class="left-btns"]').extract()
    id = re.findall('data-id="(.*?)"',str(id1))
    name = Selector(text=str(html)).xpath('//title/text()').extract()
    keyword = Selector(text=str(html)).xpath('//meta[@name="keywords"]/@content').extract()
    price = Selector(text=str(html)).xpath('//span[@class="p-price"]/span[2]/text()').extract()
    parameter = Selector(text=str(html)).xpath('//div[@class="p-parameter"]//*/text()').extract()
    detail1 = Selector(text=str(html)).xpath('//div[@class="detail-content-item"]//*/text()').extract()
    detail2 = Selector(text=str(html)).xpath('//div[@id="detail"]/div[2]/div[2]//*/text()').extract()
    commentCount = Selector(text=str(html)).xpath('//div[@id="comment-count"]/a/text()').extract()
    category =  Selector(text=str(html)).xpath('//div[@class="item first"]/a/text()').extract()

    if len(id)==0:
        id=['']
    if len(name)==0:
        name=['']
    if len(keyword)==0:
        keyword=['']
    if len(price)==0:
        price=['']

    if len(commentCount)==0:
        commentCount=['']
    if len(category)==0:
        category=['']

    list = str(id[0]).replace(',',' ') \
           + ',' + str(name[0]).replace(',',' ') \
           + ',' + str(keyword[0]).replace(',',' ')  \
           + ',' + str(price[0]).replace(',',' ') \
           + ','+ str(commentCount[0]).replace(',',' ') \
           + ','+ str(category[0]).replace(',',' ') \
           + ',' + str(parameter).replace(',',' ') \
           + ',' + str(detail1).replace(',',' ') \
           + ',' + str(detail2).replace(',',' ')
    #print(list.replace('\\n','').replace('  ',''))
    return replaceAll(list)


if __name__ == '__main__' :

    # 读取路径下的文件数量
    dirs = os.listdir('./')

    tmp=[]
    for d in dirs:
        if d.find('_')!=-1:
            tmp.append(d)
    dirs = tmp

    output = open("data_jd.csv", "a+", encoding='UTF-8')

    for d in dirs:
        fs = os.listdir(d)
        for f in fs:
        # 遍历路径下的所有网页文件，并抽取为一个csv文件
            filename = d +'/' + f
            input = open(filename, 'r', encoding='UTF-8')
            txt = input.read()

            information = extractJDInformation(str(txt))
            output.write(d+','+information + '\n')

            print(d,f)
    output.close()
