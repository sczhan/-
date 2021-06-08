class Item:
    def __init__(self, id, title, stock, price):
        self.__id = id
        self.__title = title
        self.stock = stock
        self.price = price

    def __str__(self):
        return f'商品编号:【{self.__id}】,商品名称: {self.__title},库存:（{self.__stock}）,单价:({self.__price}）'

    def __repr__(self):
        return self.__str__()

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if isinstance(stock, int):
            if stock >= 0:
                self.__stock = stock
            else:
                raise ValueError("商品库存不能为负数")
        else:
            raise ValueError("商品库存不能为小数")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("商品价格不能为负数")




