#coding:utf-8
import os
print(os.listdir('iconset1'))      #os.listdir(path)---将文件夹里的文档名以列表形式返回
print(os.getcwd())             #os.getcwd()----返回当前工作目录
#os.mkdir(path,mode)               # 创建目录
# os.chdir('pictures')          #os.chdir(dirname)改变当前目录到设定目录
# print(os.path.isdir('pictures/i.jpg'))   #os.path.isdir(name) 判断name是否是文件夹，如果是返回True
# print(os.path.isfile('pictures'))        #os.path.isfile(name) 判断name是否是文件，如果是返回True,如果不是或没有返回false
print(os.path.exists('tmp'))         #os.path.exists(name)  判断文件或文件夹是否存在
print(os.path.getsize('urls/aa'))   #os.path.getsize(name)   返回文件大小，如果是文件夹则返回0
print(os.path.abspath('tmp'))       #os.path.abspath(name)   获得绝对路径
# print(os.path.split('urls/aa'))     #os.path.split(path)  分割路径的目录与文件名('urls','aa')（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
# print(os.path.splitext('i.jpg'))    #os.path.splitext(name)   分割文件名与其扩展名('i','jpg')
# print(os.path.join('pictures','i.jpg'))   #os.path.join(path,name)连接目录与文件名（或目录名）


# for root, dirs, files in os.walk('iconset1'):            #os.walk遍历path，返回一个对象，他的每个部分都是一个三元组,('目录x'，[目录x下的目录list]，目录x下面的文件)
#     # print(root,'*', dirs,'*',files)
#     #找出所有的文件路径
#
#     for f in files:
#         print(f)
#         with open('w','a') as w:
#             w.write(os.path.join(root,f)+'\n')
#     #找出所有的文件夹路径
#     # for f in dirs:
#     #     print(f)
#     #     with open('w1', 'a') as w:
#     #         w.write(os.path.join(root, f) + '\n')

#数出三级文件的总文件数
o=0
w=open('textnum','a')
dir  = input('dir:')
list1 = os.listdir(dir)
for line in list1:
    if os.path.isdir(line):
        for i in os.listdir(line):
            o+=1
            w.write(line+'\n')
            print(i)
    else:
        o=o+1
        w.write(line+'\n')
        print(line)
print(o)
w.write(str(o))







