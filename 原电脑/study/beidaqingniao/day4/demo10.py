side = int(input("请输入边长"))
# 实心的可以简化为以下语句
# print(("*  "*side + "\n") * side)
# for i in range(1, side + 1):
#     print("*  " * side)
# 空心图形
# for n in range(side):
#     if n == 0 or n == side - 1:
#         print("* "*side)
#     else:
#         print("* " + "  "*(side - 2) + "*")

# 空心平行四边形
# for n in range(side):
#     if n == 0 or n == side - 1:
#         print("  "*(side - n - 1) + "*  "*side)
#     else:
#         print("  "*(side - n - 1) + "*  " + "   "*(side - 2) + "*  ")

# 空心三角形
#     *
#   *  *
# *  *  *
# for n in range(1, side + 1):
#     m = 1
#     if n == 1:
#         print("  "*(side//2) + "* ")
#     elif n == side:
#         print("* "*side)
#     else:
#         print("  "*(side//2 - m) + " * " + "  "*(n - 1) + "*")
#         m += 1

for i in range(1, side + 1):
    if i == 1:
        print(" " * (side - 1) + "*")
    elif i == side:
        print("* " * side)
    else:
        print(" " * (side - i) + "* " + " " * (i + i - 4) + "*")




