def accept_int(min=0, max=2 ** 31 -1):
    while True:
        try:
            a = int(input("请用户输入整数: "))
            if min <= a <= max:
                return a
            print("输入不合法,请重新输入\n")
        except ValueError as e:
            print("输入不合法")


if __name__ == "__main__":
    accept_int(4, 40)
# while True:
#     side = input("请输入菱形边长: ")       # 提示输入
#     try:
#         side = int(side)                   # 判断side是否合法
#         if side >= 3:
#             for i in range(1, side * 2):   # 打印 边长为side的菱形
#                 if i <= side:
#                     print("  " * (side - i) + " *  " * i)
#                 else:
#                     print("  " * (i - side) + " *  " * (side * 2 - i))
#             break                              # 结束循环
#         else:
#             print("输入不合法,请重新输入\n")   # 输入不合法
#     except ValueError as e:
#         print("输入不合法,请重新输入\n")       # 输入不合法
