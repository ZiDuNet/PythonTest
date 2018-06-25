# -*- coding: utf-8 -*-
"""
IDE:               PyCharm Community Edition
-------------------------------------------------
   Project Name:   PythonTest
   File Name：     ZiFuChuan
   Description :
   Author :       Admin
   date:          2018-06-25
-------------------------------------------------
   Change Activity:
                   2018-06-25:
-------------------------------------------------
"""
__author__ = 'Admin'
################################访问字符串中的值
var1='wushuo'
var2='自渡自渡自渡自渡自渡'
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5]) # 切片加索引
###############################更新字符串
print ("Updated String :- ", var1[:6] + '你好呀')
################################转义字符串
#反斜线符号	十六进制字符	描述/说明
#\a	0x07	铃声或警报
#\b	0x08	退格
#\cx		Control-x
#\C-x		Control-x
#\e	0x1b	Escape
#\f	0x0c	换页
#\M-\C-x		Meta-Control-x
#\n	0x0a	新一行
#\nnn		八进制符号，其中n在0.7范围内
#\r	0x0d	回车返回
#\s	0x20	空格
#\t	0x09	制表符
#\v	0x0b	垂直制表符
#\x		字符x
#\xnn		十六进制符号，其中n在0~9，a~f或A~F范围内
################################字符串特殊运算符
#+	连接 - 将运算符的两边的值添加	a + b 结果为 HelloPython
print(var1+var2)
#*	重复 - 创建新字符串，连接相同字符串的多个副本	a*2 结果为 HelloHello
print(var1*3)
#[]	切片 - 给出指定索引中的字符串值，它是原字符串的子串。	a[1] 结果为 e
print(var1[2])
#[:]	范围切片 - 给出给定范围内的子字符串	a[1:4] 结果为 ell
print(var1[1:3])
#in	成员关系 - 如果给定字符串中存在指定的字符，则返回true	'H' in a 结果为 1
print('w'in var1)
#not in	成员关系 - 如果给定字符串中不存在指定的字符，则返回true	'Y' not in a 结果为 1
print('w'not in var1)
#r/R	原始字符串 - 抑制转义字符的实际含义。原始字符串的语法与正常字符串的格式完全相同，除了原始字符串运算符在引号之前加上字母“r”。 “r”可以是小写(r)或大写(R)，并且必须紧靠在第一个引号之前。	print(r'\n') 将打印 \n ，或者 print(R'\n') 将打印 \n，要注意的是如果不加r或R作为前缀，打印的结果就是一个换行。
print(r'\n')# 将打印 \n  print(R'\n') 将打印 \n 注意的是如果不加r或R作为前缀，打印的结果就是一个换行。

#%	格式 - 执行字符串格式化	请参见本文第5节
################################.字符串格式化运算符

print ("My name is %s and weight is %d kg!" % ('Maxsu', 73))#
print("我%(name)s是你%(name2)s" % {'name':'武硕','name2':'爸爸'})#词典
'''
编号	格式化符号	转换
1	%c	字符
2	%s	在格式化之前通过str()函数转换字符串
3	%i	带符号的十进制整数
4	%d	带符号的十进制整数
5	%u	无符号十进制整数
6	%o	八进制整数
7	%x	十六进制整数(小写字母)
8	%X	十六进制整数(大写字母)
9	%e	指数符号(小写字母’e‘)
10	%E	指数符号(大写字母’E‘
11	%f	浮点实数
12	%g	％f和％e
13	%G	％f和％E
其他支持的符号和功能如下表所列 -
编号	符号	功能
1	*	参数指定宽度或精度
2	-	左对齐
3	+	显示标志或符号
4	<sp>	在正数之前留空格
5	#	根据是否使用“x”或“X”，添加八进制前导零(‘0‘)或十六进制前导’0x‘或’0X‘。
6	0	使用零作为左边垫符(而不是空格)
7	%	‘%%‘留下一个文字“%”
8	(var)	映射变量(字典参数)
9	m.n.	m是最小总宽度，n是小数点后显示的位数(如果应用)
'''

################################.Unicode字符串
#1	capitalize()	把字符串的第一个字母转为大写
print(var1.capitalize())
#2	center(width, fillchar)	返回使用fillchar填充的字符串，原始字符串以总共width列为中心。
print (var1.center(40, 'a'))#以var1为核心向两边填充
#3	count(str, beg = 0,end = len(string))	计算字符串中出现有多少次str或字符串的子字符串(如果开始索引beg和结束索引end,则在beg~end范围匹配)。
print("我是字符串丫丫丫".count('丫',0,100))#查丫出现的次数
#5	encode(encoding = ‘UTF-8’,errors = ‘strict’)	返回字符串的编码字符串版本; 在错误的情况下，默认是抛出ValueError，除非使用’ignore‘或’replace‘给出错误。
str_加密=var2.encode("GBK")
print(str_加密)
#4	decode(encoding = ‘UTF-8’,errors = ‘strict’)	使用编码encoding解码该字符串。 编码默认为默认字符串encoding。
print(str_加密.decode(encoding="GBK", errors="strict"))
#6	endswith(suffix, beg = 0, end = len(string))	确定字符串或字符串的子字符串(如果启动索引结束和结束索引结束)都以后缀结尾; 如果是则返回true，否则返回false。

#7	expandtabs(tabsize = 8)	将字符串中的制表符扩展到多个空格; 如果没有提供tabize，则默认为每个制表符为8个空格。
#8	find(str, beg = 0 end = len(string))	如果索引beg和结束索引end给定，则确定str是否在字符串或字符串的子字符串中，如果找到则返回索引，否则为-1。
#9	index(str, beg = 0, end = len(string))	与find()相同，但如果没有找到str，则引发异常。
#10	isalnum()	如果字符串至少包含1个字符，并且所有字符均为数字，则返回true，否则返回false。
#11	isalpha()	如果字符串至少包含1个字符，并且所有字符均为字母，则返回true，否则返回false。
#12	isdigit()	如果字符串只包含数字则返回true，否则返回false。
#13	islower()	如果字符串至少包含1个字母，并且所有字符均为小写，则返回true，否则返回false。
#14	isnumeric()	如果unicode字符串只包含数字字符，则返回true，否则返回false。
#15	isspace()	如果字符串只包含空格字符，则返回true，否则返回false。
#16	istitle()	如果字符串正确“标题大小写”，则返回true，否则返回false。
#17	isupper()	如果字符串至少包含一个可变大小写字符，并且所有可变大小写字符均为大写，则返回true，否则返回false。
#18	join(seq)	将序列seq中的元素以字符串表示合并(并入)到具有分隔符字符串的字符串中。
#19	len(string)	返回字符串的长度
#20	ljust(width[, fillchar])	返回一个空格填充的字符串，原始字符串左对齐到总共width列。
#21	lower()	将字符串中的所有大写字母转换为小写。
#22	lstrip()	删除字符串中的所有前导空格
#23	maketrans()	返回在translate函数中使用的转换表。
#24	max(str)	从字符串str返回最大字母字符。
#27	replace(old, new [, max])	如果给定max值，则用new或最多最大出现替换字符串中所有出现的旧字符(old)。
#28	rindex( str, beg = 0, end = len(string))	与index()相同，但在字符串中向后搜索。
#29	rjust(width,[, fillchar])	返回一个空格填充字符串，原始字符串右对齐到总共宽度(width)列。
#30	rstrip()	删除字符串的所有尾随空格。
#31	split(str=	根据分隔符str(空格，如果没有提供)拆分字符串并返回子字符串列表; 如果给定，最多分割为num子串。
#32	splitlines( num=string.count(‘\n’)))”)	全部拆分字符串(或num)新行符，并返回每行的列表，并删除新行符。
#33	startswith(str, beg=0,end=len(string))	确定字符串或字符串的子字符串(如果给定起始索引beg和结束索引end)以str开头; 如果是则返回true，否则返回false。
#34	strip([chars])	对字符串执行lstrip()和rstrip()
#35	swapcase()	反转在字符串中的所有字母大小写，即小写转大写，大写转小写。
#36	title()	返回字符串的标题版本，即所有单词第一个字母都以大写开头，其余的都是小写的。
#37	translate(table, deletechars=	根据转换表STR(256个字符)，除去那些在del字符串转换字符串。
#38	upper()	将字符串中的小写字母转换为大写。
#39	zfill(width)	返回原始字符串，左边填充为零，总共有宽度(width)字符; 对于数字zfill()保留给定的任何符号(少于一个零)。
#40	isdecimal()	如果unicode字符串只包含十进制字符，则返回true，否则返回false
