lt = [5, 8, 9, 10]
# 迭代器 iterator
it = iter(lt)
print(type(it))
print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
while True:
    try:
        print(next(it))
    except StopIteration as e:
        break

print("end of code")