height = int(input("请输入身高(cm): "))   # 输入身高
wage = int(input("请输入薪水(元): "))     # 输入薪资
area_house = int(input("请输入房屋面积(平方): "))  # 输入房屋面积

if height >= 180 and wage >= 15000 and area_house >= 120:   # 判断
    print("你条件很好，我们见个面吧")
elif height >= 180 and wage >= 15000:
    print("虽然你房屋不够，但我们还是可以先见个面")
elif height >= 180 and area_house >= 120:
    print("虽然你薪资不够，但我们还是可以先见个面")
elif wage >= 15000 and area_house >= 120:
    print("虽然你身高不够，但我们还是可以先见个面")
elif height >= 180:
    print("你的薪资、房屋条件达不到我的要求")
elif wage >= 15000:
    print("你的身高、房屋条件达不到我的要求")
elif area_house >= 120:
    print("你的身高、薪资条件达不到我的要求")
else:
    print("你的身高、薪资、房屋条件达不到我的要求")