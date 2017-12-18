# coding=utf-8
import pandas as pd
import random
import re
import codecs
from scrapy.selector import Selector
from urllib import request
import urllib.request, urllib.parse, urllib.error
import sys, os

global saveFlag
saveFlag = True

# request 代理
user_agents = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",]

# 获取列表页面的内容，返回目录页的html
def gethtml1(pagesUrl):
    int = 0
    while int < 200:
        try:
            # 随机选取一个agent
            index = random.randint(0, 15)
            user_agent = user_agents[index]
            head = {'User-Agent': user_agent}
            req = request.Request(pagesUrl, headers=head)
            response = urllib.request.urlopen(req)
            content = response.read().decode('utf-8')
            break
        except RuntimeError:
            print('time exceeded2', int)
            # try:
            #     driver.quit()
            #     display.stop()
            # except UnboundLocalError as ex:
            #     print(ex)
            continue
    return content


# 访问列表页的每一页
def everyPages(url,root1,root2,root3,name1, name2, name3):
    # 创建对应的目录
    path = str(root1) + '/' + str(root2)
    if os.path.exists(str(root1)) == False:
        os.mkdir(str(root1))
    if os.path.exists(path) == False:
        os.mkdir(path)
    # 循环访问每一页
    for i in range(1000):
        # 获取列表页html
        html = gethtml1(url)
        # 锁定商品框
        texts = Selector(text = html).xpath('//*[@id="plist"]/ul/li/div/div[@class="p-img"]/a').extract()

        # 获取具体链接，并写入txt文档
        output = codecs.open(str(path) + '/' + str(root3) + '.txt', "a+", encoding='utf-8')
        for text in texts:
            items = re.findall(r'<a target="_blank" href="(.*?)">', text)
            print(name1,name2,name3,i, items[0])
            output.write('https:' + str(items[0])  + '\n')
        output.close()

        # 获取下一页的链接，如果没有，跳出函数
        nextpage = re.findall('<a class="pn-next" href="(.*?)"', html)
        if len(nextpage) == 0:
            return 0
        url = 'https://list.jd.com' + str(nextpage[0])
        # time.sleep(random.randint(3, 6))



# 这个函数里面的循环代码很复杂，我写完后...自己就理不清出这个逻辑，但是绝对是对的。
# 总体就是遍历每一个‘一级分类---二级分类---三级分类----打开三级分类的页面调用everyPages遍历列表页’
def SearchJD():
    # root.txt 是配置文件，内容是一部分‘京东全部分类’那个页面的html
    input = codecs.open('root.txt', 'r', encoding='UTF-8')
    txt = input.read()
    root_title0 =Selector(text = str(txt)).xpath('//div[@class="category-item m"]/div[@class="mt"]/h2[@class="item-title"]/span').extract()
    root2_title =Selector(text = str(txt)).xpath('//div[@class="category-item m"]/div[@class="mc"]/div[@class="items"]').extract()

    global saveFlag
    i1 = 0
    j1 = 0
    l1 = 0

    # 读取保存文件
    if saveFlag == True:
        load2 = pd.read_csv('save.csv', header=None, encoding='utf-8', sep=',')
        i1 = load2.iat[0, 0]
        j1 = load2.iat[0, 1]
        l1 = load2.iat[0, 2] + 1
        saveFlag = False

    # 三层循环，遍历访问每一个三级分类
    for i in range(i1, len(root_title0)):
        root = re.findall('<span>(.*?)</span>' ,root_title0[i])
        root2_title1 = Selector(text=str(root2_title[i])).xpath('//dt/a').extract()
        if saveFlag == False:
            j1 = 0
        for j in range(j1, len(root2_title1)):
            root2 = re.findall('>(.*?)</a>' ,root2_title1[j])
            root3_title = Selector(text=str(root2_title[i])).xpath('//dl/dd').extract()
            texts = Selector(text=str(root3_title[j])).xpath('//a').extract()

            if saveFlag == False:
                l1 = 0
            for l in range(l1, len(texts)):
                items = re.findall(r'<a href="(.*?)" target="_blank">', texts[l])
                name = re.findall(r'" target="_blank">(.*?)</a>', texts[l])
                if items[0].split('.')[0][2:] != 'list':
                    continue
                everyPages('https:' + str(items[0]),i,j,l,root[0], root2[0], name[0])

                save = codecs.open('save.csv', "w+", encoding='utf-8')
                save.write(str(i) + ',' + str(j) + ',' + str(l))
                save.close()




if __name__ == '__main__':
    SearchJD()
