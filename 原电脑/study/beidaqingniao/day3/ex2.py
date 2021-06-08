import math
π = math.pi
r = int(input("请输入半径: "))  # 输入半径
C = 2 * π * int(r)             # 计算周长
S = π * r ** 2                 # 计算面积
V = (4 / 3) * π * r ** 3       # 计算体积
print("这个圆的周长是{0}, \n面积是{1}, \n圆球的体积是{2}".format(C, S, V))   # 输出周长,面积, 体积