# # # 算术运算符
# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % 3)
# print(a ** b)  # a的3次方
# print(a ** 3)
# print(a ** 1e1)
# print(a ** 10)
#
# # A%B : A-A//B*B
# print(10//-4)
# print(a % (-4))
# 已知有n 个男生, 入住4人间, 求需要几间房
n = input("请输入人数: ")
b = (int(n) + 4 - 1)//4
print("需要{}房间".format(b))