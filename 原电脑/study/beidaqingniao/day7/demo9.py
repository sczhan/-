lt = [4, 7, 9, 1, 65, 9]
print(lt)
lt.sort()
print(lt)

names = ["mike", "Tom", "jerry"]
names.sort()
print(names)
names.sort(key=lambda n: n.lower())
print(names)

names.sort(key=lambda n: n.lower(), reverse=True)
print(names)


lt = ["4", "7", "9", "1", "65", "9"]
lt.sort()
print(lt)
lt.sort(key=lambda n: int(n))
print(names)