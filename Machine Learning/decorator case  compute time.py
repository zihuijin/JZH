# # -*- coding:utf8  -*-
#
# import re,time,random,os,datetime
# # import requests
# # import HTMLparser
# import sys
# # reload(sys)   #????
# # sys.getdefaultencoding('utf-8')
#
#
# # 计算时间函数
# def print_run_time(func):
#     def wrapper(*args,**kwargs):
#         local_time = time.time()
#         func(*args,**kwargs)
#         print('current Function [%s] run time is %.2f'%(func.__name__,local_time))
#     return wrapper
#
# class Test:
#     def __init__(self):
#         self.utl=''
#     #获取页面内容
#     #即装饰器不管参数多少都能使用
#     @print_run_time
#     def get_html(self,url):
#         headers = {} #设置网页头信息
#         req = requests.post(url=url,headers=headers)
#         return req.text
#
# #在类的内部使用装饰器
# @print_run_time
# def run(self):
#     self.url='http://www.baidu.com'
#     self.get_html(self.url)
#     print('end')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import urllib2, re, time, random, os, datetime
# # import HTMLParser
# # import sys
# #
# # reload(sys)
# # sys.setdefaultencoding('utf-8')
# #
# #
# # # 计算时间函数
# # def print_run_time(func):
# #     def wrapper(*args, **kw):
# #         local_time = time.time()
# #         func(*args, **kw)
# #         print('current Function [%s] run time is %.2f' % (func.__name__, time.time() - local_time))
# #
# #     return wrapper
# #
# #
# # class test:
# #     def __init__(self):
# #         self.url = ''
# #
# #     # 获取网页页面内容
# #     # 即装饰器不管参数有多少，都能使用
# #     @print_run_time
# #     def get_html(self, url):
# #         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}  # 设置header
# #         req = urllib2.Request(url=url, headers=headers)
# #         try:
# #             html = urllib2.urlopen(req).read().decode('utf-8')
# #             html = HTMLParser.HTMLParser().unescape(html)  # 处理网页内容， 可以将一些html类型的符号如" 转换回双引号
# #         # html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())#转码:避免输出出现乱码
# #         except urllib2.HTTPError, e:
# #             print(2, u"连接页面失败，错误原因： %s" % e.code)
# #             return None
# #         except urllib2.URLError, e:
# #             if hasattr(e, 'reason'):
# #                 print(2, u"连接页面失败，错误原因：%s" % e.reason)
# #                 return None
# #         return html
# #
# #     # 在类的内部使用装饰器
# #     @print_run_time
# #     def run(self):
# #         self.url = 'http://www.baidu.com'
# #         self.get_html(self.url)
# #         print('end')
# #
# #
# # # 在外面直接使用装饰器
# # @print_run_time
# # def get_current_dir(spath):
# #     # spath=os.getcwd()
# #     # spath=os.path.abspath(os.curdir)
# #
# #     for schild in os.listdir(spath):
# #         schildpath = spath + '/' + schild
# #         if os.path.isdir(schildpath):
# #             get_current_dir(schildpath)
# #         else:
# #             print(schildpath)
# #
# #
# # if __name__ == '__main__':
# #     my_test = test()
# #     my_test.run()
# #     spath = os.path.abspath('.')
# #     get_current_dir(spath)

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
import time
print('start:',time.ctime())
time.sleep(5)
print('end:',time.ctime())
