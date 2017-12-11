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
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Firefox(executable_path = '/home/samsung/bin/geckodriver')
# 用来读取已保存进度的全局变量。
global saveFlag
saveFlag = True

# 计时用的函数
def timed_out(b, c):
    print('alarmed')
    raise RuntimeError()

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



            # 引入配置对象DesiredCapabilities
            from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            # 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
            user_agents = [
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
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
                "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52" ]
            dcap["phantomjs.page.settings.userAgent"] = (random.choice(user_agents))
            # 不载入图片，爬页面速度会快很多
            dcap["phantomjs.page.settings.loadImages"] = False
            # 设置代理????????
            service_args = ['--proxy=127.0.0.1:9999', '--proxy-type=socks5']
            # 打开带配置信息的
            driver = webdriver.Chrome(desired_capabilities=dcap, service_args=service_args)
            driver.get(url_root.replace('amp;', '').replace('&th=1', ''))
            # driver = webdriver.PhantomJS(phantomjs_driver_path, desired_capabilities=dcap, service_args=service_args)
            # 隐式等待5秒，可以自己调节
            # driver.implicitly_wait(5)
            # # 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
            # # 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
            # driver.set_page_load_timeout(10)
            # # 设置10秒脚本超时时间
            # driver.set_script_timeout(10)


            # options = webdriver.ChromeOptions()********************************************************
            # # 设置中文
            # options.add_argument('lang=zh_CN.UTF-8')
            # #设置请求头

            # index = random.randint(0, 15)
            # user_agent = user_agents[index]
            # user_agent1 = 'user-agent='+ str(user_agent)
            #
            # # 更换头部
            # options.add_argument(user_agent1)
            #
            # #————————————————————————
            # # options.add_argument(
            # #     'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
            #
            # # def get_content(pagesUrl):
            # #     content = ""
            # #     try:
            # #         index = random.randint(0, 15)
            # #         user_agent = user_agents[index]
            # #         head = {'User-Agent': user_agent}
            # #         proxy = {'http': 'http://109.105.1.52:8080', 'https': 'http://109.105.1.52:8080',
            # #                  'User-Agent': user_agent}
            # #         req = urllib2.Request(pagesUrl, headers=head)
            # #         response = urllib2.urlopen(req, timeout=3)
            # #         content = response.read().decode('utf-8')
            # #     except Exception as e:
            # #         print ("error:", e.message)
            # #
            # #     return content
            # #————————————————————————
            #
            #
            #
            #
            # driver = webdriver.Chrome(chrome_options=options)**************************************




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
                # os.system('pkill -9 geckodriver')
                print('sleep...')
                time.sleep(60 * 10)
                print('starting')
                display = Display(visible=0, size=(800, 800))
                display.start()
                #driver = webdriver.Firefox()
                driver = webdriver.chrome()
                driver.delete_all_cookies()
                print('started')
            except Exception as e:
                print('!', e)
    return html


# 解决有些页面是大目录，需要再进入每个小目录爬去。调用过程类似递归。
def anotherType(goodsUrl2, category, categoryCode):
    for line in range(len(goodsUrl2)):
        flag = line
        str_url = r'href="(.*?)"'
        url_sub = re.findall(str_url, goodsUrl2[line])
        everyPage(url_sub[0], category, categoryCode, flag)


# 该函数用来偏离该类目的每一页目录
def everyPage(url_root, category, categoryCode, flag):
    beg = 0
    global saveFlag

    # 读取当前进度
    if saveFlag and os.path.exists('save.esa.csv'):
        load3 = pd.read_csv('save.esa.csv', header=None, encoding='utf-8', sep=' ')
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
            str_mainpage = r'<div id="resultsCol" class=(.*?)<div id="search-js-btr'
            try:
                mainpage = re.findall(str_mainpage, str(html), re.S | re.M)
                html1 = mainpage[0]
            except IndexError:
                print('error empty:', mainpage, '***********************')
                print(html1)
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

            save = codecs.open('save.esa.csv', "w", encoding='utf-8')
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
    file = pd.read_csv('esa.csv', header=None, encoding='gbk', sep=',')

    global saveFlag
    num = 0

    # 读取存档文件，判断从那个类别开始继续爬
    if os.path.exists('save.esa.csv'):
        load2 = pd.read_csv('save.esa.csv', header=None, encoding='utf-8', sep=' ')
        num = int(load2.iat[0, 0])

    # 循环所有的类别
    for category in range(num, file.shape[0]):
        categoryCode = file.iat[category, 1]
        url_root = file.iat[category, 2]
        flag = -1
        everyPage(url_root, category, categoryCode, flag)


if __name__ == '__main__':
    SearchAmazon()

