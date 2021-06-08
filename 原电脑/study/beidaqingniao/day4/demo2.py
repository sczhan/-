staff_type = input("请输入员工类型(普通员工, 管理层, 高管): ")
if staff_type == "普通员工":
    print("只有工资")
elif staff_type == "管理层":
    print("工资加奖金")
elif staff_type == "高管":
    print("工作加奖金加分红")
else:
    print("输出员工不在范围之内")