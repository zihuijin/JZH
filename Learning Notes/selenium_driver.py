#selenium 知识----------------
#coding:utf-8


# Selenium 是什么？一句话，自动化测试工具。它支持各种浏览器，包括 Chrome，Safari，Firefox 等主流界面式浏览器，
# 如果你在这些浏览器里面安装一个 Selenium 的插件，那么便可以方便地实现Web界面的测试。
# 换句话说叫 Selenium 支持这些浏览器驱动。
# 话说回来，PhantomJS不也是一个浏览器吗，那么 Selenium 支持不？答案是肯定的，这样二者便可以实现无缝对接了。
# Selenium支持多种语言开发，比如 Java，C，Ruby,python等等
# 安装一下 Python 的 Selenium 库，再安装好 PhantomJS，不就可以实现 Python＋Selenium＋PhantomJS 的无缝对接了嘛！
# PhantomJS 用来渲染解析JS，Selenium 用来驱动以及与 Python 的对接，Python 进行后期的处理，完美的三剑客！
# 有人问，为什么不直接用浏览器而用一个没界面的 PhantomJS 呢？答案是：效率高！
# Selenium 2，又名 WebDriver，它的主要新功能是集成了 Selenium 1.0 以及 WebDriver（WebDriver 曾经是 Selenium 的竞争对手）。
# 也就是说 Selenium 2 是 Selenium 和 WebDriver 两个项目的合并，即 Selenium 2 兼容 Selenium，它既支持 Selenium API 也支持 WebDriver API。


#安装selenium
# pip install selenium

# (1) 打开浏览器
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
#driver = webdriver.Chrome('/home/bing/Downloads/chromedriver')  #自动配置路径
# #drivre = webdriver.Firefox()
# driver.get('http://www.baidu.com/')

# 运行这段代码，会自动打开浏览器，然后访问百度。
# 如果程序执行错误，浏览器没有打开，那么应该是没有装 Chrome 浏览器或者 Chrome 驱动（chromedriver）没有配置在环境变量里。下载驱动，然后将驱动文件路径配置在环境变量即可。
#其中 driver.get ，WebDriver 会等待页面完全加载完成之后才会返回，即程序会等待页面的所有内容加载完成，JS渲染完毕之后才继续往下执行。
# 注意：如果这里用到了特别多的 Ajax 的话，程序可能不知道是否已经完全加载完毕。


# （2）模拟提交
#首先等页面加载完成，然后输入到搜索框文本，点击提交。
# WebDriver 提供了许多寻找网页元素的方法，譬如 find_element_by_* 的方法。例如一个输入框可以通过  find_element_by_name 方法寻找 name 属性来确定。
# elem =driver.find_element_by_name('q')
# elem.send_keys('python')
# elem.send_keys(Keys.RETURN)
#  find_element_by_id('')
# 我们可以利用 Keys 这个类来模拟键盘输入。
##通过.send_keys(keys.按键名称)调用按键：
#.send_keys(Keys.TAB) # 按TAB键
#.send_keys(Keys.ENTER) # 按回车键
#获取网页渲染后的源代码。输出 page_source 属性即可。
#不过 close 方法相当于关闭了这个当前页面，然而 quit 是关闭了整个浏览器。


#（3）页面操作
#》 页面交互
#》 搜索标签
# <input type="text" name="passwd" id="passwd-id" />
#寻找input标签可以搜索属性，标签名，还有xpath
# elem = driver.find_element_by_type('text')
# elem1 = driver.find_element_by_name('passwd')
# elem2 = driver.find_element_by_id('passwd-id')
# elem3 = driver.find_element_by_tag_name('input')
# ele4 = driver.find_element_by_xpath("//input[@id='passwd_id']")
# ————————元素选取-------------
#find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_class_name
# find_element_by_tag_name
# find_element_by_link_text
# find_element_by_partial_link_text
#  find_element_by_css_selector
# ______________________________________
# **** xpath注意： 如果有多个元素匹配了 xpath，它只会返回第一个匹配的元素。如果没有找到，那么会抛出 NoSuchElementException 的异常。
# 》 向文本输入内容
# elem.send_keys('content')
# elem.clear()        #你可以对任何获取到到元素使用 send_keys 方法，不过输入的文本不会自动清除，都会在原基础上自动输入，可以手动清除
# 》可以利用 Keys 这个类来模拟点击某个按键。
#通过.send_keys(keys.按键名称)调用按键：
#.send_keys(Keys.TAB) # 按TAB键
#.send_keys(Keys.ENTER) # 按回车键
#  》找到按钮模拟点击
# elem.click()



# (4) Cookies处理
# # 》为页面添加 Cookies，用法如下
# driver.get("http://www.example.com")
# cookie = {‘name’: ‘foo’, ‘value’: ‘bar’}
# driver.add_cookie(cookie)
# # 》获取页面 Cookies，用法如下
# driver.get("http://www.example.com")
# driver.get_cookies()

# 》携带cookie
# from selenium import webdriver
# browser = webdriver.Chrome()
#
# url = "https://www.baidu.com/"
# browser.get(url)
# # 通过js新打开一个窗口
# newwindow='window.open("https://www.baidu.com");'
# # 删除原来的cookie
# browser.delete_all_cookies()
# # 携带cookie打开
# browser.add_cookie({'name':'ABC','value':'DEF'})
# # 通过js新打开一个窗口
# browser.execute_script(newwindow)
# input("查看效果")
# browser.quit()
# 》关闭图片
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2
#     }
# }
# options.add_experimental_option('prefs', prefs)
# browser = webdriver.Chrome(chrome_options=options)
#
# # browser = webdriver.Chrome()
# url = "http://image.baidu.com/"
# browser.get(url)
# input("是否有图")
# browser.quit()



# （5） 关闭页面
# driver.quit()   #关闭浏览器
# driver.close()   #关闭当前页面



#爬取知乎-------------------------------------------------------------
#coding:utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
from bs4 import BeautifulSoup
#在后台建立一个虚拟界面
display = Display(visible=0, size=(800, 800))
display.start()

# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36



url = "https://www.zhihu.com/"
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
driver.get(url)  #打开url
time.sleep(0.5)  #等程序加载完
# driver.maximize_window()   # 浏览器全屏显示
driver.find_element_by_xpath('//a[@class="MobileAppHeader-authLink"]').click()

driver.find_element_by_xpath('//button[@class="Button"]').click()

driver.find_element_by_name('username').send_keys('17831108012')

driver.find_element_by_name('password').send_keys('JinZiHui1!')


driver.find_element_by_xpath('//button[@class="Button Login-submitButton Button--primary Button--blue"]').click()

time.sleep(0.1)

driver.get_screenshot_as_file("aa.png")  #截图保存

inp = driver.find_element_by_xpath('//input[@class="zu-top-search-input"]')
inp.send_keys('猎场')
inp.send_keys(Keys.RETURN)
#enter（回车）来代替按钮
# password.send_keys(Keys.ENTER)
print(driver.current_url)  #输出当前网页
print(driver.page_source)  #输出当前代码

driver.get_screenshot_as_file("bb.png")  #截图保存
#老弹出验证页面
if driver.find_element_by_xpath('//div[@class="modal-dialog-title"]'):
    driver.find_element_by_xpath('//span[@class="modal-dialog-title-close"]').click()




driver.quit()   #关闭浏览器
# driver.close()   #关闭当前页面
display.stop()  #关闭虚拟界面
# ------------------------------------------------------------------------------------------
