# 1. 语法(syntax)错误
# 2. 算法(algorithm)错误
# 3. 运行时(runtime) 错误: 异常

try:
    age = int(input("请输入年龄: "))
    if age < 0:
        raise ValueError("年龄不能为负数")
    print(age)
except ValueError as error:
    print("出异常了:", error)
else:
    print("end of try")
finally:
    print("finally")

print("end of code")