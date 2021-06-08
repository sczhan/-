# 赋值运算符
a = 10
b = 5
a += b  # a = a+b
print(a)
# 交换 a与 b
# temp = a
# a = b
# b = a
a, b = b, a
print(a, b)

# 包装 (pack)操作, 包装成元组
c = a, b, 15
print(type(c), c)

# 解包(unpack)操作, 变量和数据要一致
lt = [1, 3, 5]
a, b, c = lt
print(a, b, c)
a += 1
print(a)

 