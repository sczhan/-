import math


def distance(coordinate1, coordinate2=(0, 0)):     # 两个点 一个有默认值(0,0)
    dis = math.sqrt((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2)  # 计算两点距离
    print("两点距离: %.4f" % dis)                 # 打印


distance((2, 2))
distance((2, 2), (8, 2))

