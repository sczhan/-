a = 10
b = 5
print(a > b)
print(a < b)

a = "10"
b = "5"
print(a > b)
print(a < b)

a = 10
# 不能直接比较数字和字符串
# print(a < b)
print(a < int(b))