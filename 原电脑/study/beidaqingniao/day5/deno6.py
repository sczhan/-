def test1(a, b, c, d):
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")


test1(2, 5, 8, 4)
test1(d=1, b=3, a=2, c=6)


# 有默认值的参数
def test2(a, b, c=0, d=10):
    print("a = %d, b = %d, c = %d, d = %-2d" % (a, b, c, d))


test2(2, 4)
print('*'*20)


# 变长参数
def test3(*a, b=""):
    print(type(a), a)
    print(f'b={b}')


test3(2, 5, 5, 2, b=3)
