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

saveFlag = True


os.system('pkill -9 chrome')
os.system('pkill -9 Xvfb')
os.system('pkill -9 chromedriver')



# 模拟chrome，并消除浏览器图像化，以便在服务器里运行
display = Display(visible=0, size=(800, 800))
display.start()
driver = webdriver.Chrome()
#driver = webdriver.Firefox()


_root1 = []
_root2 = []
_root3 = []

# 计时用的函数
def timed_out(b, c):
    print('alarmed')
    raise RuntimeError()

def read_config():
    i1 = 0
    j1 = 0
    k1 = 0
    h1 = 0
    if os.path.exists('save_html.csv'):
        load2 = pd.read_csv('save_html.csv', header=None, encoding='utf-8', sep=',')
        i1 = int(load2.iat[0, 0])
        j1 = int(load2.iat[0, 1])
        k1 = int(load2.iat[0, 2])
        h1 = int(load2.iat[0, 3])
    return i1,j1,k1,h1


def write_config(i,j,k,h):
    save = codecs.open('save_html.csv', "w+", encoding='utf-8')
    save.write(str(i) + ',' +str(j) + ',' + str(k) + ',' + str(h))
    save.close()


# 获取商品页面内容,返回页面html
def gethtml2(goodsUrl):
    global driver
    int1 = 0
    while int1 < 100:

        # 配合计时函数，开一个信号来计算时间，超时便报错，然后except重新再爬这个网址。要是200次都报错就跳过该网址
        # （有时候因为网络或者模拟浏览器的问题，程序会卡住但不会报错跳出，用这个方法识别超时，手动报出错，catch错误后重新爬）
        #signal.signal(signal.SIGALRM, timed_out)
        #signal.setitimer(signal.ITIMER_REAL, 10, 0)

        try:
            int1 = int1 + 1

            driver.get(goodsUrl)

            print(driver.current_url)

            content = driver.page_source.encode('utf-8', 'ignore').decode()
            break
        except :
            print('time exceeded2', int1)
            try:
                #driver.quit()
                #display.stop()
                os.system('rm -rf /tmp/.com.google.Chrome*')
                os.system('rm -rf /tmp/.org.chromium*')
                os.system('pkill -9 chrome')
                os.system('pkill -9 Xvfb')
                os.system('pkill -9 chromedriver')
                time.sleep(random.randint(1, 3))
                display = Display(visible=0, size=(800, 800))
                display.start()
                driver = webdriver.Chrome()
            except:
                print("except raise")
    return content

#
def goods(i,j,k,h1,filename):
    print("go "+ filename)
    list1 = linecache.getlines(filename)
    print('URLs number:',str(len(list1)))
    # 需要的话，读取进度，读取一次后，saveFlag变成false，本次运行再也不会读取
    num = 0
    global saveFlag
    if saveFlag == True:
        num = h1
        saveFlag = False
    # 遍历页面下的每个商品
    for times in range(num,len(list1)):

        global _root1,_root2,_root3
        #path = str(i) + '_' + str(j)+ '_' + str(k) + '/'
        path = _root1[i] + '_' + _root2[j]+ '_' + _root3[k].replace('.txt','') + '/'
        print('level: ', _root1[i],_root2[j],_root3[k],times)
        if os.path.exists(path) == False:
            os.mkdir(path)

        if os.path.exists(path + str(times) + '.txt') == False:
            content = gethtml2(list1[times])
            # 保存页面文件
            output = codecs.open(path + str(times) + '.txt', "w+", encoding='utf-8')
            output.write(str(content))
            output.close()

        #保存当前爬虫进度
        write_config(i,j,k,times)

        if times > 100:
            break
        continue

        int1 = 0
        # 间隔1—3秒再爬取下个循环，同时kill一些中间调用的进程，减少内存压力
        while int1 < 20:
            try:
                # time.sleep(random.randint(1, 3))
                os.system('pkill -9 chrome')
                os.system('pkill -9 Xvfb')
                break
            except RuntimeError:
                print('time exceeded3', int1)
                int1 = int1 + 1
                continue


if __name__ == '__main__':
    # 读取路径下的文件(.txt)个数,并排序
    path1 ='.'
    _root1 = os.listdir(path1)
    
    tmp = []
    for p in _root1:
        path = path1 + '/' + p
        if os.path.isdir(path) and p.rfind('_') == -1:
            tmp.append(p)
    _root1 = tmp
    _root1.sort()

    i1 = 0
    j1 = 0
    k1 = 0
    h1 = 0
    # 读取存档
    i1,j1,k1,h1 = read_config()

    print("dir number is "+str(len(_root1)))
    # 循环遍历两层文件夹，最后遍历第三层的txt文件，并调用goods()获取页面
    for i in range(i1, len(_root1)):
        path2 = path1 + '/' +str(_root1[i])
        print("go "+path2)
        _root2 = os.listdir(path2)
        _root2.sort()
        for j in range(j1, len(_root2)):
            path3 = path2 + '/' + str(_root2[j])
            _root3 = os.listdir(path3)
            print("go "+path3)
            _root3.sort()
            for k in range(k1, len(_root3)):
                goods(i,j,k,h1,path3 +"/"+ str(_root3[k]))
