class Demo:
    __ty = "DL"

    def __init__(self, name='default'):
        self.name = name

    def __str__(self):
        return f"name = {self.name}"

    def intro(self):
        print("name: ", self.name)

    @staticmethod       # 没有参数
    def test():
        print("static test")

    @classmethod            # 有参数
    def test2(cls):
        print("static test2 ", cls.__ty)


if __name__ == '__main__':
    d1 = Demo("Mike")
    d1.intro()
    print(d1)
    Demo.test()
    Demo.test2()
    # 类的方法不建议使用对象调用, 虽然语法正确
    # d1.test()
    # d1.test2()
