# -*- coding: utf-8 -*-
"""
IDE:               PyCharm Community Edition
-------------------------------------------------
   Project Name:   PythonTest
   File Name：     爬虫
   Description :
   Author :       Admin
   date:          2018-6-7
-------------------------------------------------
   Change Activity:
                   2018-6-7:
-------------------------------------------------
"""
'''
import urllib2
#获取html
response = urllib2.urlopen("http://www.wushuo.xyz")

#输出到文件
File = open("text2.txt" , "wb")
File.write(response.read())
print response.read();
'''
'''
import urllib2
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()
'''
'''
#POST方式
import urllib
import urllib2

values = {"user_login": "wushuo" , "user_pass": "wushuo1998"}
data = urllib.urlencode(values)
url = "http://www.wushuo.xyz/wp-login.php?redirect_to=http%3A%2F%2Fwww.wushuo.xyz%2Fwp-admin%2F&reauth=1"
request = urllib2.Request(url , data)
response = urllib2.urlopen(request)
print response.read()
'''
import urllib
import urllib2

url = "http://vip.wushuo.xyz/admin/login.php"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
values = {"username": "wushuo" , "password": "wushuo1998"}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url , data , headers)
response = urllib2.urlopen(request)
page = response.read()
print page
