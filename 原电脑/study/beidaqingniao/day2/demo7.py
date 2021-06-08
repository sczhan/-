
# 字符串格式化
s = "hell\to \nworld"
print(s)

s = r"he\tllo \\nworld"
print(s)
print("*"*20)

a = 10
b = 3.56
c = "hello"
d = 0x9fa5
# a = 10 b = .....c=...,d=..,
# c = char: A=65 a=97  0x4e00～0x9fa5
print("a=%d, b=%f, c=%s, d=%c" % (a, b, c, d))
print("a=%-5d, b=%-5.1f, c=%-10s, d=%-5c" % (a, b, c, d))
print("a={0}, b={1}, c={2}, d={3}".format(a, b, c, d), type(a), type(b), type(c), type(d))
# format方法
print("a={}, b={}, c={}, d={}".format(a, b, c, d))
