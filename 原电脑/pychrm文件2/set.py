
# # 集合序列操作
# # 成员检测
# a = {4, 5, "love", "you", "刘梦"}
# # a是一个集合 ,无序
# print(a)
# if "love" in a:
#     print("刘梦")
# else:
#     print("不爱")

# # 集合的遍历操作
# a = {4, 5, "love", "you", "刘梦"}
# for i in a:
#     print(i, end=" ")

# # 带有元组的集合遍历
# s = {(1, 2, 3, 9), ("l", "love", "you", "刘梦"), (4, 5, 45, 56)}
# for a, b, c, d, in s:
#     print(a, '--', b, '==', c, '***', d)
# for m in s:
#     print(m)

# # 集合的内涵
# # 普通集合的内涵
#
# # 以下集合在初始化后自动过滤掉重复元素
# s = {12, 21, 3, 4, 5, 6, 7, 1, 3, 5, 1, 2, 1}
# print(s)
# ss = {i for i in s}
# print(ss)
# # 带条件的集合内涵
# sss = {m for m in s if m % 2 == 0}
# print(sss)

# # 多循环的集合内涵
# s = {i for i in range(1, 5)}
# ss = {'i', 'love you', '刘梦 '}
# sss = {i*j for i in s for j in ss if i == 2}
# print(sss)
#
# # 集合函数/关于集合的函数
# # len  max min 跟其他基本函数一致
# s = {1, 2, 1, 3}
# # 过滤了重复的
# print(len(s))
# print(max(s))
# print(min(s))
#
#
# # set生成一个集合
# k = ['m', 'p', 1]
# o = set(k)
# print(o)
#
# # add向集合内添加元素
# s = {1}
# s.add(255)
# print(s)
#
# # clear
# s = {1, 2}
# print(id(s))
# s.clear()
# print(id(s))
# # 结果表明clear函数是原地清空数据

# # copy拷贝
# # remove 移除指定的值,直接改变原有值,如果要删除的不存在,报错
# # discard 移除集合中指定的值,和remove一样,但是删除的值不存在,不报错
# s = {1, 2}
# print(s)
# ss = s.copy()
# print(ss)
# print("*"*20)
# s.remove(2)
# print(s)
# print("*"*20)
# s.discard(2)
# print(s)
# print("*"*20)
# s.remove(2)  # 报错了
# print(s)

# # pop随机移除一个元素
# # s = {1, 2, 3, 4}
# # a = s.pop()
# # print(a)
# # print(s)

# # 集合函数
# # intersection:交集
# # difference:差集
# # union:并集
# # issubset: 检查一个集合是否为另一个子集
# # issuperset: 检查一个集合是否为另一个超集
# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {5, 6, 7, 8, 9}
# s7 = {1,3}
# s3 = s1.intersection(s2)
# print(s3)
# s4 = s1.difference(s2)
# print(s4)
# s5 = s3.issubset(s1)
# print(s5)
# s8 = s1.issubset(s3)
# print(s8)
# s6 = s1.union(s2)
# print(s6)

# 集合的数学操作
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}
s_1 = s1 - s2
print(s_1)

# frozenset: 冰冻集合
# 创建
s = frozenset()
print(type(s))
print(s)


