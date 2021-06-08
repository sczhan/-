import copy
lt = [1, 5, 9, [100, 2]]
lt1 = lt                        # 引用
lt2 = lt[:]                     # 浅复制
lt3 = lt.copy()                 # 浅复制
lt4 = copy.deepcopy(lt)           # 深复制
# 集合中数据如果都是不可变类型, 则深. 浅复制效果相同
# 如果有可变类型,则深复制才是正确的复制操作
lt[0] = 100
lt[3][0] = 1
print(lt)
print(lt1)
print(lt2)
print(lt3)
print(lt4)