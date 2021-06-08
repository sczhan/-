lt = [3, 5, 8, 9]
lt2 = [i * 10 for i in lt]
print(lt, lt2)
# for i in lt:
#   lt2.append(i * 10)

# 产生1-10的列表
lt3 = [i for i in range(1, 11)]
print(lt3)

# 产生1-10之间的偶数列表
lt4 = [i for i in range(1, 11) if i % 2 == 0]
print(lt4)


# for i in range(1, 11):
#   if i % 2 == 0:
#       lt4.append(i * 10)

