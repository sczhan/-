# 函数定义: 无参无返回值
def test1():
    print("hello test1")


test1()
print("*" * 20)
a = test1()
print(a)
print("*" * 20)


# 函数定义: 有参无返回值
def test2(s):    # 形式参数  形参
    print("s = ", s)


a = test2("jj")   # 实际参数 实参
# 实参数量和形参必须一致, 否则报错
# s = test2()
# s = test2(12, 45)
print(a)
print("*" * 20)


# 函数定义: 有参有返回值
def test3(s):
    print("s = ", s)
    return s


a = test3("55")
print(a)
