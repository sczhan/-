# 空元组
tp = ()
print(type(tp))

# 单个数据定义元组是需加 ","
tp = (3)
print(type(tp))
tp = (3,)
print(type(tp))

# 多个数据末尾无需加
tp = (2, 8, 9, 4)
print(type(tp))
print(tp[2])
print(tp[1:-1])


# 元组不能修改是不可变类型, 字符串也是不可变类型
# tp[0] = 100
# 通过与list转换以进行修改
lt = list(tp)
print(lt, type(lt))
lt[0] = 200
tp = tuple(lt)
print(tp, type(tp))

print(max(tp), min(tp), len(tp))


# s = "sjkhssdj123"
# import re
# c = re.compile(r"\d+")
# ss = c.findall(s)
# a = "123456"
# ass = re.sub(ss[0], a, s)
# print(ss)
# print(ass)