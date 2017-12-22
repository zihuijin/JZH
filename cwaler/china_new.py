# coding:utf-8
import requests
import re
# s = re.findall(r'<div class="left_zw" style="position:relative">(.*?)<embed',str(o),re.I | re.S)
# print(s[0])
#
# a = re.findall(r'<ul class="module_con_ul">(.*?)</ul>',html,re.I|re.S)
# print('a:',len(a))
#
# for i in a:
#     print(i)
#     b = re.findall(r'<a href=(.*?)>(.*?)</a>',i,re.I|re.S)
#     print('b',len(b))
#     for j in b:
#         print(j[0])
#
#         print(j[1])



content = []

def gethtml(base_url):
    global html

    res = requests.get(base_url)
    if res.status_code==200:
        res.encoding = 'GBK'
        html = res.text
    else:
        print('htmlerror')
    return html

def geturl(html):
    # http: // www.chinanews.com / sh / 2017 / 11 - 29 / 8387744.shtml
    a = re.findall(r'<ul class="module_con_ul">(.*?)</ul>', html, re.I | re.S)
    print('zongduanshu:', len(a))
    list = []

    for i in a:
        print(i)
        b = re.findall(r'<a href=(.*?)>', i, re.I | re.S)
        print('urlnum_row:', len(b))
        for j in b:
            if j.find('chinanews')==-1:
                list.append('http://www.chinanews.com' + str(j))
                print('http://www.chinanews.com' + str(j))
            else:
                list.append('http:' + str(j))
                print('http:' + str(j))
    return list

def getcontent(list):
    for url in list:

        print(url)
        html1 = gethtml(url)
        pattern = r'<div class="left_zw" style="position:relative">(.*?)<div class="left_name"'
        content.append(re.search(pattern,html1,re.I|re.S).group(1))
    return content

html = gethtml('http://www.chinanews.com/')
url = geturl(html)
print('sumurl:',len(url))
content1= getcontent(url)

count = 1
for i in content1:
    with open(str(count)+'.txt','w')as f:
        f.write('count:******'+str(count)+'*********************'+'\n\n')
        f.write(str(i)+'\n\n')
        count+=1












