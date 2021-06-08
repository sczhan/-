# import beidaqingniao.day6.demo5 as d5
# from beidaqingniao.day5.ex1 import accept_int
#
# if __name__ == "__main__":
#     print(__name__, "demo6")
#     accept_int(2, 10)
#     print(d5.__name__)
#

# 全局变量
a = 100


def test1():
    global a
    a = 9
    print(f"in test1: a= {a}")


def test2():
    # 局部变量
    a = 99
    print(f"in test2: a= {a}")
    print(f"in test2: a= {a}")


if __name__ == "__main__":
    print("a =", a)    # a =100
    test1()            # in test1: a= 9
    print("a =", a)    # a =9
    test2()            # in test2: a= 99   in test2: a= 99
    print("a =", a)    # a =9

