
class Book:                                                                        # 定义图书类
    def __init__(self, title="Book", publisher="NJUP", price=10):                  # 重写构造方法
        self.title = title
        self.publisher = publisher
        self.price = price

    def __str__(self):                                                             # 重写__str__方法返回图书信息
        return f'{self.title},出版社是{self.publisher}, 价格是{self.__price}'

    @property                                                                     # 对price进行封装
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price >= 0:
            self.__price = price
        else:
            self.__price = 1

    def __lt__(self, other):
        if type(other) is Book:
            print(self, other, 1)
            return self.price < other.price
        print(self, other,  2, not other < self, )
        return not other < self


if __name__ == '__main__':
    book1 = Book("1", 2, price=-5)
    book1.__str__()
    print(book1)
    print(book1.__str__())
    print(book1.__repr__())
