

#爬取糗事百科-----------
#coding:utf-8
import requests
import re

url = 'https://www.qiushibaike.com/text/'
res = requests.get(url)
html = res.text
pages = 1
while re.search('下一页',html):
    r = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S|re.I)
    s =r.findall(html)
    print('*****' + str(pages) + '******')
    f = open('qsbk.txt', 'a')
    f.write('**********' + 'pages' + str(pages) + '************' + '\n\n')
    print('sum:',len(s))
    for i in s:
        t = re.sub(r'\n','',i)
        y = re.sub(r'<br/>','  ',t)
        print(y)
        print()
        f.write(y+'\n\n')



    pages += 1
    url = 'https://www.qiushibaike.com/text/page/%d/'%(pages)
    res = requests.get(url)
    html = res.text
f.close()

