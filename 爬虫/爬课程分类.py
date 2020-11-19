# 自动获取每个课程(手动分页)-获取课程下章节连接
import json
import time
import requests
import urllib
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql
import wsql
import down
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# 新建一个chrome浏览器 executable_path=chromedriver.exe地址
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# UA指定为iphone打开
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # 模拟iPhone X浏览
# 新建浏览器
driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
url = "http://www.ghmba.online/my/courses/learning"

# # 打开网页
driver.get(url)
driver.add_cookie(
    {'domain': 'www.ghmba.online', 'expiry': 1635923066, 'httpOnly': True, 'name': 'REMEMBERME', 'path': '/',
     'secure': False,
     'value': 'Qml6XFVzZXJcQ3VycmVudFVzZXI6Wkc5dWJtVmZNVGs0TVVCb2IzUnRZV2xzTG1OdmJRPT06MTYzNTkyMzA0MTo2ZWIwNTVhZTM5OGVkNDYzNWY5ODNhMmQ1NzUzZGZlOWEwODhkMWFkYTJjMmMzZjk5MTk0OTA5MDczNzI1MmEy'})
# driver.delete_all_cookies()
# setcookie后等待三秒加载视频列表页面```````````
driver.set_page_load_timeout(3000)
# 页面下滑到底加载列表
driver.get('http://www.ghmba.online/my/courses/learning?page=2')
js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(4)
# 获取响应的 html 内容
htmll = driver.page_source
soup = BeautifulSoup(htmll, 'lxml')
# 筛选div
for tag in soup.find_all('div', class_='my-course-item cd-mb40 clearfix'):
    # 筛选名称
    kname = tag.find_all('a', class_='cd-link-major')
    # 筛选链接
    kurl = tag.find_all('a', class_='btn cd-btn cd-btn-primary cd-btn-lg')

    for zjname in kname:
        # print('当前章节为'+zjname.get_text())
        zjname2 = zjname.get_text()
        for zjurl in kurl:

            print('当前章节***************************' + zjname.get_text() + '  ' + 'http://www.ghmba.online' + zjurl["href"])