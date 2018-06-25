# -*- coding: utf-8 -*-
"""
IDE:               PyCharm Community Edition
-------------------------------------------------
   Project Name:   PythonTest
   File Name：     ShuZi
   Description :
   Author :       Admin
   date:          2018-06-25
-------------------------------------------------
   Change Activity:
                   2018-06-25:
-------------------------------------------------
"""
import math
__author__ = 'Admin'
##################################数学函数     都可使用del删除某个元素
#abs(x)	x的绝对值，x与零之间的(正)距离。
print(abs(10),abs(-10))
#2	ceil(x)	x的上限，不小于x的最小整数。
print(math.ceil(-10.1221),math.ceil(9.612))
#3	cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 或者 如果 x > y 返回 1。在Python 3中已经弃用，可使用return (x>y)-(x<y)代替。
#4	exp(x)	x的指数，返回e的x次幂
print(math.exp(2))
#5	fabs(x)	x的绝对值。
print(math.fabs(-29.1),math.fabs(21.7))
#6	floor(x)	不大于x的最大整数。
print(math.floor(-45.8),math.floor(90.5))
#7	log(x)	x的自然对数(x > 0)。
print(math.log(20))
#8	log10(x)	以基数为10的x的对数(x > 0)。
print(math.log10(20))
#9	max(x1, x2,…)	给定参数中的最大值，最接近正无穷大值
print(max(1,4,6))
#10	min(x1, x2,…)	给定参数中的最小值，最接近负无穷小值
print(min(1,4,6))
#11	modf(x)	将x的分数和整数部分切成两项放入元组中，两个部分与x具有相同的符号。整数部分作为浮点数返回。
print(math.modf(1.123))#分别拆开整数与小数
#12	pow(x, y)	x的y次幂
print(pow(2,2))
#13	round(x [,n])	x从小数点舍入到n位数。round(0.5)结果为 1.0， round(-0.5) 结果为 -1.0
print(round(123.2),round(123.5),round(123.123,2))
#14	sqrt(x)	x的平方根(x > 0)。
print(math.sqrt(100))
##################################随机数函数三角函数
import random
#1	choice(seq)	来自列表，元组或字符串的随机项目。
print(random.choice(range(2,10)))
print(random.choice([1,2,3,4,5,6,7]))
#2	randrange ([start,] stop [,step])	从范围(start(起点), stop（终点）, step（跳跃）)中随机选择的元素。
print(random.randrange(1,6,2))
#3	random()	返回随机浮点数r(0 <= r < 1)
print(random.random())
#4	seed([x])	设置用于生成随机数的整数起始值。在调用任何其他随机模块功能之前调用此函数，返回None。
#带本函数的话随机值会一样
a=0
random.seed(1)
print(random.random())
random.seed(1)
print(random.random())
random.seed(1)
print(random.random())
#5	shuffle(lst)	将列表的项目随机化到位置。 返回None。
#随机排列
list=[1,2,3,4,5,6]
random.shuffle(list)
print(list)
random.shuffle(list)
print(list)
#6	uniform(x, y)	返回随机浮点数 r (x <= r < y)。
print(random.uniform(2,6))
##################################三角函数
print("----------------三角函数--------------")
#1	acos(x)	返回x的弧余弦值，以弧度表示。
print(math.acos(0.21))
#2	asin(x)	返回x的弧线正弦，以弧度表示。
print(math.asin(0.21))
#3	atan(x)	返回x的反正切，以弧度表示。
print(math.atan(0.21))
#4	atan2(y, x)	返回atan(y / x)，以弧度表示。
print(math.atan2(0.21,1))
#5	cos(x)	返回x弧度的余弦。
print(math.cos(1))
#6	hypot(x, y)	返回欧几里得规范，sqrt(x*x + y*y)
print(math.hypot(1,2))
#7	sin(x)	返回x弧度的正弦。
print(math.sin(1))
#8	tan(x)	返回x弧度的正切值。
print(math.tan(1))
#9	degrees(x)	将角度x从弧度转换为度。
print(math.degrees(1))
#10	radians(x)	将角度x从角度转换为弧度。
print(math.radians(1))
##################################数学常数
#pi e
