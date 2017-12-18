# coding:utf-8
import  pandas as pd
import numpy as np
from numpy import array
from pandas import DataFrame,Series


#series 是一个带标签的一维数组
#1创建:在创建函数中装序列
# s=Series([1,2,3,4])
#分别查询他的索引s.index 与值 s.vaules
# print(s,'\n\n',s.index,'\n\n',s.values)

#2.创建带索引的Series
# s= Series([1,2,3,4],index=['a','b','c','d'])
# c= Series([1,2,3,4],index=[2,5,7,8])

#3.查询，使用索引
# print(c[[2,5,8]])
#4.进行计算会保留索引与值的联系
# print(c*2,np.exp(c),c[c>2])

#5.可以将Series 看成定长的字典，可以用字典应用
# print(2 in c)
# c.set_value(label=1,value=3)
# print(c)

#6.可以通过字典创建
# d={'a':1,'b':2,'c':3}
# l=['a','c','d']
# c=Series(d,index=l)
# print(c)

#7 pandas 的isnull,notnull 可以检测缺失数据
# print(pd.isnull(c),'\n\n',pd.notnull(c))
#8.Series 的重要应用是他在算数运算中会对齐索引
# d={'a':1,'b':2,'c':3}
# e={'b':1,'c':2,'a':3}
# d=Series(d)
# e=Series(e)
# print(d+e)

#9.Series 对象本身及其索引都有一个name属性
# d.name = 'sss'
# d.index.name = 'ddd'
# print(d)

#10.Series 可以通过赋值的方式就地修改

# d.index=[1,2,3]
# print(d)

#pandas 简介
#是一种表格型的数据结构，含有有序的列，每列可以是不同值类型（数值，字符，布尔）
#既有行索引，也有列索引，是有二维块存放的
#1.DataFrame创建
#一般传入字典，由等长列表或数组组成
d = {'a':[1,2,3,4],
     'b':[5,6,7,8],
     'c':[9,0,1,2]
     }
# c = DataFrame(d,index=[5,6,7,8])
# print(c)
#列标签如果指定，列就会自动排列顺序   如果找不到就会产生空值
# c= DataFrame(d,columns=['b','c','a'])
# print(c)
#    b  c  a
# 0  5  9  1
# 1  6  0  2
# 2  7  1  3
# 3  8  2  4
c= DataFrame(d,columns=['a','b','c','d'],index=['v','b','n','m'])
# print(c)
#    a  b  c    d
# 0  1  5  9  NaN
# 1  2  6  0  NaN
# 2  3  7  1  NaN
# 3  4  8  2  NaN
#查找列索引
# print(c.columns,c.index)
#查询
#可以将DataFrame的列或行获取为一个Series
# 获取列直接
# print(c['a'])
# v    1
# b    2
# n    3
# m    4
# Name: a, dtype: int64

#行索引通过ix
# print(c.ix['v'])
# a      1
# b      5
# c      9
# d    NaN
# Name: v, dtype: object


#可以通过赋值新加一列,赋值可以为数字或列表，也可以通过赋值方式修改
# c['e']=[1,2,3,4]
# print(c)
# c['e'] = 1
# print(c)
#    a  b  c    d  e
# v  1  5  9  NaN  1
# b  2  6  0  NaN  1
# n  3  7  1  NaN  1
# m  4  8  2  NaN  1

#如果赋值的是一个Series 那么索引会匹配，匹配不上为空
# print(c)
#    a  b  c    d
# v  1  5  9  NaN
# b  2  6  0  NaN
# n  3  7  1  NaN
# m  4  8  2  NaN
# c['d']= Series([1,2,3,4],index=['b','v','m','y'])
# print(c)
#    a  b  c    d
# v  1  5  9  2.0
# b  2  6  0  1.0
# n  3  7  1  NaN
# m  4  8  2  3.0


#关键词del 用于删除列
del c['a']
print(c)

#DataFrame 的查询都是视图，如果想显示复制则用copy
