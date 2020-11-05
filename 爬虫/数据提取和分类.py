# 数据提取概念和数据的分类
# 使用 json 模块提取数据
# 使用正则表达式提取数据
# 使用 xpath 提取数据
# 使用 beautifulsoup 提取数据
# json、csv 数据转换
#######如果是json或XML结构化数据通过 json 模块等直接转成 Python 数据类型
#######如果是html、word等非结构化数据，通过正则表达式 、 xpath 、beautifulsoup 等模块提取数据


# 导入模块
import json

# json.loads json字符串 转 Python数据类型
json_string = '''
{
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
'''
print("json_string数据类型：",type(json_string))
data = json.loads(json_string)
print("data数据类型：",type(data))
print(data)
print("*" * 100)
# json.dumps Python数据类型 转 json字符串
data = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
print("data数据类型：",type(data))
json_string = json.dumps(data)
print("json_string数据类型：",type(json_string))
print(json_string)

print("*"*100)
# json.load json文件 转 Python数据类型
with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)
    print("data数据类型：", type(data))
    print(data)

print("*"*100)
# json.dump Python数据类型 转 json文件
data = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
with open('data_out.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)