#coding:utf-8
import requests

#1. get 请求   :得到东西
# 在URLs中传递参数(params)
#有时候我们需要在URL中传递参数，比如在采集百度搜索结果时，我们wd参数（搜索词）和rn参数（搜素结果数量），你可以手工组成URL，requests也提供了一种看起来很NB的方法：
# params = {'wd': '张亚楠', 'rn': '100'}
# r =requests.get(url = 'http://www.baidu.com',params=params,timeout= 10)    #requests.get()返回response对象,其存储了服务器响应的内容，如上实例中已经提到的 r.text、r.status_code……
# print(r.url)     #返回当前网页
# u'http://www.baidu.com/s?rn=100&wd=%E5%BC%A0%E4%BA%9A%E6%A5%A0'
# 上面wd=的乱码就是“张亚楠”的转码形式。（好像参数按照首字母进行了排序。）

# print(r.text)     #获取文本方式的响应体实例：当你访问 r.text 之时，会使用其响应的文本编码进行解码，并且你可以修改其编码让 r.text 使用自定义的编码进行解码。
# (1)r.encoding = 'GBK'
# print(r.text)
# (2) print(r.text, '\n{}\n'.format('*'*79), r.encoding)


#设置超时时间,我们可以通过timeout属性设置超时时间，一旦超过这个时间还没获得响应内容，就会提示错误。
# >>> requests.get('http://github.com', timeout=0.001)
# requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)


# r= requests.get('https://www.qiushibaike.com/imgrank/')
# print(r.url,r.status_code)
# print(r.headers)
# print(r.content)
# print(r.text)
# print(r.json)
# print(r.cookies)


# r响应的内容还包括
# r.status_code #响应状态码
# >>>r = requests.get('http://www.mengtiankong.com/123123/')
# >>>r.status_code
# 404  #能正常打开的返回200，不能正常打开的返回404。

# r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
# r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码

# r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# >>>r = requests.get('http://www.zhidaow.com')
# >>> r.headers
# {
#     'content-encoding': 'gzip',
#     'transfer-encoding': 'chunked',
#     'content-type': 'text/html; charset=utf-8';
#     ...
# }
#也可以直接访问
# >>> r.headers['Content-Type']      #r.headers.get('content-type')
# 'text/html; charset=utf-8'

# #*特殊方法*#
# r.json() #Requests中内置的JSON解码器      #需要先import json
#>>>r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
# >>>r.json()['data']['country']
# '中国'

# r.raise_for_status() #失败请求(非200响应)抛出异常

# 可以用print(r.encoding)来获取网页编码,r.text在requests默认用网页编码来编码，
# 我们可以修改requests编码格式 r.encoding = 'gbk'

#print(r.cookies['NID'])
# print(tuple(r.cookies)) #如果某个响应中包含一些Cookie，你可以快速访问它们

# 代理访问
#采集时为避免被封IP，经常会使用代理。requests也有相应的proxies属性。
# import requests
#
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "http://10.10.1.10:1080",
# }

# requests.get("http://www.zhidaow.com", proxies=proxies)

# 如果代理需要账户和密码，则需这样：
# proxies = {
#     "http": "http://user:pass@10.10.1.10:3128/",
# }



# 2. post请求  :   传递东西（data）

# data = {}
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
# r=requests.post(url = '',data = data,headers=headers)

#3. eg
# url = 'http://ip.taobao.com/service/getIpInfo.php'   # 淘宝IP地址库API
# try:
#     r = requests.get(url,params = {'ip':'8.8.8.8'},timeout = 1)
#     r.raise_for_status() # 如果响应状态码不是 200，就主动抛出异常
# except requests.RequestException as e:
#     print(e)
# else:
#     result = r.json()
#     print(type(result),result,sep = '\n')

# {'code': 0, 'data': {'isp_id': '3000519', 'country': '内网IP', 'region': '', : '-1', 'county_id': '-1', 'isp': '谷歌', 'region_id': '-1', 'city': '', 'citty': ''}}
















# #简单应用
# # HTTP请求类型
# # get类型
# r = requests.get('https://github.com/timeline.json')
# # post类型
# r = requests.post("http://m.ctrip.com/post")
# # put类型
# r = requests.put("http://m.ctrip.com/put")
# # delete类型
# r = requests.delete("http://m.ctrip.com/delete")
# # head类型
# r = requests.head("http://m.ctrip.com/head")
# # options类型
# r = requests.options("http://m.ctrip.com/get")
#
# # 获取响应内容
# print
# r.content  # 以字节的方式去显示，中文显示为字符
# print
# r.text  # 以文本的方式去显示
#
# # URL传递参数
# payload = {'keyword': '日本', 'salecityid': '2'}
# r = requests.get("http://m.ctrip.com/webapp/tourvisa/visa_list", params=payload)
# print
# r.url  # 示例为http://m.ctrip.com/webapp/tourvisa/visa_list?salecityid=2&keyword=日本
#
# # 获取/修改网页编码
# r = requests.get('https://github.com/timeline.json')
# print
# r.encoding
# r.encoding = 'utf-8'
#
# # json处理
# r = requests.get('https://github.com/timeline.json')
# print
# r.json()  # 需要先import json
#
# # 定制请求头
# url = 'http://m.ctrip.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
# r = requests.post(url, headers=headers)
# print
# r.request.headers
#
# # 复杂post请求
# url = 'http://m.ctrip.com'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))  # 如果传递的payload是string而不是dict，需要先调用dumps方法格式化一下
#
# # post多部分编码文件
# url = 'http://m.ctrip.com'
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
#
# # 响应状态码
# r = requests.get('http://m.ctrip.com')
# print
# r.status_code
#
# # 响应头
# r = requests.get('http://m.ctrip.com')
# print
# r.headers
# print
# r.headers['Content-Type']
# print
# r.headers.get('content-type')  # 访问响应头部分内容的两种方式
#
# # Cookies
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# r.cookies['example_cookie_name']  # 读取cookies
#
# url = 'http://m.ctrip.com/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)  # 发送cookies
#
# # 设置超时时间
# r = requests.get('http://m.ctrip.com', timeout=0.001)
#
# # 设置访问代理
# proxies = {
#     "http": "http://10.10.10.10:8888",
#     "https": "http://10.10.10.100:4444",
# }
# r = requests.get('http://m.ctrip.com', proxies=proxies)

