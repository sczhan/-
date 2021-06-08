s = input("请输入: ")
print("你输入的是: %s" % s)
# print("你输入的是: %d" % int(s)) d数字
print("你输入的是:", s)

# 输入内容都是字符串
s = input("请输入年龄: ")
# type函数用于查看数据类型
print(type(s))

# 使用int函数进行转换 (转换为整数)
age = int(s)
print(type(age))

# 使用float函数进行转换 (转换成浮点数)
s = input("请输入体重: ")
height = float(s)
print(type(height))


