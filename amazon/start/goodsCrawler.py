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
import linecache


import sys, os

display = Display(visible=0, size=(800, 800))
display.start()
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

global saveFlag
saveFlag = True

# 计时用的函数
# def timed_out(b, c):
#     print('alarmed')
#     raise RuntimeError()
#
# def child_exit(b,c):
#     ret = os.wait()
#     print('child exiting',ret)


# def read_config():
#     num1 = 0
#     num2 = 0
#     if os.path.exists('save_goods.csv'):
#         load2 = pd.read_csv('save_goods.csv', header=None, encoding='utf-8', sep=',')
#         num1 = load2.iat[0, 0]
#         num2 = load2.iat[0, 1]
#     return num1,num2

def write_config(number,times):
    save = codecs.open('save_goods.csv', "w+", encoding='utf-8')
    save.write(str(number) + ',' + str(times))
    save.close()

# 获取商品页面内容，返回页面html
def gethtml2(goodsUrl):
    global driver
    global display
    try_times = 0
    content= ''
    while try_times < 100:

        # 配合计时函数，开一个信号来计算时间，超时便报错，然后except重新再爬这个网址。要是200次都报错就跳过该网址
        # （有时候因为网络或者模拟浏览器的问题，程序会卡住但不会报错跳出，用这个方法识别超时，手动报出错，catch错误后重新爬）
        #signal.signal(signal.SIGALRM, timed_out)
        #signal.setitimer(signal.ITIMER_REAL, 10, 0)

        try:

            # 模拟chrome，并消除浏览器图像化，以便在服务器里运行

            try_times = try_times + 1

            # 正则去除连接上的反爬虫部分
            re_url = re.compile('/\d{3}-\d{7}-\d{7}')
            url = re_url.sub('', goodsUrl).replace('amp;', '').replace('&th=1', '')
            driver.get(url)

            print(driver.current_url)

            content = driver.page_source.encode('utf-8', 'ignore').decode()
            if content.find('您输入的网址在我们的网站上无法正常显示网页')!= -1:
                print('good is missing')
                content=""
            elif content.find('当前访问者并非自动程序') != -1:
                print('block 1...')
                f= open('/tmp/aa','w')
                f.write(content)
                f.close()
                driver.get_screenshot_as_file("/tmp/aa.png")
                raise RuntimeError()
            elif len(content) < 1024 * 5:
                print('block 2...',len(content))
                raise RuntimeError()
            break
        except Exception as e:
            print(try_times,e)
            try:

                #driver.quit()
                #display.stop()
                print('kill all')
                os.system('pkill -9 chrome')
                os.system('pkill -9 Xvfb')
                os.system('pkill -9 chromedriver')
                #os.system('pkill -9 geckodriver')
                os.system('rm -rf /tmp/.com.google.Chrome*')
                os.system('rm -rf /tmp/.org.chromium*')
                print('sleep...')
                time.sleep(60*10)
                print('starting')
                #time.sleep(random.randint(1, 3))
                display = Display(visible=0, size=(800, 800))
                display.start()
                driver = webdriver.Chrome()
                driver.delete_all_cookies()
                print('started')
            except Exception as e:
                print('!',e)
    return content

# 压缩html代码，去除脚本和header
def compress(html):
    dr = re.compile(r'<script(.*?)</script>', re.S | re.M)     #head头
    Info = dr.sub('', str(html))
    dr3 = re.compile(r'<style(.*?)</style>', re.S | re.M)    #修饰
    Info2 = dr3.sub('', Info)
    dr2 = re.compile(r'<noscript>(.*?)</noscript>', re.S | re.M)   #未执行的替代文本
    Info3 = dr2.sub('', Info2)
    categoryRanke = re.findall('<div class="nav-search-facade" data-value="search-alias=aps">(.*?)</div>', Info3, re.S | re.M)    #总归属  eg 服饰箱包
    dr4 = re.compile(r'<header class=(.*?)</header>', re.S | re.M)
    Info4 = dr4.sub('', Info3)
    if len(categoryRanke) == 0:
        categoryRanke = [1]
        categoryRanke[0] = ''
    txt = (categoryRanke[0] + Info4).replace('\n','').replace('  ','')
    return txt

def check_file_is_normal(f):
    if os.path.exists(f) == False:
        return False
    if os.path.getsize(f) == 0:
        return False
    return True

def goods(number, num2,filename):   #filename 是一个txt 文件名
    # 注意路径
    list = linecache.getlines(filename)    #linecache.getlines  把文件内每行变成列表中的元素

    # 需要的话，读取进度，读取一次后，saveFlag变成false，本次运行再也不会读取   ？？？？？？
    global saveFlag
    num = 0
    if saveFlag == True:
        num = num2
        saveFlag = False

    # 遍历页面下的每个商品
    for times in range(num, len(list)):
        print('category code: ', str(filename).replace('.txt',''))
        print('number:', times)


        path = 'contents/' + str(filename).replace('.txt','') + '/'

        if os.path.exists(path) == False:
            os.mkdir(path)

        if check_file_is_normal(path + str(times) + '.txt') == False:
            content = gethtml2(list[times])
            allType = re.findall('<a class="a-link-normal" href="(.*?)">查看所有商品描述</a>', content, re.S | re.M)

            # 有些商品页面信息不全，会有一个‘详细信息’的页面，这时会用详细信息的页面替代原来获取的商品页面
            if len(allType) != 0:
                content = gethtml2('https://www.amazon.cn' + allType[0])
            # 保存页面文件
            output = codecs.open(path + str(times) + '.txt', "w+", encoding='utf-8')
            output.write(str(compress(content)))
            output.close()

        #保存当前爬虫进度
        write_config(number,times)


        if times > 220000:
            break


if __name__ == '__main__':

    print('starting...')
    # signal.signal(signal.SIGCLD,signal.SIG_IGN)
    #signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    #signal.signal(signal.SIGCHLD, child_exit)
    num = 0
    num2 = 0
    #num,num2 = read_config()

    # 读取路径下的文件(.txt)个数,并排序
    filenames = os.listdir('./')    #返回文件夹内文件名或文件夹名的列表

    tmp = []
    for f in filenames:
        if f.endswith(".txt"):    #Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
            tmp.append(f)
    filenames = tmp

    filenames.sort()
    #filenames.sort(key=lambda x: int(x[:-4]))
    for i in range(num,len(filenames)):
        goods(num,num2,filenames[i])

    print('done')


