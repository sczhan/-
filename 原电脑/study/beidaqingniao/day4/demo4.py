a = 1
# while a < 10:
#     print(a)
#     a += 1
# else:
#     print("end while")

# while True:
#     print(a)
#     a += 1
#     if a == 10:
#         break
# else:           # 无效的语句
#     print("end while")

while a < 10:
    if a % 2 == 0:
        print(a)
        a += 1
        continue
    a += 1
else:
    print("end while")