def accept_int(min_m=0, max_m=2 ** 31 - 1):
    while True:
        try:
            a = int(input("请输入整数: "))
            if min_m <= a <= max_m:
                return a
            print("输入不合法,请重新输入\n")
        except ValueError as e:
            print("输入不合法")


if __name__ == "__main__":
    accept_int(4, 40)