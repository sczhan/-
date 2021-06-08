import math
nums = int(input("请输入一个数"))


def square_root(num):
    if num <= 0:                                  # 判断输入的数是否小于等于0
        absolute_num = abs(num)                   # 转化成绝对值
        num_square_root = complex(0, math.sqrt(absolute_num))  # 求平方根
        print("{} 的平方根是: {}".format(absolute_num, num_square_root))   # 输出
    else:
        num_square_root = math.sqrt(num)              # 求平方根
        print("{} 的平方根是: {}".format(num, num_square_root))  # 输出


square_root(nums)


