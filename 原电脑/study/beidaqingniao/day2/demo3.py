# 整数和浮点数的表示方式
a = 10
print(a)

a = 0b10
print(a)

a = 0o10
print(a)

a = 0x10
print(a)

b = 3e2
print(b)
print(type(b))

c = 3.14e1 + .05e2
print(c)

def biao():
    for i in range(1, 10):
        for j in range(1, i+1):
            if i == 2 and j == 2:
                print(" " + str(i*j), end=" ")
            elif i == 3 and j == 2 or j == 3:
                print(" " + str(i*j), end=" ")
            elif i == 4 and j == 2:
                print(" " + str(i*j), end=" ")
            else:
                print(i*j, end=" ")
        print()

biao()