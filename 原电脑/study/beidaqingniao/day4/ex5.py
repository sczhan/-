# c = 0
# # for cock in range(1, 20):                    # 公鸡最多买20只
# #     for hen in range(1, 30):                # 母鸡最多买33只
# #         c += 1
# #         biddy = 100 - cock - hen                   # 小鸡的个数
# #         if 5 * cock + 3 * hen + biddy/3 == 100:    # 是否满足总价格
# #             print("公鸡的个数为{0}, \n母鸡的个数为{1},\n小鸡的个数为{2}\n".format(cock, hen, biddy))    # 输出
# # print(c)

for cock in range(1, 15):
    remain = (100 - cock * 5) // 3
    for hen in range(1, remain):
        biddy = (100 - cock * 5 - hen * 3) * 3
        if cock + hen + biddy == 100:
            print("公鸡的个数为{0}, \n母鸡的个数为{1},\n小鸡的个数为{2}\n".format(cock, hen, biddy))