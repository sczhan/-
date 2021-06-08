# print("\"")
# temp = input("请输入数字: ")
# if temp.isdigit():
#     temp = int(temp)
#     if 1<=temp<=100:
#         print('1')
#     else:
#         print("11丑八怪")
# else:
#     print("丑八怪")
# year = input("请输入年份: ")
# if year.isdigit():
#     year = int(year)
#     if year % 4 ==0:
#         print(str(year)+"是闰年")
#     else:
#         print(str(year)+"不是闰年")
# else:
#     print("输入年份")
# import random
# s = random.randint(1, 100)
# times = 3
# while times:
#     num = input("请输入数字")
#     if num.isdigit():
#         a = int(num)
#         if a == s:
#             print("你才对了")
#             break
#         elif a < s:
#             print("你猜的数字太小了")
#             times = times - 1
#         else:
#             print("数字太大了")
#             times = times - 1
#     else:
#         print("输入数字")
# print(s)
# a = range(0, 101)
# for i in a:
#     if i % 2 != 0:
#         print(i)
#     else:
#         pass
# x = 0
# while x < 200:
#     if (x % 2 == 1) \
#     and (x % 3 == 2) \
#     and (x % 5 == 4) \
#     and (x % 6 == 5) \
#     and (x % 7 == 0):
#         print(x)
#         x += 1
#         #break
#
#     else:
#         x += 1
# print("结束")
# password = 'abc'
# times = 3
# while times:
#     mima = input("请输入密码:")
#     if '*' in mima:
#         print("密码中不能输入*")
#     else:
#         if mima == password:
#             print("密码正确")
#             break
#         else:
#             print("密码错误")
#             times = times - 1
# print()
#
# with open("yuan.txt") as  yuanzhou :
#     b = yuanzhou.read()
#     print(b.rstrip())
# a = 5.0
# bb = 5
# c = a is bb
# f = id(a) == id(b)
# d  = a == bb
# print(c)
# print(d)
# print(f)
# a = "F:\新建文件夹 (3)\yuan\yuan.txt"
# with open(a) as  yuanzhou:
#     b = yuanzhou.read()
#     print(b.rstrip())
# c = "F:\新建文件夹 (3)\yuan\yuan.txt"
# with open(c) as yuan:
#     for fs in yuan:
#         print(fs.rstrip())
# c = "F:\新建文件夹 (3)\yuan\yuan.txt"
# with open(c) as yuan:
#     f = yuan.readlines()
# a = ''
# for fs in f:
#     a += fs.strip()
# #     a +=  fs.rstrip()
# # print(a.rstrip())
# print(len(a))
# print(a.strip())

with open("yuan.txt") as  yuanzhou :
    b = yuanzhou.readlines()
a = ''
for bs in b:
    a += bs.strip()
print(a[:52] + "....")
birth = input("请输入生日")
if birth in a:
    print("在")
else:
    print("不在")
print('你的生日'+str(birth))
# print(a[:52] + "....")