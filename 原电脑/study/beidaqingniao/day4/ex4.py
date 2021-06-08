for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:     # 不满足的话执行 else
            break          # 执行break 不执行 else,
    else:
        print(i)           # 打印质数
