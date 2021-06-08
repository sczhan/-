def hanoi_tower(disk: int = 3, start: str = "A", target: str = "B", middle: str = "C"):    # n盘子数量（默认值：3）、起始柱（默认值：“A”）、目标柱（默认值：“B”）和过渡柱（默认值：“C”）的名
    if disk == 1:
        print(f"第{disk}盘子, 从{start} --> {target}")                 # 从起始柱a --> 目标柱 b
    else:
        hanoi_tower(disk - 1, start, middle, target)           # 将n -1 的盘子 从起始柱a 借助目标柱 b --> 过渡柱 c
        print(f"第{disk}盘子, 从{start} --> {target}")                 # 将最下面的盘子从起始柱a --> 目标柱 b
        hanoi_tower(disk - 1, middle, target, start)           # 将n -1 的盘子 从过渡柱 c 借助起始柱a --> 目标柱 b

#
# def hanoi_tower2(n=3, a="A", c="C", b="B"):
#     if n == 1:
#         print(f"{a} --> {b}")
#     else:
#         hanoi_tower2(n - 1, a, b, c)
#         print(f"{a} --> {b}")
#         hanoi_tower2(n - 1, c, a, b)


if __name__ == '__main__':
    hanoi_tower(3)
    # hanoi_tower2(3)


