# 使用流程
# 导入urllib2模块
# 发起请求获取响应数据
# 定义请求地址
# 自定义请求头
# 自定义请求对象
# 发送请求
# 处理响应内容

# import urllib.request
#
# # 2. 发起网络请求
# # 2.1. 定义请求地址
# url = "https://github.com"
# # 2.2. 自定义请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
#     "Referer": "https://github.com/",
#     "Host": "github.com"
# }
# # 定义请求对象
# req = urllib.request.Request(
#     url=url,
#     headers=headers
# )
# # 发送请求
# resp = urllib.request.urlopen(req)
# # 处理响应
# with open('github.txt', 'wb') as f:
#     f.write(resp.read())




###########################################如果使用在URL中需要进行转义
# -*- coding: utf-8 -*-

# 1. 导入模块
import urllib.request
import urllib.parse

# 2. 发起请求获取响应

wd = input("请输入查询内容：")

# 2.1 定义请求地址
url = "https://www.baidu.com/s?wd="
# 2.2 定义自定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "https://github.com/",
    "Host": "github.com"
}
# 2.3 定义请求对象
request = urllib.request.Request(
    url=url + urllib.parse.quote(wd),
    headers=headers
)
# 2.4 发送请求
response = urllib.request.urlopen(request)

# 3. 处理响应
with open('02.html','wb') as f:
    f.write(response.read())
response.read()
#返回值是字节串，获取字符串内容需要进行 decode
html = response.read().decode('utf-8')
