# num = int(input("请输入一个整数: "))
# if num % 2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")


# num = input("请输入一个整数: ")
# a = num.isdigit()
# if a == False:
#     print("让你输入数字, 听不懂人话啊")
# elif int(num) % 2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")

# year = int(input("请输入一个年份: "))
# if year % 4 == 0 and year % 100 != 0:
#     print("是闰年")
# elif year % 400 == 0:
#     print("是闰年")
# else:
#     print("平年")

# year = int(input("请输入一个年份: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("是闰年")
# else:
#     print("平年")


staff_type = input("请输入员工类型(普通员工, 管理层, 高管): ")
if staff_type == "普通员工":
    print("只有工资")
elif staff_type == "管理层":
    print("工资加奖金")
elif staff_type == "高管":
    print("工作加奖金加分红")
else:
    print("输出员工不在范围之内")