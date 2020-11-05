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
# setcookie后等待三秒加载视频列表页面
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
            # 页面下滑到底加载列表
            driver.get('http://www.ghmba.online' + zjurl["href"])
            js = "var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            htmll = driver.page_source
            soup2 = BeautifulSoup(htmll, 'lxml')
            # print(soup)
            # #筛选div
            for tag2 in soup2.find_all('li',
                                       class_='task-item task-content mouse-control infinite-item color-gray bg-gray-lighter'):
                #     #筛选名称
                knameurl = tag2.find_all('a', class_='title')
                # print(knameurl)
                for knameurl2 in knameurl:
                    ksname = knameurl2.get_text()
                    ksurl = 'http://www.ghmba.online' + knameurl2["href"]
                    ##################################获取视频URL
                    # 打开页面
                    driver.get(ksurl)
                    # 点击播放按钮
                    # driver.find_element_by_xpath('//*[@id="example_video_1"]/div[5]/button[1]')
                    # 延迟x秒等加载完成
                    # time.sleep(1)
                    # 获取iframe中的内容，因为视频页面是iframe
                    # 切换到iframe
                    iframe = driver.find_elements_by_tag_name('iframe')[0]
                    driver.switch_to.frame(iframe)
                    # switch_to_default_content()  释放iframe 重新回到主页面
                    time.sleep(2)
                    sphtml = driver.page_source
                    # 格式化lxml
                    soup3 = BeautifulSoup(sphtml, 'lxml')
                    # print(soup2)
                    for tag3 in soup3.find_all('div', class_='ballon-video-player'):
                        # 获取div中的url
                        shipin = tag3['data-url']
                        kejian = ''
                        kejianurl = ''
                        # 储存至数据库，在文件下载函数直接写库并把路径保存到数据库
                        value = (zjname2.strip(), ksname.strip(), ksurl, shipin, kejian, kejianurl)
                        wsql.insert(value)
                        print(
                            '本课程名称： ' + zjname2.strip() + '课时：' + ksname.strip() + '课时URL：' + ksurl + '视频MP4地址：' + shipin + '' + '')
                        # 下载处理
                        url = shipin
                        # .strip()去除两端空格,文件名冒号，处理文件名为
                        path1 = 'D:\\Down\\' + zjname2.strip().replace(':', '') + ksname.strip().replace(':', '') + '.mp4'
                        # 去除符号
                        path = path1.replace('【', '').replace('】', '').replace(' ', '')
                        print('视频保存路径为' + path)
                        down.do_load_media(url, path)

                    # 对课件文档的处理
                    for tag4 in soup3.find_all('a', class_='link-darker'):
                        # 获取资料中的url
                        xiazainame = tag4.get_text()
                        xiazaiurl = 'http://www.ghmba.online' + tag3['data-url']
                        print(ksname + xiazainame + xiazaiurl)
                        #储存到库
                        value = (zjname2, ksname, ksurl, '', xiazainame, xiazaiurl)
                        wsql.insert(value)
                        # 下载处理----文件下载暂不处理
# for urlname in kname:
# print('当前章节------------'+urlname.get_text()+'  '+'http://www.ghmba.online'+urlname["href"])
#
#     url2='http://www.ghmba.online'+urlname["href"]
#     response2 = requests.request("GET", url, data=payload, headers=headers)
#     html2 = response2.text
#     soup2 = BeautifulSoup(html2,'lxml')
