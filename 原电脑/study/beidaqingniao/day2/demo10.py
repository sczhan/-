lt1 = [1, 5, 9, 8]
# 引用
lt2 = lt1
print(lt2)
lt1[0] = 100
print(lt2)

# 复制
lt4 = [1, 5, 9, 8]
lt3 = lt4[:]
print(lt3)
lt4[0] = 200
print(lt3, lt4)
lt3[1] = 500
print(lt3, lt4)