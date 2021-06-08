# is 运算符
a = [3, 6, 8]
b = a
c = a[:]
print(a is b)
print(a is c)
print("a: ", id(a))
print("b: ", id(b))
print("b: ", id(c))
print("*" * 20)

a = 265222
b = 265222
print("a: ", id(a))
print("b: ", id(b))
print("*" * 20)

a = 2565
b = a
print("a: ", id(a))
print("b: ", id(b))
print("*" * 20)


a = [3, 6, 8]
b = [3, 6, 8]
print("a: ", id(a))
print("b: ", id(b))