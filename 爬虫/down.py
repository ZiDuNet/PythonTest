import os
import requests
import wsql


# url='http://www.ghmba.online/course/178/activiy/2612/download?materialId=3275'
# path=r'D:\Down\123'
# r = requests.get(url)
# with open(path, 'wb') as f:
#     f.write(r.content)
#     f.close()
#     print('文件保存成功')
def do_load_media(url, path):
    # url='http://ese6a7b7c8d5ti-pub.pub.qiqiuyun.net/67785/b54d7382cb8c46b79172f3900d85c08e/ltisv86nsWg3xBWw-merged-hd.mp4'
    # path=r'D:\Down\1.mp4'
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print('文件保存成功')
    # try:
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"}
    #     pre_content_length = 0
    #     # 循环接收视频数据
    #     while True:
    #         # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
    #         if os.path.exists(path):
    #             headers['Range'] = 'bytes=%d-' % os.path.getsize(path)
    #         res = requests.get(url, stream=True, headers=headers)
    #
    #         content_length = int(res.headers['content-length'])
    #         # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
    #         if content_length < pre_content_length or (
    #                 os.path.exists(path) and os.path.getsize(path) == content_length):
    #             break
    #         pre_content_length = content_length
    #
    #         # 写入收到的视频数据
    #         with open(path, 'ab') as file:
    #             file.write(res.content)
    #             file.flush()
    #             print('receive data，file size : %d  total size:%d' % (os.path.getsize(path), content_length))
    # except Exception as e:
    #     print(e)

# def load_media():
#     url='http://ese6a7b7c8d5ti-pub.pub.qiqiuyun.net/67785/b54d7382cb8c46b79172f3900d85c08e/ltisv86nsWg3xBWw-merged-hd.mp4'
#     path=r'D:\Down\1.mp4'
#
#     print('下载视频-----URL'+url+'名称为'+path)
#     do_load_media(url, path)
#     pass
