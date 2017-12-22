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




driver.quit()   #
# driver.close()
display.stop()

