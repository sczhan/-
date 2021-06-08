# 工厂模式: 父类商品, 子类商品, 工厂类
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"商品{self.name}的价格是{self.price}"


class Cole(Drink):
    def __init__(self, price):
        Drink.__init__(self, "Cole", price)


class Sprite(Drink):
    def __init__(self, price):
        Drink.__init__(self, "Sprite", price)


class DrinkFactory:
    # __TY = "2"
    @staticmethod
    def product(type, price):
        if type == "Cole":
            # return str(Cole(price)) + self.__TY
            return Cole(price)
        elif type == "Sprite":
            return Sprite(price)
        else:
            return None


if __name__ == '__main__':
    # d1 = DrinkFactory.product("Cole", 15)  # 报错
    # d2 = DrinkFactory()
    # d3 = DrinkFactory()
    # print(d1.product("Cole", 15))
    # print(d2.product("Sprite", 25))
    # print(d3.product("Fonda", 25))
    d1 = DrinkFactory.product("Cole", 15)
    print(d1)
    d2 = DrinkFactory.product("Sprite", 25)
    print(d2)
    d3 = DrinkFactory.product("Fonda", 25)
    print(d3)
