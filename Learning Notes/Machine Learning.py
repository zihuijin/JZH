#-*- coding:utf8 -*-
#安装anaconda 在jupyter notebook 中打开网页版


# 1。numpy 包的基础讲解------------------------------------------------
#numpy 含有ndarray n维数组结构，还有一些简单运算  a dimension array
#ndarray :是由相同类型元素组成的多维数组，特点是创建好数组一旦指定好大小就不会改变
import numpy as np
from numpy import array
# a=array([[1,2,3,4],
#          [4,5,6,7]
#          ])
# print(a,\
# a.dtype,\    #数组类型
# a.ndim,\    #数组维度
# a.shape,\   #数组结构
# a.size)   #数组大小
#1.ndarray 的常见创建方式

#可以直接传入序列
# a=[1,2,3,4,5]
# print(array(a))

#可以直接创建
# a=array([
#     [2,3,4],
#     [3,4,5]
# ])

#创建全0或全1数组,默认为float
# b=np.zeros(10)
# c=np.zeros((2,4))
# np.ones((4,5))

#用arange创建等差序列 （相当于内置的range）
# print(np.arange(0,10,1))

#reshape()可以改变结构
# a=np.arange(10).reshape(2,5)
# print(a)

#2.array 的数据类型

#dtype————可以指定数组类型
# a=array([1,2,4],dtype=int)
# print(a)

#可以通过astype 方法转化dtype,必须赋值
# a=a.astype(float)

# b=array(['1'])
# a=a.astype(b.dtype)
# print(a)

#3. 数组与标量的运算：数组不用循环即可对数据执行批量运算，这叫矢量化，数组之间的运算会应用到元素级
# a=array([
#     [1,2,3],
#     [4,5,6]
# ])
# b=array([
#     [1,2,4],
#     [4,5,6]
# ])
# print(a*b,'\n\n',a+b,'\n\n',1/a,'\n\n',b-1,'\n\n',3*a)

#4.基本的索引与切片   ----索引从0开始，切片左闭右开
# a=np.arange(10)
# print(a,a[5],a[2:6])
# a[2:5]=[7,78,789]    #注意：数组切片是原数组的视图，视图上的任何修改都会反映到原数组上
# print(a)
# b=a.copy()       #要想切片视图与原数组没有关系，则可以显式复制
# b[2:5]=[1,2,3]
# print(a)


#
# a=array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# a[0]=42
# [[42 42 42]    ---数据也可赋值   #数组索引出的数据子集也是数组视图
#  [ 4  5  6]
#  [ 7  8  9]]

# print(a[:2])
# # [[1 2 3]
# #  [4 5 6]]

# print(a[0][1],a[2][2],a[2,2],a[0])    #索引从0开始，第一个数为一维，第二个数是二维  a[1][1]  == a[1,1]
# print(a[1][:2])  # a[1][:2]
# print(a[:,:2])
#  # [4 5]
#  # [7 8]]

# print(a==1)      #比较运算 a>1,a<1,a==1,a!=1,对每一个数组元素进行比对，如果正确返回TRUE，否则返回False
# [[ True False False]
#  [False False False]
#  [False False False]]

#布尔型数组可以做数组索引
# print(a[a>3])

# a[a<3]=0
# print(a)

#可以加布尔条件  & |
# print(a[(a>1)&(a<5)])

# b=np.empty((4,5))
# for i in range(4):
#     b[i]=i
# print(b[[1,3]])   #花式索引索引里传列表

# d=np.array([
#     [1,2,3,4,5,6],
#     [4,5,6,7,8,9],
#     [7,8,9,1,2,3],
#     [4,5,6,7,8,9]
# ])
# print(d[1:3,[1,4]])

#索引总结：1.首先索引加【】    ***********************************
#2.数组索引第一个是一维，第二个是二维，依次类推
#3.【1，1:3,[1,5]】
#单个数字是元素，就是一排；连续取是切片表示为1:3，不加任何括号，花式索引加【】，表示单个元素
#4.数组索引与切片都是视图，修改后修改原数组
#5.布尔索引，也就是加条件【a>1】

#5.数组的转置于轴对换
# a=np.arange(10).reshape(2,5)
# print(a,'\n\n',a.T,'\n\n')

#7.通用函数：快速的元素级数组元素----用函数来代替循环，要快一些
#1.一元数组函数
# a=np.arange(10)
# b=np.sqrt(a)   #开跟号
# f=np.square(a)   #平方
# c=np.exp(a)     #e^a
# e=np.abs(a)     #绝对值
# g=np.log10(a)    #
# h=np.sign(a)     #得出符号
# i=np.rint(a)    #取整
# j=np.isnan(a)     #判断是否为空
# k=np.cos(a)      #

#2.二元数组函数(两个数组结构相同)
# b=np.arange(10)
# l=np.add(a,b)     #对应元素相加
# m=np.subtract(a,b)   #对应元素相减
# n=np.multiply(a,b)    #对应元素相乘



#np.where   ,来等同代替三元表达式  :: x if condition else y

# a=np.arange(-5,5)
#将<0的加1
# b=np.where(a<0,a+1,a)
# print(a,b)
#可以变成复杂的条件表达式
# c=np.where(a<-3,0,np.where(a<0,1,np.where(a<5,2,3)))

#8.数学统计方法(聚合函数)
# print(a.sum(),a.mean(),a.std(),a.var(),a.min(),a.max())
# a.sum(1)        #聚合函数一样，0是纵向，1是横向
# print(np.sum(a,0))

#9.布尔函数方法
# a=a>3
# print(a.all(),a.any())   #a.all()---判断是否 全部为True,a.any()------判断是否 有False

#10.sort 方法排序
# a.sort()     #从小到大排序
# print(a)
# a.sort()
# a=array([
#     [1,5,4,7,3],
#     [4,8,2,5,6],
#     [8,6,8,2,4]
# ])

# a.sort()      #默认是1轴：横向
# a.sort(0)     #默认是0轴：纵向

#注意a.sort 就地排序，会改变原数组
#而np.sort  是复制排序，不会改变原数组

##10.1  补充  数组增加行列
#
# a=array([
#     [1,5,4,7,3],
#     [4,8,2,5,6],
#     [8,6,8,2,4]
# ])
# row = a[-1]
# col = a[:,-1]
# # a=np.row_stack((a,row))      #a 增加一行
# b=np.column_stack((a,col))     #b  增加一列
# print(b)

#10.2 按第一列排序
# import numpy as np
# a=np.array([
#     [8,5,2,7,3],
#     [2,4,1,5,6],
#     [7,2,3,1,5]
# ])
#
# a=a[a[:,0].argsort()]
# print(a)

#11.去重  np.unique(a)
# print(np.unique(a))


#12.数组文件的输入输出 np.save  np.load
# np.save('a',a)    #将数组保存在磁盘中，默认后缀为 .npy
# print(np.load('a.npy'))    #将数组从磁盘中加载出来

#13.存取文本文件
#将数据文件加载到二维数组中  np.loadtxt
# arr=np.loadtxt('isisTestset.txt',delimiter=',')
# print(arr)
#将数组写入以符号隔开的文本文件中   np.savetxt
# np.savetxt('a.txt',a,delimiter=',')
# arr=np.loadtxt('a.txt',delimiter=',')

#14.数组的线性代数（矩阵乘法，矩阵分解，行列式）
#矩阵乘法用  np.dot(a,b)  或 a.dot(b)    要求是第一个矩阵的列 = 第二个矩阵的行
# b=a.T
# print(np.dot(a,b))
#  np.linalg  中有很多矩阵运算，eg:矩阵的逆(条件是方阵)
# b=np.random.randint(1,10,16).reshape(4,4)
# print(np.linalg.inv(b))



#随机数生成  用numpy 内置的 random
#生成正态分布数组  np.random.normal()
# samples  = np.random.normal(size=(4,5))
# print(samples)

#生成0-1的随机数 参数是shape
# s2 = np.random.rand(3,2)
# print(s2)
#生成随机整数 (low ,high ,size)
# s3 = np.random.randint(1,10,5)
# print(s3)
#生成标准正态分布的样本值
# s4= np.random.randn(2,4)
# print(s4)
#生成二项分布的样本值
# s5=np.random.binomial(9, 0.1, 20)
# print(s5)
#卡方分布chisqure  [0,1]分布 uniform


#随机小例子：随机漫步
#1.用普通方式实现
# position=0
# walk=[position]
# steps = 1000
# for i in range(steps):
#     step = np.where(np.random.randint(0,1),1,-1)
#     position += step
#     walk.append(position)
# for i in walk:
#     print(i)

#用数组方式
# nsteps = 1000
# draws = np.random.randint(0,2,size=nsteps)
# step = np.where(draws>0,1,-1)
# walk = step.cumsum()

#做500 个随机漫步
# a=np.random.randint(0,2,size=(500,1000))
# b=np.where(a>0,1,-1)
# s=np.cumsum(b,axis=1)
# print(s,s.max())
# x = np.abs(s)>=30        #看看有无在30，-30 以外的
# print(x.any(1))


