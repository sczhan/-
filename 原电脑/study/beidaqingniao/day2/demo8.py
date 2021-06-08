
# 列表的定义和简单使用
lt = [4, 9, 17, 65, 2]
print(lt[:])
print(lt[4])
print(lt[::-1])

# del指令
del lt[-1]
print(lt)

del lt[:2]
print(lt)

del lt
# 删除列表后必须再次定义后才能使用
# print(lt)
print("*"*20)
lt = [1, 2, 4, 23, 0]
print(len(lt))
print(max(lt))
print(min(lt))

name = ["mike", "tom", "jerry", "andy"]
print(max(name))
print(min(name))