from beidaqingniao.oop.d01.book import Book


class Magazine(Book):                                                            # 图书类的子类杂志类（Magazine）
    def __init__(self, title="Magazine", publisher="NJUP", price=10, period=4):    # 重新定义杂志类的构造方法
        Book.__init__(self, title, publisher, price)
        self.period = period

    @property                                                                     # 对period进行封装
    def period(self):
        return self.__period

    @period.setter
    def period(self, period):
        if 4 <= period <= 53:
            self.__period = period
        else:
            self.__period = 4

    def __str__(self):                                                            # 重写__str__方法
        return Book.__str__(self) + f', {self.period}期'

    def __lt__(self, other):
        if isinstance(other, Magazine):
            print(self, other, 3, self.price * self.period < other.price * other.period)
            return self.price * self.period < other.price * other.period
        if isinstance(other, Book):
            print(self, other, 4, self.price * self.period < other.price)
            return self.price * self.period < other.price
        raise ValueError('无法比较')


if __name__ == '__main__':
    a = Magazine("1", "2", 6, period=-5)
    print(a)
    print(a.__str__())