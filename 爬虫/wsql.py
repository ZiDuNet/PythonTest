# 数据库类
import pymysql


def insert(value):
    db = pymysql.connect(host='IP', user='shuju2', password='shuju2', port=3306, db='shuju2')
    cursor = db.cursor()
    sql = "INSERT INTO shuju1(大标题, 章节, 章节URL,视频mp4,课件,课件URL) values (%s,%s,%s,%s,%s,%s)"
    print('插入语句为'+sql)
    try:
        cursor.execute(sql, value)
        db.commit()
        print('插入数据成功')

    except:
        db.rollback()
        print("插入数据失败")
    db.close()


def update(ksname, path):
    db = pymysql.connect(host='39.106.127.121', user='shuju2', password='shuju2', port=3306, db='shuju2')
    cursor = db.cursor()
    sql = 'UPDATE shuju1 SET 是否下载 = '+path+'WHERE 章节 = '+ksname
    print('修改语句为'+sql)
    try:
        cursor.execute(sql, value)
        db.commit()
        print('修改数据成功')

    except:
        db.rollback()
        print("修改数据失败")
    db.close()
