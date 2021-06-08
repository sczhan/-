# 单例模式: 一个类且能创建一个对象实例


class MySignleton:

    __obj = None
    __inited = False

    # 重写object中用于创建对象, 分配内存空间的方法
    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, age=10):
        if MySignleton.__inited:
            return
        self.age = age
        print("init...")
        MySignleton.__inited = True

    def product(self, type, price):
        if type == "Cole":
            # return str(Cole(price)) + self.__TY
            return price
        elif type == "Sprite":
            return price
        else:
            return None


if __name__ == '__main__':
    ms1 = MySignleton()
    ms2 = MySignleton(20)
    print(ms1.product("Sprite", 2), ms1, ms2)
    print(ms2.product("Sprite", 3))
    print(ms1.age)
    print(ms2.age)