for i in range(100, 1000):
    hundreds_num = i // 100                          # i 的百位数
    ten_num = i // 10 % 10                           # i 的十位数
    ge_num = i % 10                                  # i 的个位数
    if i == hundreds_num ** 3 + ten_num ** 3 + ge_num ** 3:    # 判断满足水仙花
        print(i)                          # 输出水仙花
