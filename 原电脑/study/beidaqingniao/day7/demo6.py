lt = [2, 5, 7]
lt2 = [1, 9]
lt.append(71)
# lt.append(lt2)
# print(len(lt))
print(lt)

lt.extend(lt2)
print(len(lt))
print(lt)

print(lt + lt2)
print(lt)

lt[len(lt):] = [10, 45, 78]
print(lt)

