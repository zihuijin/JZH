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
import urllib
from PIL import Image
import math
import os



#def
# 夹角公式
class VectorCompare:
    # 计算矢量大小
    # 计算平方和
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量之间的 cos 值
    def relation(self, concordance1, concordance2):
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                # 计算相乘的和
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


# 将图片转换为矢量
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


def main(item):
    try:
        newjpgname = []
        im = Image.open(item)
        # jpg不是最低像素，gif才是，所以要转换像素
        im = im.convert("P")

        # 像素直方图
        his = im.histogram()

        values = {}
        for i in range(0, 256):
            values[i] = his[i]

        # 排序，x:x[1]是按照括号内第二个字段进行排序,x:x[0]是按照第一个字段
        # temp = sorted(values.items(), key=lambda x: x[1], reverse=True)

        # 占比最多的10种颜色
        # for j, k in temp[:10]:
        #     print(j, k)
        # 255 12177
        # 0 772
        # 254 94
        # 1 40
        # 245 10
        # 12 9
        # 236 9
        # 243 9
        # 2 8
        # 6 8
        # 255是白底，0是黑色，可以打印来看看0和254

        # 获取图片大小，生成一张白底255的图片________________________黑白处理
        im2 = Image.new("P", im.size, 255)
        for y in range(im.size[1]):
            # 获得y坐标
            for x in range(im.size[0]):

                # 获得坐标(x,y)的RGB值
                pix = im.getpixel((x, y))

                # 这些是要得到的数字
                # 事实证明只要0就行，254是斑点
                if pix == 0:
                    # 将黑色0填充到im2中
                    im2.putpixel((x, y), 0)
        # 生成了一张黑白二值照片---------------------------------------------------------
        # im2.show()

        # 纵向切割---------------------------------------------------------------
        # 找到切割的起始和结束的横坐标
        inletter = False
        foundletter = False
        start = 0
        end = 0

        letters = []

        for x in range(im2.size[0]):
            for y in range(im2.size[1]):
                pix = im2.getpixel((x, y))
                if pix != 255:
                    inletter = True
            if foundletter == False and inletter == True:
                foundletter = True
                start = x

            if foundletter == True and inletter == False:
                foundletter = False
                end = x
                letters.append((start, end))

            inletter = False
        # print(letters)
        # [(27, 47), (48, 71), (73, 101), (102, 120), (122, 147), (148, 166)]
        # 打印出6个点，说明能切割成6个字母，正确

        for letter in letters:
            # (切割的起始横坐标，起始纵坐标，切割的宽度，切割的高度)
            im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))



            # ____________________________________________________________________________________

        # 加载训练集-----------------------用相似度找到最合适的字母
        v = VectorCompare()

        # 开始破解训练
        count = 0
        for letter in letters:
            # (切割的起始横坐标，起始纵坐标，切割的宽度，切割的高度)
            im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))

            guess = []
            # 将切割得到的验证码小片段与每个训练片段进行比较
            for image in imageset:
                for x, y in image.items():
                    if len(y) != 0:
                        guess.append((v.relation(y[0], buildvector(im3)), x))

            # 排序选出夹角最小的（即cos值最大）的向量，夹角越小则越接近重合，匹配越接近
            guess.sort(reverse=True)
            newjpgname.append(guess[0][1])
            count += 1

        # 得到拼接后的验证码识别图像
        newname = str("".join(newjpgname))  # --------------------------------------

        # 向框输入newname    ???????????????
        print (newname)
        return (newname)
    except Exception as err:
        print('identifying code error --------------')
        print(err)
        # 如果错误就记录下来



        # 开启多进程
        # def runthreading():
        #     pool = ThreadPoolExecutor(5)
        # jpgname = listfiles(path, "jpg")         #传入图片，生成路径列表
        # for item in jpgname:
        #     # 识别过的就不再识别了
        #     if len(item)>30:
        #         pool.submit(main, item)



display = Display(visible=0, size=(800, 800))
display.start()
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
# 用来读取已保存进度的全局变量。
global saveFlag
saveFlag = True


# yanzheng 全局变量

# iconset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#que   d,i,o,q,s,v,w,z
iconset = ['a','b','c','e','f','g','h','j','k','l','m','n','p','r','t','u','x','y']


imageset = []
for letter in iconset:
    for img in os.listdir('iconset1/%s/' % (letter)):
        temp = []
        if img != "":
            temp.append(buildvector(Image.open("iconset1/%s/%s" % (letter, img))))
        imageset.append({letter: temp})

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
            elif len(html) < 1024 * 5:
                print('block 2...',len(html))
                raise RuntimeError()
            else:
                while(html.find('抱歉，我们只是想确认一下当前访问者并非自动程序')) != -1:
                    print('block 1...')
                    f= open('tmp/fp.txt','w')
                    f.write(html)
                    f.close()

                    #找正则表达式
                    pi = r'<img src="(.*?)" />'
                    pi_url = re.findall(pi, str(html), re.S | re.M)     #findall下是一个列表
                    #获取图片
                    if len(pi_url) > 0:
                        data = urllib.request.urlopen(pi_url[0]).read()
                        address = 'pi/pi.jpg'
                        w = open(address, 'wb')
                        w.write(data)
                        w.close()

                        de  = main(address)
                    else:
                        print('pi_url is null')
                    #输入验证码
                    driver.find_element_by_id("captchacharacters").send_keys(str(de))
                    # driver.find_element_by_name("继续购物").click()
                    driver.find_element_by_class_name('a-button-text').click()
                    time.sleep(0.5)

                    driver.get(driver.current_url.replace('amp;', '').replace('&th=1', ''))

                    # 打印当前网址
                    print(driver.current_url)
                    html = driver.page_source.encode('utf-8', 'ignore').decode()

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
                time.sleep(random.randint(1,3))
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
    if saveFlag and os.path.exists('save.hd.csv'):
        load3 = pd.read_csv('save.hd.csv', header=None, encoding='utf-8', sep=' ')
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
                # detail = r'<div class="a-row a-spacing-none"><a class="a-link-normal a-text-normal" target="_blank" href="(.*?)">'


            detail0 = r'<div class="a-row a-spacing-none"><a class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal" target="_blank" title=(.*?)><'
            goodsUrl0 = re.findall(detail0, str(html1))
            # if len(goodsUrl0)==0:
            # detail0 = r'<div class="a-row a-spacing-mini"><a class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal" target="_blank" title=(.*?)>'
            # goodsUrl0 = re.findall(detail0, str(html1))
            if len(goodsUrl0) == 0:
                print('type1 is null')
                detail0 = r'<div class="a-row a-spacing-mini"><a class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal" target="_blank" title=(.*?)>'
                goodsUrl0 = re.findall(detail0, str(html1))

            if len(goodsUrl0) == 0:
                print('type2 is null')
                detail0 = r'<a data-asin=(.*?)>'
                # <a data-asin=(.*?)><
                goodsUrl0 = re.findall(detail0, str(html1))
            if len(goodsUrl0) == 0:
                print('type2 is null')

            detail = r'href="(.*?)"'
            goodsUrl = re.findall(detail, str(''.join(goodsUrl0)), re.S | re.M)

            # 手机配件大目录： #<div class="FourthHeader">  <a href=" target="_blank">  </a> </div>
            # 手机配件里 # class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"

            print('Sum:', len(goodsUrl))


            # 保存页面文件
            if flag < 0:
                filename = "urls1/" + str(categoryCode) + '.txt'
            # else:
            #     filename = "urls/" + str(categoryCode) + '_' + str(flag) + '.txt'

            output = codecs.open(filename, "a+", encoding='utf-8')

            # 得到商品网址
            for line in range(len(goodsUrl)):

                if str(goodsUrl[line]).find('/gp/') != -1:
                    goodsUrlFin = 'https://www.amazon.cn' + str(goodsUrl[line]).replace('amp;', '')
                else:
                    goodsUrlFin = str(goodsUrl[line]).replace('amp;', '')

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

            save = codecs.open('save.hd.csv', "w", encoding='utf-8')
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
    file = pd.read_csv('hd.csv', header=None, encoding='gbk', sep=',')

    global saveFlag
    num = 0

    # 读取存档文件，判断从那个类别开始继续爬
    if os.path.exists('save.hd.csv'):
        load2 = pd.read_csv('save.hd.csv', header=None, encoding='utf-8', sep=' ')
        num = int(load2.iat[0, 0])

    # 循环所有的类别
    for category in range(num, file.shape[0]):
        categoryCode = file.iat[category, 1]
        url_root = file.iat[category, 2]
        flag = -1
        everyPage(url_root, category, categoryCode, flag)


if __name__ == '__main__':
    SearchAmazon()

