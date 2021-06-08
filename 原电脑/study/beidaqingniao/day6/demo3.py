from functools import reduce
lt = [2, 5, 10, 6, 9]
# rt = []
# for n in lt:
#     if n % 2 == 0:
#         rt.append(n)

"""
Map：对每个项应用相同的步骤集，存储结果

Filter：应用验证条件，存储计算结果为 True 的项

Reduce：返回一个从元素传递到元素的值
"""
rt = filter(lambda n: n % 2, lt)
print(list(rt))

rt = filter(lambda n: n * 20, lt)
print(list(rt))

rt = reduce(lambda acc, n: acc + n, lt)
print(rt)
