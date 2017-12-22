#coding:utf-8
import requests
import re
import urllib.request
import  os

# r = re.findall(r'<div class="thumb">\n\n<a href=(.*?) alt=', html, re.S | re.I)
# for i in r:
#     img = re.findall(r'<img src="(.*?)"', i)
#     print('http:'+str(img[0]))
#
url = 'https://www.qiushibaike.com/imgrank/'
res = requests.get(url,timeout = 0.5)
html = res.text



pages = 1
count = 1
while re.search('下一页',html):
    r = re.findall(r'<div class="thumb">\n\n<a href=(.*?) alt=', html, re.S | re.I)
    print('*****' + str(pages) + '******')
    print('sum:',len(r))
    for i in r:
        img = re.findall(r'<img src="(.*?)"', i)
        img_url = 'http:' + str(img[0])

        print(img_url)
        res =requests.get(img_url)         #requests.get().content 返回网页内容的字节形式     字符形式用requests.get().text
        # img1 = urllib.request.urlopen(img_url).read()   #urllib 返回网页内容的字节形式     字符形式用urllib.request.urlopen().read().decode()

        if res.status_code == 200:    #如果链接正常打开
        # res.raise_for_status()   # r.raise_for_status() #失败请求(非200响应)抛出异常 可以用try：  except requests.exceptions.ConnectionError：
            img1 = res.content
            if os.path.exists('pi'):
                pass
            else:
                os.mkdir('pi')

            pathName = 'pi/'+str(count)+'.jpg'  # 设置路径和文件名
            f = open(pathName, 'wb')    #图片是以字节方式写入
            f.write(img1)
            count += 1
        else:
            print('Linkopen error')
    pages +=1
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'%(pages)
    res = requests.get(url)
    html = res.text
f.close()

