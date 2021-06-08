for i in range(1, 10):                                        # 1 到 9 行
    for j in range(1, i + 1):                                 # 在i行  j的范围 1 到 i + 1
        print("%d*%d=%-2d" % (j, i, i * j), end=" ")
        # print("{0}*{1}={2}".format(j, i, i * j), end=" ")     # 打印 i * j
    print()                                                   # 换行
