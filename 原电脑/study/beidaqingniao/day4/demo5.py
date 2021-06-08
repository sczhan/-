score = [78, 56, 45, 98, 85]
while True:
    sn = int(input("请输入学号: "))
    if 0 < sn <= len(score):
        break
    else:
        print("输入不合法")

print(score[sn - 1])