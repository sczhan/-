# range函数的用法
# 1. 产生[0, N)的数字序列
for i in range(3):
    print(i)
print("*" * 20)

# 2. 产生[M, N)的数字序列
for i in range(3, 8):
    print(i)
print("*" * 20)


# 3. 产生[M, N)的数字序列,且间隔为T的数字序列
for i in range(3, 20, 5):
    print(i)
print("*" * 20)

for i in range(1, 10):
    for j in range(1, i+1):
        print(i * j, end=" ")
    print()
