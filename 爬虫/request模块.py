"""
#########################################################################################################requests模块的使用---基本使用
# 导入模块
import requests
# 定义请求地址
url = 'http://www.baidu.com'
# 发送 GET 请求获取响应
response = requests.get(url)
# 获取响应的 html 内容
html = response.text

# response 常用属性
# response.text 返回响应内容，响应内容为 str 类型
# respones.content 返回响应内容,响应内容为 bytes 类型
# response.status_code 返回响应状态码
# response.request.headers 返回请求头
# response.headers 返回响应头
# response.cookies 返回响应的 RequestsCookieJar 对象

# response.content 转换 str 类型
# 获取字节数据
content = response.content
# 转换成字符串类型
html = content.decode('utf-8')
#response.cookies 操作
# 返回 RequestsCookieJar 对象
cookies = response.cookies
# RequestsCookieJar 转 dict
requests.utils.dict_from_cookiejar(cookies)
# dict 转 RequestsCookieJar
requests.utils.cookiejar_from_dict()
# 对cookie进行操作,把一个字典添加到cookiejar中
requests.utils.add_dict_to_cookiejar();
"""
#########################################################################################################requests模块的使用---自定义请求头
# # 导入模块
# import requests
# # 定义请求地址
# url = 'http://www.baidu.com/s'
# # 定义自定义请求头
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# }
# # 定义 GET 请求参数
# params = {
#     "kw":"hello"
# }
# # 使用 GET 请求参数发送请求
# #response = requests.get(url,headers=headers,params=params)
# #POST
# response = requests.post(url,headers=headers,data=params)
# # 获取响应的 html 内容
# html = response.text
# print(html)
#########################################################################################################requests模块的使用---保存图片
# 导入模块
# import requests
# # 下载图片地址
# url = "http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
# # 发送请求获取响应
# response = requests.get(url)
# # 保存图片
# with open('image.png','wb') as f:
#     f.write(response.content)

#########################################################################################################requests模块的使用---保代理服务器
# 导入模块
# import requests
# # 定义请求地址
# url = 'http://www.baidu.com'
# # 定义自定义请求头
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# }
# # 定义 代理服务器
# proxies = {
#     "http":"http://IP地址:端口号",
#     "https":"https://IP地址:端口号"
# }
# # 使用 POST 请求参数发送请求
# response = requests.get(url,headers=headers,proxies=proxies)
# # 获取响应的 html 内容
# html = response.text
#########################################################################################################requests模块的使用---携带Cookie
# 导入模块
import requests
# 定义请求地址
url = 'http://www.baidu.com'
# 定义自定义请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    # 方式一：直接在请求头中携带Cookie内容
                 "Cookie": "Cookie值"
}
# 方式二：定义 cookies 值
cookies = {
    "xx":"yy"
}
# 使用 POST 请求参数发送请求
response = requests.get(url,headers=headers,cookies=cookies)

# 设置忽略证书
#response = requests.get(url,verify=False)
#超时处理
#response = requests.get(url,timeout=5)
# 获取响应的 html 内容
html = response.text
#########################################################################################################requests模块的使用---重试处理retrying
'''
可以使用第三方模块 retrying 模块
1. pip install retrying

'''
import requests
# 1. 导入模块
from retrying import retry

# 2. 使用装饰器进行重试设置
# stop_max_attempt_number 表示重试次数
@retry(stop_max_attempt_number=3)
def parse_url(url):
    print("访问url:",url)
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    proxies = {
        "http":"http://124.235.135.210:80"
    }
    # 设置超时参数
    response = requests.get(url,headers=headers,proxies=proxies,timeout=5)
    return response.text

if __name__ == '__main__':
    url = "http://www.baidu.com"
    try:
        html = parse_url(url)
        print(html)
    except Exception as e:
        # 把 url 记录到日志文件中，未来进行手动分析，然后对url进行重新请求
        print(e)

#########################################################################################################requests模块的使用---保代理服务器
#########################################################################################################requests模块的使用---保代理服务器
#########################################################################################################requests模块的使用---保代理服务器
#########################################################################################################requests模块的使用---保代理服务器
#########################################################################################################requests模块的使用---保代理服务器
#########################################################################################################requests模块的使用---保代理服务器