# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divvide by zero")
# print("除法")
# while True:
#     frist_number = input("输入第一个数字")
#     if frist_number == 'q':
#         break
#     second_number = input("输入第二个数字")
#     try:
#         answer = int(frist_number) / int(second_number)
#     except ZeroDivisionError:
#         print("you can't divide by 0")
#     else:
#         print(str(answer)+'\n')
# c = "alice.txt"
# try:
#     with open(c) as b:
#         a = b.read()
#         # print(a)
# except FileNotFoundError:
#     print("Sorry, the file " + c + "does not exist")
# else:
#     f = a.split()
#     h = len(f)
#     print(h)
# e = "Alice  in  Wonderland"
# print(e.split())


# def count_words(filename):
#     '''
#     计算一个文件大约有多少个单词
#     param filename: 文件名
#     '''
#     try:
#         with open(filename) as a:
#             b = a.read()
#     except FileNotFoundError:
#         '''失败的时候一声不吭 pass'''
#         print("Sorry, the file " + filename + "does not exist")
#         pass
#     else:
#         c = b.split()
#         d = len(c)
#         print("The  file" + filename + "has about " + str(d))
#
#
# filename = ["F:\wang.txt", "F:\yong.txt", "F:\zhan.txt", "F:\wangyongzhan.txt"]
# for filenames in filename:
#     count_words(filenames)



# print("10-7")
# while True:
#     try:
#         first_number = input("请输入一个数字")
#         if first_number == 'q':
#             break
#         first_number = int(first_number)
#         second_number = input("请输入第二个数字")
#         if second_number == 'q':
#             break
#         second_number = int(second_number)
#     except ValueError:
#         print("请输入数字,而不是文本\n")
#     else:
#         value = first_number + second_number
#         print(value)

# print("10-8")
#
#
# def name(filename):
#     '''
#     打印文本中的内容
#     :param filename: 文件名
#     '''
#     try:
#         with open(filename) as a:
#             names = a.read()
#             print(names)
#     except FileNotFoundError:
#         pass
#         # print("文件" + filename + "不存在")
#
#
# filename = ["F:\wang.txt", "F:\yong.txt"]
# for filenames in filename:
#     name(filenames)


print("10-10")


# def word(filename):
#     try:
#         with open(filename) as a:
#             words = a.read()
#             wordthe = a.readline()
#     except FileNotFoundError:
#         print("文件" + filename + "未找到")
#     else:
#         wordshu = words.split()
#         wordshus = len(wordshu)
#         e = words.count("l")
#         f = words.lower().count("l")
#         print("文件" + filename + "中有l单词 " + str(e))
#         print("文件" + filename + "中有l单词 " + str(f))
#
#
# filename = "F:\wang.txt"
# word(filename)

#
# x = 0
#
#
# def fun():
#     global x
#     x += 1
#     if x <= 10 and x % 2 == 0:
#         print(x)
#     if x > 11:
#         return print("结束")
#     return fun()
#
#
# fun()


# a = [1, 2, 3]
# print(id(a))
# del a[1]
# print(id(a))
# a.clear()
# print(id(a))

# a = [1, 2, 3]
# print(a)
# print(id(a))
# a.reverse()
# print(a)
# print(id(a))

# a = [1, [2, 5], 2, 3, 5]
# print(a)
# b = a.copy()
# print(id(a))
# print(id(b))
# print(id(a[1]))
# print(id(b[1]))
# a[1].append(8)
# a[2] = 555
# print(a)
# print(id(a))
# print(b)
# print(id(b))

# import copy
# a = [1, [2, 5], 2, 3, 5]
# print(a)
# b = copy.deepcopy(a)
# a[1].append(8)
# a[2] = 555
# print(a)
# print(id(a))
# print(b)
# print(id(b))
#
#
# a = [1, 2, 3, 5]
# print(a)
# b = a.copy()
# a.append(8)
# a[1] = 888
# print(a)
# print(id(a))
# print(b)
# print(id(b))

# t = ()
# print(type(t))
# t = 1,
# print(type(t))
# t = (1,)
# print(type(t))
# t = (1, 2, 3, 4)
# print(type(t))
# t = 1, 2, 3, 4
# print(type(t))


t = (1, 2, 3, 4)
t1 = (4, 6)
t += t1
"""
这里的t相当于新创建的一个对象,没有修改元组的内容
元组的内容不可修改
t[1] = 100  会报错
"""
print(t)


t = (1, 2, 3, 4)
t *= 2
"""
这里的t相当于新创建的一个对象,没有修改元组的内容
元组的内容不可修改
t[1] = 100  会报错
"""
print(t)

t = (1, 2, 3, 4)
if 2 in t:
    print("yes")
else:
    print("no")

t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for i in t:
    for m in i:
        print(m, end='  ')
    print()


for k, w, m in t:
    print(k, '--', w, '--', m)

d = {}
r = {1}
c = set()
c = {1, 2, 3}
print(type(d))
print(type(c))
print(type(r))
print(d)
print(c)
print(r)

x = 2
x **= 3
print(x)



