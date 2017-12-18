# encoding: utf-8

#1 数组的欧式距离

import numpy as np
from numpy import array
def distance(v1,v2):
    b = np.square(v1-v2)
    d = b.sum()**0.5
    return d

# 2 knn算法
def KNN (t,v,l,k):
    d =np.zeros(v.shape[0])      #创建全0 一维数组，盛放距离
    for i in range(v.shape[0]):
        d[i]=distance(v[i],t)        #生成距离数组
    ds= np.column_stack((d,l))      #添加数组对应标签
    ds = ds[ds[:, 0].argsort()]      #按距离排序
    d1 = ds[0: k+1,1]               #提取排序后的标签
    if np.sum(d1)>d1.shape[0]/2:      #如果1累积大于数组个数一半，就1类
        return 1
    else:
        return 0


# 3 文件提取

f = np.loadtxt('isisTestset.txt',delimiter=',')
labels = f [:,-1]
var = f[:,0:-1]
text = f[6,0:-1]
print(KNN(text,var,labels,5))
