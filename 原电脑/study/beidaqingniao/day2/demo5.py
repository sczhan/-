
s = "hello,world"
print(s[5])
print(s[-1])

t = s[:]
print(t)

t = s[:-1]
print(t)

t = s[6:-1]
print(t)

t = s[-11:20]
print(t)

t = s[1:100]
print(t)

# 切片操作还允许指定切片间隔和方向
v = s[::-2]
print(v)
print("*"*20)

m = s[::-1]
n = s[::1]
print(m)
print(n)
print("*"*20)

# 判断一个用户输入是否是回文
b = input("请输入一句话: ")
a = b[::-1]
print(a, b)
print(a == b)



