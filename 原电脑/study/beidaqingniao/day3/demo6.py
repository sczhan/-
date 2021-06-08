# 逻辑运算
a = True
b = True
print(a and b)
print(a or b)
print(not a)
print("*" * 20)

b = False
print(a and b)
print(a or b)
print(not a)
print("*" * 20)

# 数字0表示False, 非0表示True
b = 0
print(a and b)  # 0
print(b and a)  # 0

b = 10
print(a and b)  # 10
print(b and a)  # True
print("*" * 20)

# 空字符串(str), 空列表(list), 空字典(dict), 空元组(tuple), 空集合(set)表示False, 非空表示True
b = "abc"
print(a and b)  # True
print(b and a)  # True
print("*" * 20)

b = ""
print(a and b)  # ""
print(b and a)  # ""
print("*" * 20)

b = []
print(a and b)  # []
print(b and a)  # []
print("*" * 20)


b = [1]
print(a and b)  # [1]
print(b and a)  # True
print("*" * 20)


b = ()
print(a and b)  # ()
print(b and a)  # ()
print("*" * 20)


b = (1, )
print(a and b)  # (1,)
print(b and a)  # True
print("*" * 20)

