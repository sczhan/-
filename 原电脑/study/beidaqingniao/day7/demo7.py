lt = [4, 7, 8, 1, 10, 20]
lt.insert(2, 4)
print(lt)

# 根据数据的值删除
lt.remove(4)   # 数值
print(lt)
lt.remove(4)
print(lt.remove(8))

# 根据索引位置删除, 既可以是索引, 也可以是切片
del lt[2]    # 下标
print(lt)
# del lt[1:]    # 下标
# print(lt)

n = lt.pop()
print(n, lt)

lt.clear()
print(lt)
