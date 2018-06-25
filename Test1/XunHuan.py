# -*- coding: utf-8 -*-
"""
IDE:               PyCharm Community Edition
-------------------------------------------------
   Project Name:   PythonTest
   File Name：     XunHuan
   Description :
   Author :       Admin
   date:          2018-06-25
-------------------------------------------------
   Change Activity:
                   2018-06-25:
-------------------------------------------------
"""
__author__ = 'Admin'
##############################################1.while循环
a=0
while (a<10):
    print(a)
    a+=1
else:
    print("结束")

##############################################2.for循环
#数字迭代
#1
for var in list(range(0,5)):
    print(var)
#2
aaa=['我','babna','sasa','sasde','qwqr','dfgfd','adasd','hgfhgf']
for bbb in  aaa:
    print(bbb)
#3
for ccc in 'wushuo':
    print(ccc)
#4按下标迭代
for ddd in range(len(aaa)):
    print(aaa[ddd],ddd)
#嵌套for(break和continco，pass(站位))
for i in range(1,100):
    for j in range(1,100):
        k=i*j

        if k==79:
            break#跳出整体循环
        else:
            print(k , end=' ')
    print()
print("-----------------------------------------------------")
for i in range(1,100):
    for j in range(1,100):
        k=i*j

        if k==79:
            continue#跳出本次循环
        print(k , end=' ')
    print()
##############################################迭代器和生成器iter()和next()
list=[1,2,3,4]
print("第一种",iter(list))
print("第二种",next(iter(list)))
for x in list:
    print(x)
