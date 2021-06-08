score = [78, 56, 45, 98, 85, 65, 53]
for sc in score:
    if sc >= 90:
        print("优秀")
    elif sc >= 70:
        print("良")
    elif sc >= 60:
        print("中")
        break
    else:
        continue
        # print("差")
else:
    print("end")

