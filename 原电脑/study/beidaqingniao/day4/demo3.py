num = int(input("请输入一个整数: "))
# 条件表达式
print("偶数" if num % 2 == 0 else "奇数")
other_num = int(input("请输入一个整数: "))
print(num if num > other_num else other_num)
# print("最小数是: {}".format(num) if num < other_num else "最小数是: {}".format(other_num))

# 使用逻辑运算符实现条件表达式
# print(num > other_num and num or other_num)  # 当 num = 0 other_num = -7 的时候结果就不对了
# 列表版
print((num > other_num and [num] or [other_num])[0])
# 元组版
print((num > other_num and (num,) or (other_num,))[0])