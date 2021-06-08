#
# # dict 字典
# # 字典是一种组合数据,没有顺序的组合数据,数据已键值对形式出现
# # dict字典的创建
#
# # 创建空字典
# a = {}
# print(type(a))
# print(a)
# b = dict()
# print(b)
#
# # 创建有值的字典, 每一组数据用冒号隔开, 每一对键值对用逗号隔开
# a = {"one": 1, "two": 2}
# print(a)
# a = dict({"one": 1, "two": 2})
# print(a)
#
# # 利用关键字参数
# a = dict(one=1, two=2)
# print(a)
#
# # 利用元组
# a = dict([("one", 1), ("two", 2)])
# print(a)

# 字典的特征
# 1.字典是序列类型,但是是无序序列,没有分片和索引
# 2.字典中的数据每个都有键值对组成,即kv对,key,value
# key:必须是可哈希的值,比如 int,string,float,tuple,但是list, set, dict 不行
# value:任何值

# 字典常见操作
# 访问数据
# a = {"one": 1, "two": 2}
# # 中括号内是键值
# print(a["one"])
#
#
# a["one"] = "55"
# print(a)
#
# # 删除某个操作
# # 使用del操作
# del a["one"]
# print(a)

# # 成员检测 in / not in
# # 成员检测检测的是key内容
# a = {"one": 1, "two": 2}
# if 2 in a:
#     print("value")
# if "two" in a:
#     print("key")
# if ("two", 2)in a:
#     print("kv")

# # 按key值使用for循环
# a = {"one": 1, "two": 2}
# # 第一种:使用for循环访问,直接按key值访问
# for k in a:
#     print(k, a[k])
#
# # 第二种: 使用keys()
# for key in a.keys():
#     print(key, a[key])
# # 访问值
# for value in a.values():
#     print(value)
#
#
# for k, v in a.items():
#     print(k, v)

# # 字典生成式
# a = {"one": 1, "two": 2}
# b = {k: v for k, v in a.items()}
# print(b)
#
# # 加限制条件的字典生成式
# a = {"one": 1, "two": 2}
# b = {k: v for k, v in a.items() if v % 2 == 0}
# print(b)

# # 字典的函数
# # 通用函数 len,max min dict
# # str(字典)返回字典的字符串格式
# a = {"one": 1, "two": 2}
# print(max(a))
# print(min(a))
# print(len(a))
# print(str(a))

# clear: 清空字典
# items: 返回字典的键值对组成的元组格式
a = {"one": 1, "two": 2}
a.clear()
print(a)

a = {"one": 1, "two": 2}
b = a.items()
print(type(b))
print(b)

# keys: 返回字典的键组成的一个结构,可迭代的结构
a = {"one": 1, "two": 2}
c = a.keys()
print(type(c))
print(c)

# values: 返回字典的值组成的一个结构,可迭代的结构
a = {"one": 1, "two": 2}
c = a.values()
print(type(c))
print(c)

# get: 根据制定键返回相应的值, 好处是, 可以设置默认值
a = {"one": 1, "two": 2}
print(a.get("one1"))
# get 默认值是None ,可以设置
print(a.get("one", 100))
print(a.get("one11", 100))
# 体会一下代码跟上面代码的区别
# print(a["one1"])  # 报错

# fromkeys: 使用指定的序列作为建,使用一个值作为字典的所有的键的值
p = ["wo", 'kk', 'll']
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主体
gg = dict.fromkeys(p, '刘梦')
print(gg)

