# coding=utf-8
import pandas as pd
import random
import re
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import codecs
import signal
from urllib import request
import urllib.request, urllib.parse, urllib.error
import sys, os


display = Display(visible=0, size=(800, 800))
display.start()
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
# 用来读取已保存进度的全局变量。
global saveFlag
saveFlag = True

# # 计时用的函数
# def timed_out(b, c):
#     print('alarmed')
#     raise RuntimeError()

# 获取商品页面内容
def gethtml1(url_root):
    global driver
    int1 = 0
    html=''
    while int1 < 10:

        # 配合计时函数，开一个信号来计算时间，超时便报错，然后except重新再爬这个网址。要是200次都报错就跳过该网址
        #（有时候因为网络或者模拟浏览器的问题，程序会卡住但不会报错跳出，用这个方法识别超时，手动报出错，catch错误后重新爬）
        #signal.signal(signal.SIGALRM, timed_out)
        #signal.setitimer(signal.ITIMER_REAL, 10, 0)

        try:
            #模拟chrome，并消除浏览器图像化，以便在服务器里运行
            int1 = int1 + 1

            driver.get(url_root.replace('amp;', '').replace('&th=1', ''))

            #打印当前网址
            print(driver.current_url)

            html = driver.page_source.encode('utf-8','ignore').decode()
            if html.find('您输入的网址在我们的网站上无法正常显示网页')!= -1:
                print('good is missing')
                html=""
            elif html.find('抱歉，我们只是想确认一下当前访问者并非自动程序') != -1:
                print('block 1...')
                f= open('tmp/fp.txt','w')
                f.write(html)
                f.close()
                driver.get_screenshot_as_file("tmp/fp.png")
                raise RuntimeError()
            elif len(html) < 1024 * 5:
                print('block 2...',len(html))
                raise RuntimeError()

            # index = random.randint(0, 15)
            # user_agent = user_agents[index]
            # head = {'User-Agent': user_agent}
            # req = request.Request(url_root, headers=head)
            # response = urllib.request.urlopen(req)
            # html = response.read().decode('utf-8')
            break
        except Exception as e:
            print('time exceeded', int1,e)
            try:
                os.system('rm -rf /tmp/.com.google.Chrome*')
                os.system('rm -rf /tmp/.org.chromium*')
                os.system('pkill -9 chrome')
                os.system('pkill -9 Xvfb')
                os.system('pkill -9 chromedriver')
                os.system('pkill -9 geckodriver')
                print('sleep...')
                time.sleep(60 * 10)
                print('starting')
                display = Display(visible=0, size=(800, 800))
                display.start()
                #driver = webdriver.Firefox()
                driver = webdriver.Chrome()
                driver.delete_all_cookies()
                print('started')
            except Exception as e:
                print('!', e)
    return html


# # 解决有些页面是大目录，需要再进入每个小目录爬去。调用过程类似递归。
# def anotherType(goodsUrl2, category, categoryCode):
#     for line in range(len(goodsUrl2)):
#         flag = line
#         str_url = r'href="(.*?)"'
#         url_sub = re.findall(str_url, goodsUrl2[line])
#         everyPage(url_sub[0], category, categoryCode, flag)


# 该函数用来偏离该类目的每一页目录
def everyPage(url_root, category, categoryCode, flag):
    beg = 0
    global saveFlag


    # 读取当前进度
    if saveFlag and os.path.exists('save.ech.csv'):
        load3 = pd.read_csv('save.ech.csv', header=None, encoding='utf-8', sep=' ')
        url_root = load3.iat[0, 1]
        beg = int(load3.iat[0, 2])
        saveFlag = False

    # 循环每页，当下一页不能点击时，跳出函数，爬下一类
    for pages in range(beg, 1000):
        html = gethtml1(url_root)
        if html == None:
            break
        # anotherDetail = r'<ul class="sc-thirdlevel-ul(.*?)<span class="sc-text">'
        # goodsUrl2 = re.findall(anotherDetail, str(html), re.S | re.M)
        # anotherDetail2 = r'<div class="sc-c-div-per">(.*?)<div'
        # goodsUrl3= re.findall(anotherDetail2, str(html), re.S | re.M)
        # 判断是否为大目录类型的网页
        # if len(goodsUrl2) != 0:
        #     anotherType(goodsUrl2, category, categoryCode)
        #     return 0
        # # 判断是否为大目录第二种类型的网页
        # elif len(goodsUrl3) != 0:
        #     anotherType(goodsUrl3, category, categoryCode)
        #     return 0

        else:
            if pages != 0:
                str_mainpage = r'<div id="resultsCol" class=(.*?)<div id="search-js-btr'
                try:
                    mainpage = re.findall(str_mainpage, str(html), re.S | re.M)
                    html1 = mainpage[0]
                except IndexError:
                    print('error empty:', mainpage, '***********************')
                    html1 = html
                    print(html1)
            else:
                html1 = html


            detail = r'<div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" target="_blank" href="(.*?)"><span class="a-size-small a-color-secondary">'
            goodsUrl = re.findall(detail, str(html1), re.S | re.M)
            # 手机配件大目录： #<div class="FourthHeader">  <a href=" target="_blank">  </a> </div>
            # 手机配件里 # class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"

            print('Sum:', len(goodsUrl))

            # 保存页面文件
            if flag < 0:
                filename = "urls/" + str(categoryCode) + '.txt'
            # else:
            #     filename = "urls/" + str(categoryCode) + '_' + str(flag) + '.txt'

            output = codecs.open(filename, "a+", encoding='utf-8')

            # 得到商品网址
            for line in range(len(goodsUrl)):

                if str(goodsUrl[line]).find('/gp/') != -1:
                    goodsUrlFin = 'https://www.amazon.cn' + str(goodsUrl[line])
                else:
                    goodsUrlFin = str(goodsUrl[line])

                print(pages, line, goodsUrlFin)
                output.write(goodsUrlFin + '\n')

            output.close()


            # 获取下一页网址，若没有，跳出
            nextpage = r'<span class="pagnRA">(.*?)</a></span>'
            nextpageInformation = re.findall(nextpage, str(html), re.S | re.M)
            if len(nextpageInformation) == 0:
                return 0
            nextInformation = re.findall('href="(.*?)"', nextpageInformation[0], re.S | re.M)

            # 同上，正则去除亚马逊防爬虫策略
            re_number = re.compile('/\d{3}-\d{7}-\d{7}')
            s = re_number.sub('', str(nextInformation[0]))
            url_root = 'https://www.amazon.cn' + str(s).replace('amp;', '')

            save = codecs.open('save.ech.csv', "w", encoding='utf-8')
            save.write(str(category) + ' ' + str(url_root) + ' ' + str(pages+1))

            continue
            # kill掉无用进程，防止内存爆炸
            int1 = 0
            while int1 < 20:
                try:
                    # time.sleep(random.randint(3, 5))
                    os.system('pkill -9 chrome')
                    os.system('pkill -9 Xvfb')
                    break
                except RuntimeError:
                    print('time exceeded3', int1)
                    int1 = int1 + 1
                    continue


def SearchAmazon():
    # 读取配置文件（类别的网址）
    file = pd.read_csv('ech.csv', header=None, encoding='gbk', sep=',')

    global saveFlag
    num = 0

    # 读取存档文件，判断从那个类别开始继续爬
    if os.path.exists('save.ech.csv'):
        load2 = pd.read_csv('save.ech.csv', header=None, encoding='utf-8', sep=' ')
        num = int(load2.iat[0, 0])

    # 循环所有的类别
    for category in range(num, file.shape[0]):
        categoryCode = file.iat[category, 1]
        url_root = file.iat[category, 2]
        flag = -1
        everyPage(url_root, category, categoryCode, flag)


if __name__ == '__main__':
    SearchAmazon()

