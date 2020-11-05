# 测试类
import os
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
# setcookie后等待三秒加载视频列表页面
driver.set_page_load_timeout(3000)
# 页面下滑到底加载列表
driver.get('http://www.ghmba.online/my/course/120')
# 课程名称
kcmc = '导学阶段'
js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)

# 获取全局渲染后代码
htmll = driver.page_source
soup = BeautifulSoup(htmll, 'lxml')
# print(soup)
# #筛选div
for tag in soup.find_all('li', class_='task-item task-content mouse-control infinite-item color-gray bg-gray-lighter'):
    #     #筛选名称
    knameurl = tag.find_all('a', class_='title')
    # print(knameurl)
    for knameurl2 in knameurl:
        zjname = knameurl2.get_text()
        zjurl = 'http://www.ghmba.online' + knameurl2["href"]
        ##################################获取视频URL
        # 打开页面
        driver.get(zjurl)
        # 点击播放按钮
        # driver.find_element_by_xpath('//*[@id="example_video_1"]/div[5]/button[1]')
        # 延迟x秒等加载完成
        # time.sleep(1)
        # 获取iframe中的内容，因为视频页面是iframe
        # 切换到iframe

        iframe = driver.find_elements_by_tag_name('iframe')[0]
        driver.switch_to.frame(iframe)
        # switch_to_default_content()  释放iframe 重新回到主页面
        sphtml = driver.page_source
        # 格式化lxml
        soup2 = BeautifulSoup(sphtml, 'lxml')
        # print(soup2)
        for tag2 in soup2.find_all('div', class_='ballon-video-player'):
            # 获取div中的url
            shipin = tag2['data-url']
            # kejian=''
            # kejianurl=''
            # # 储存至数据库
            value = (kcmc, zjname, zjurl, shipin, '', '')
            wsql.insert(value)
            print(kcmc + '课时：' + zjname + '课时URL：' + zjurl + '视频MP4地址：' + shipin + '' + '')
            url = shipin
            # .strip()去除两端空格,文件名冒号
            path1 = 'D:\\Down\\' + kcmc + zjname.strip().replace(':', '') + '.mp4'
            # 去除符号
            path = path1.replace('【', '').replace('】', '').replace(' ', '')
            print('路径为' + path)
            down.do_load_media(url, path)
        for tag3 in soup2.find_all('a', class_='link-darker'):
            # 获取资料中的url
            xiazainame = tag3.get_text()
            xiazaiurl = 'http://www.ghmba.online' + tag3['data-url']
            print(zjname + xiazainame + xiazaiurl)
            value = (kcmc, zjname, zjurl, '', xiazainame, xiazaiurl)
            wsql.insert(value)
#     #筛选链接
#     kurl=tag.find_all(kname["href"])
#     print(kname)


# ##登录代码
# username=driver.find_element_by_id('login_username')
# username.send_keys('董磊')
# password=driver.find_element_by_id('login_password')
# password.send_keys('002332')
# driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()


# driver.add_cookie("REMEMBERME:"Qml6XFVzZXJcQ3VycmVudFVzZXI6Wkc5dWJtVmZNVGs0TVVCb2IzUnRZV2xzTG1OdmJRPT06MTYzMDM5MjAzMjpkOGFlNzg5OWZiNDA5MTA1Njk4MDRmNmFmNjYxZGQzNDRlOGQwNmZlMmE4ZTI0OWJjN2ZhNGZjNDBjMzU2NDc2;","_pk_testcookie.179.c5a7"="1","online-uuid":"A999F7C9-23CF-7146-1A5C-C10D996EDBE9","PHPSESSID":"4ba4a3oom4jb1nagmd6v2sh7jg","_pk_ses.179.c5a7":"1,"_pk_id.179.c5a7":"3deebaee9a8814bd.1598856027.3.1604306811.1604306222.")
# response = requests.request("GET", url, data=payload, headers=headers)
# 设置忽略证书
# response = requests.get(url,verify=False)
# 超时处理
# response = requests.get(url,timeout=5)
# 获取响应的 html 内容

# html = driver.text
# soup = BeautifulSoup(html,'lxml')
# print(soup)


# #筛选div
# for tag in soup.find_all('div',class_='my-course-item cd-mb40 clearfix'):
#     #筛选名称
#     kname=tag.find_all('a',class_='cd-link-major')
#     #筛选链接
#     kurl=tag.find_all('a',class_='btn cd-btn cd-btn-primary cd-btn-lg')
#
#     for zjname in kname:
#         # print('当前章节为'+zjname.get_text())
#         for zjurl in kurl:
#             print('当前章节------------'+zjname.get_text()+'  '+'http://www.ghmba.online'+zjurl["href"])
#             #url2='http://www.ghmba.online'+zjurl["href"]
#             url2='http://www.ghmba.online/my/course/204'
#             response2 = requests.request("GET", url, data=payload, headers=headers)
#             html2 = response2.text
#             soup2 = BeautifulSoup(html2,'lxml')
#
#
#


# for urlname in kname:
# print('当前章节------------'+urlname.get_text()+'  '+'http://www.ghmba.online'+urlname["href"])
#
#     url2='http://www.ghmba.online'+urlname["href"]
#     response2 = requests.request("GET", url, data=payload, headers=headers)
#     html2 = response2.text
#     soup2 = BeautifulSoup(html2,'lxml')
