

#bs4
#方便地提取出HTML或XML标签中的内容
#beautifulSoup 官方解释：Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
# Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度


# 1. 导入与安装
#pip install beautifulsoup4
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
#2. 创建soup对象
soup = BeautifulSoup(html)
#如果报这种警告，就是没指定解析器  UserWarning: No parser was explicitly specified
# soup = BeautifulSoup(html, 'html.parser')   #要加上指定解析器HTML.parser
# #另外，我们还可以用本地 HTML 文件来创建对象，例如
# soup = BeautifulSoup(open('xinwen.html'))
# 上面这句代码便是将本地 index.html 文件打开，用它来创建 soup 对象

# 下面我们来打印一下 soup 对象的内容，格式化输出
# print(soup.prettify())

# 3. 四大对象种类

#bs4将复杂的html转化为树形结构，树形结构的每一个节点都是python对象，所有对象归纳为4中

# 1. Tag：通俗点讲就是 HTML 中的一个个整标签，例如	<title>The Dormouse's story</title>
#soup+标签名可以直接输出第一个标签
# eg:  print（soup.head）
#<head><title>The Dormouse's story</title></head>
#可以验证标签类型
#eg: print(type(soup.a))
# <class 'bs4.element.Tag'>
#对于 Tag，它有两个重要的属性，是 name 和 attrs
# print(soup.name)
#[document]
#print(soup.a.name)
#a
#print(soup.a.attrs)  #标签属性：内容 组成的字典
# {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
#我们可以直接获得某一个标签属性内容
#print soup.p['class']    或  	#print soup.p.get('class')
#['title']
#我们可以对这些属性和内容等等进行修改
#soup.p['class']="newClass"
# print (soup.p)
#还可以对这个属性进行删除，例如
# del soup.p['class']
# print (soup.p)
#<p name="dromouse"><b>The Dormouse's story</b></p>



#2. NavigableString    标签内部的文字
# 用 .string 访问标签内容
# 注：（1）可以返回一层标签内容，也可以返回只含一层子标签的标签内容
 #eg:<p><a>string1</a></p>.   print（soup.p.string）#string1
# （2）但是如果标签内含有太多子标签，那么,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
#用这个我们可以判断是否标签含有一个子标签
# print(soup.p.string)
#The Dormouse's story
# print(type(soup.p.string))
# <class 'bs4.element.NavigableString'>

soup.p.get_text()----可以得到p的文本内容,不用担心string的子标签内容

#（3）多 个内容  知识点： .strings  .stripped_strings 属性
# #soup.tag.strings,--遍历标签的所有内容
# for string in soup.strings:
#     print(repr(string))
# #soup.tag.stripped_strings---遍历标签的所有内容,去掉空格与空白符
# for string in soup.stripped_strings :
#     print(repr(string))



# 3. BeatifulSoup    一个文档的全部内容
# 大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下

# print type(soup.name)
# #<type 'unicode'>
# print soup.name
# # [document]
# print soup.attrs
#{} 空字典

#4. Comment     Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。
#标签内容的注释符会被去掉
# print soup.a
# print soup.a.string
# print type(soup.a.string)
#
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie
# <class 'bs4.element.Comment'>
#为了防止这些问题
# if type(soup.p.string) == 'bs4.element.Comment':
#     print(soup.a.string)
# 上面的代码中，我们首先判断了它的类型，是否为 Comment 类型，然后再进行其他操作，如打印输出。

# 4.   遍历文档树
# （1）直接子节点  要点：.contents  .children  属性
# tag 的 .content 属性可以将tag的子节点以列表的方式输出
# print(soup.body.contents)
#['\n', <p class="title" name="dromouse"><b>The Dormouse's story</b></p>, '\n', <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>, '\n', <p class="story">...</p>, '\n']

# 输出方式为列表，我们可以用列表索引来获取它的某一个元素
# print(soup.body.contents[1])
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

#.children属性  它返回的是list生成器，我们可以遍历获取所有子节点


# （2）所有子孙节点   知识点：.descendants 属性

# for child in soup.descendants:
#     print child
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <b>The Dormouse's story</b>
# The Dormouse's story
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie ,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# Lacie
#  and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# Tillie
# ;and they lived at the bottom of a well.
# <p class="story">...</p>
# ...
#（3）多 个内容  知识点： .strings  .stripped_strings 属性
# #soup.tag.strings,--遍历标签的所有内容
# for string in soup.strings:
#     print(repr(string))
# #soup.tag.stripped_strings---遍历标签的所有内容,去掉空格与空白符
# for string in soup.stripped_strings :
#     print(repr(string))
# （4）父节点   知识点：.parents 属性
#soup.tag.parents   可以递归到标签的所有父节点
# for i in soup.title.parents:
#     print(i.name)

# （5）兄弟节点    知识点：.next_sibling  .previous_sibling 属性   知识点：.next_siblings  .previous_siblings 属性
#兄弟节点是属于同一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，.previous_sibling 则与之相反，如果节点不存在，则返回 None
#通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
#注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
#eg：
# for i in soup.a.next_siblings:
#     print(i)

# （6）前后节点    知识点：.next_element  .previous_element 属性    previous_element     知识点：.next_elements  .previous_elements 属性
#节点的前一个节垫previous_element  后一个节点  next_element
##节点的所有前节点previous_elements  所有后节点  next_elements
# for i in soup.a.next_elements:
#     print(i)




# 4.搜索文档树
# （1）find_all( name , attrs , recursive , text , **kwargs )   find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

# 1）name 参数   name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
# A.传字符串 （标签名）
#print(soup.find_all('p'))   ----找出所有p标签
# B.传正则表达式   通过正则表达式的 match() 来匹配内容.
# print(soup.find_all(re.compile('^b')))   #所有以b开头的标签
#c 传列表  ：传多个字符串（标签）
# print(soup.find_all(['a','b']))    ---找出所有a,b标签
# D.传 True  True 可以匹配任何值,下面代码查找到所有的tag
# for i in soup.find_all(True):
#     print(i.name)
# E.传方法
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')   #找出含有class属性，不含id属性
#
# print(soup.find_all(has_class_but_no_id))

# 2）keyword 参数 (属性值)
print(soup.find_all(id = 'link2'))
print(soup.find_all(href = re.compile('elsie')))
print(soup.find_all(id = 'link2',href = re.compile('elsie')))  #可以同时匹配多个属性
soup.find_all("a", class_="sister")    #可以一齐传入字符与关键字
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 在这里我们想用 class 过滤，不过 class 是 python 的关键词，所以加_以区分
soup.find_all("a", class_="sister")
#可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag

soup.find_all(attrs = {"data-foo":"value"})
# [<div data-foo="value">foo!</div>]

# 3）text 参数
# 通过 text 参数可以搜搜文档中的字符串内容,与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True


soup.find_all(text="Elsie")
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]

# 4）limit 参数    ---限制find_all搜索文档数量
print(soup.find_all('a',limint = 2))

# 5）recursive 参数  #find_all 默认会搜索所有子孙节点，用recursive = False 就可以搜索所有子节点

soup.html.find_all("title")
# [<title>The Dormouse's story</title>]

soup.html.find_all("title", recursive=False)
# []

# （2）find( name , attrs , recursive , text , **kwargs )
#find_all 相似，find_all 返回的是列表，而find直接返回第一个元素


# （3）find_parents()  find_parent()
#
# find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容
#
# （4）find_next_siblings()  find_next_sibling()
#
# 这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点
#
# （5）find_previous_siblings()  find_previous_sibling()
#
# 这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点
#
# （6）find_all_next()  find_next()
#
# 这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点
#
# （7）find_all_previous() 和 find_previous()
#
# 这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点


# 8.CSS选择器   通过id,class查找标签，返回列表

# 我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
# （1）通过标签名查找
print (soup.select('title'))
#[<title>The Dormouse's story</title>]

# （2）通过类名查找
print soup.select('.sister')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# （3）通过 id 名查找
print soup.select('#link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# （4）组合查找

print soup.select('p #link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# （5）直接子标签查找
print soup.select("head > title")
#[<title>The Dormouse's story</title>]
# （5）属性查找
print soup.select('a[class="sister"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格

print soup.select('p a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
# 效率还是lxml 比较快
