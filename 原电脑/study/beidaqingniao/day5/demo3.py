# math模块的函数
import math
# 查看模块里面的内容: 函数和数据
# help("math")

# 平方根
a = math.sqrt(16)
print(a)
print("*" * 20)

# 角度转弧度
a = math.radians(180)
print(a, math.pi)
print("*" * 20)

# 正弦函数
a = math.sin(math.radians(30))
print(a)
print("*" * 20)

# 弧度转角度
a = math.degrees(math.pi)
print(a)
print("*" * 20)

# 向上取整
a = 2.4556
print(math.ceil(a))
print("*" * 20)

# 向下取证
print(math.floor(a))
print("*" * 20)

# 四舍五入
print(round(a))
print("*" * 20)

# 求n次方
a = 3
print(math.pow(a, 3), a ** 3)
print("*" * 20)

# 最大公约数
print(math.gcd(12, 4))