# coding=utf-8
import pandas as pd
import random
import re
import time
import sys, os


# 信息抽取，主要使用正则抽取，直接返回可以按','分割，写入CSV文件的字符串。
# 函数内部的判断，全部都是确认网页内能不能get到对应的属性，get不到，就填空
def extractAmazonInformation(html):
    ID = re.findall('<b>ASIN: </b>(.*?)</li>', html, re.S | re.M)
    title = re.findall('<div class="ma-title"><p class="wraptext goto-top">(.*?)</p></div>', html, re.S | re.M)
    title2 = re.findall('<meta name="title" content="(.*?)"', html, re.S | re.M)
    price = re.findall('<span class="price">(.*?)</span>', html, re.S | re.M)
    price2 = re.findall('<span class="a-size-mini"> ￥(.*?)</span>', html, re.S | re.M)   #???
    price3 = re.findall('￥(.*?)</\)', html, re.S | re.M)
    shortInformation = re.findall('<ul class="a-unordered-list a-vertical a-spacing-none">(.*?)</ul>', html, re.S | re.M)
    information = re.findall('id="productDescription"(.*?)</div></div><div id="', html, re.S | re.M)
    category = re.findall('<span class="nav-search-label"(.*?)</span>', html, re.S | re.M)
    detail = re.findall('<span class="zg_hrsr_ladder">(.*?)</span>', html, re.S | re.M)   #????
    detail2= re.findall('<ul class="a-unordered-list a-horizontal a-size-small">(.*?)</ul>', html, re.S | re.M)
    detailRank = re.findall('<span class="zg_hrsr_rank">第(.*?)位</span>', html, re.S | re.M)    #?????
    categoryRanke= re.findall('亚马逊热销商品排名(.*?)\(<a', html, re.S | re.M)           #???
    keyword = re.findall('<meta name="keywords" content="(.*?)" />', html, re.S | re.M)
    productDetails = re.findall('<div class="wrapper CNlocale">(.*?)<div class="column col2 ">', html, re.S | re.M)
#???????????????????????????????????
    dr = re.compile(r'<[^>]+>', re.S)
    a1 = re.compile(r'&.*?;')
    chinese = re.compile(r'[\u2E80-\uFE4F]{2,7}')

    if len(ID) == 0:
        ID = ['']

    if len(title) == 0:
        title = title2
    if len(title) == 0:
        title = ['']

    if len(productDetails) == 0:
        productDe = ['']
    else :
        productDe = dr.sub('',str(productDetails[0]).replace('-&nbsp;','').replace('- ','').replace('&gt; ','/'))

    if len(price) == 0:
        price = price2
        if len(price2) == 0:
            price = price3
            if len(price3) == 0:
                price = ['']
    if len(shortInformation) != 0:
        baseInfo = dr.sub('', str(shortInformation[0]).replace('\n','').replace('	','').replace('  ',''))
        Info = a1.sub('', baseInfo)
    else :
        Info = ''
    if len(information)!=0 :
        aa = '<' + str(information[0]).replace('\n', '').replace('	', '').replace('  ', '')
        baseInfo2 = dr.sub('', aa)
        Info2 = a1.sub('', baseInfo2)
    else :
        Info2 = ''

    if len(detail) != 0:
        detailin = dr.sub('',str(detail[0]).replace('-&nbsp;','').replace('- ','').replace('&gt; ','/'))
    elif len(detail2) != 0:
        detailin = dr.sub('',str(detail2[0]).replace('-&nbsp;','').replace('- ','').replace('&gt; ','/').replace('\n','').replace('›',''))
    else :
        detailin = ['']

    if len(detailRank) == 0:
        detailRank = ['']

    if len(categoryRanke) == 0:
        categoryRankeIn2 = ['']
    else:
        categoryRankeIn2 = re.findall('里排第(.*?)名', categoryRanke[0], re.S | re.M)

    category1 = ['']
    if len(category) != 0:
        category1 = chinese.findall(str(category[0]))

    if len(keyword) == 0:
        keyword = ['']
#???????????????????????????????
    return str(ID[0]) + ',' \
           + str(keyword[0]).replace(',','/').replace('、','/')\
           + ',' + str(title[0]).replace(',','/')\
           + ',' + str(price[0]).replace(',','').replace(' ','').replace('￥', '')\
           + ',' + str(category1[0])\
           + ',' + str(categoryRankeIn2[0]).replace(',','')\
           + ',' + str(detailin).replace(',','/').replace(' ','')\
           + ',' + str(detailRank[0])\
           + ',' + str(Info).replace(',','/')\
           + ',' + str(Info2).replace(',','/') \
           + ',' + str(productDe).replace(',','/')

# 用来消除部分字符的函数
def replaceAll(text):
    return str(text).replace("\xa0"," ").replace("\n"," ").replace("\'"," ").replace("["," ").replace("]"," ").replace("\\"," ").replace("'"," ")


if __name__ == '__main__':
    # 读取路径下的文件数量


    root_dirs = os.listdir('./contents/')
    output = open("data.csv", "a+", encoding='UTF-8')

    for p in root_dirs:
        dirs = os.listdir('./contents/' + p)

        for f in dirs:
            filename = './contents/' + p + '/' + f
        # 遍历路径下的所有网页文件，并抽取为一个csv文件
            print(p,f)
            input = open(filename, 'r', encoding='UTF-8')
            txt = input.read()

            information = extractAmazonInformation(str(txt))

            output.write(p+','+replaceAll(information) + '\n')

            

    output.close()


