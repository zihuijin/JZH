#coding:utf-8
import re
content = '000-111-333'
# m = re.match('\d{2}',content)
# print(m.group())
# s = re.search('\d{3}',content)
# print(s.group())
# su = re.sub('\d-','ii',content)
# print(su)
# fa = re.findall('(\d+)-',content)
# for i in fa:
#     print(i)
# 000
# 111


#1. re.match函数
#re.match(pattern, string, flags=0)       #re.match(在起始位置匹配),如果没有则返回None
#我们可以使用group(num=0) 或 groups() 匹配对象函数来获取匹配表达式。
#group（）相当于group（0），是返回所有匹配字符
# group（1）是返回第一个括号里(1组)的内容
# group（2）是返回第二个括号内(2组)的内容
# groups(),以元组形式返回所有组内容
line = "Cats are smarter than dogs"

searchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("searchObj.groups() : ", searchObj.groups())
else:
    print("Nothing found!!")

# searchObj.group() :  Cats are smarter than dogs
# searchObj.group(1) :  Cats
# searchObj.group(2) :  smarter
# searchObj.groups() :  ('Cats', 'smarter')

#2. re.search(pattern, string, flags=0)    #re.search()返回第一个匹配对象,否则返回None。
# if re.search('',''):
#     pass

#我们可以使用group(num=0) 或 groups() 匹配对象函数来获取匹配表达式。

# line = "Cats are smarter than dogs"
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print("Nothing found!!")


#3. re.sub(pattern, repl, string, count=0, flags=0)   #替换匹配到的字符串
# 参数：
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# t=re.sub('\d{3}','555',content)
# print(t)

#4. 正则表达式模式
#由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。
# 模式元素(如 r'\t'，等价于 '\\t')匹配相应的特殊字符。
#下表列出了正则表达式模式语法中的特殊元素。----在r' ' 下都不是转义字符
# ^ 匹配字符串开头，$匹配字符串结尾
# . 匹配除\n以外的所有字符
# [abc] 表示多选一
# [^abc]  表示除这些字符的所有字符
# a*      匹配0个或多个
# a+      匹配一个以上
# a?      匹配0个或一个、
# a{n}    匹配n个
# a{n,m}  匹配n到m个
# a|b     匹配a或b
# （re）   匹配括号内的表达式，也表示一个组
# \w      匹配数字字母下划线（名字）
# \W      匹配除了数字字母下滑线
# \s      匹配任意空白字符（\t,\n,\r,\f）
# \S      匹配除任意空白字符
# \d      匹配数字[0-9]
# \D      匹配非数字
# \A      匹配字符串开始
# \Z      匹配字符串结束

#5.  re.compile('\d{3}-\d{3}-\d{3}')  #compile生成正则表达式对象
# eg:
# r = re.compile('\d{3}-\d{3}-\d{3}')
# t= r.search(content).group()
# print(t)   #000-111-333

#6. 匹配格式
#re.M|re.I??????
# re.M    多行匹配，影响^与$
# re.I    忽略大小写
# re.S    使.匹配包括/n的所有字符

#7. findall(pattern,str)   --- 以列表形式返回所有匹配对象
#(1)如果正则表达式不带括号，则列表元素为字符串，字符串是整个正则表达式内容
# fa = re.findall('\d+-',content)
# for i in fa:
#     print(i)
# 000-
# 111-

#(2)如果正则表达式带一个括号，则列表元素为字符串，字符串是括号里匹配内容
# fa = re.findall('(\d+)-',content)
# for i in fa:
#     print(i)
# 000
# 111
#(3) 如果正则表达式带多个括号，则列表元素为多个字符串组成的元组，字符串顺序，个数与括号相对应
# fa = re.findall('(\d+)-(.*?)-',content)
# for i in fa:
#     print(i)
# ('000', '111')


