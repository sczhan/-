from beidaqingniao.oop.d01.book import Book
from beidaqingniao.oop.d01.magazine import Magazine


class BookFactory:
    __new = None
    __inited = False

    def __new__(cls, *args, **kwargs):
        if cls.__new is None:
            cls.__new = object.__new__(cls)
        return cls.__new

    def __init__(self):
        if BookFactory.__inited:
            return
        BookFactory.__inited = True

    def product(self, type="Book", title="Book", publisher="NJUP", price=10, period=4):
        if type == "Book":
            if title == "Book":
                return Book(title, publisher, price)
            return Book(title, publisher, price)
        elif type == "Magazine":
            if title == "Book":
                title = "Magazine"
                return Magazine(title, publisher, price, period)
            return Magazine(title, publisher, price, period)
        else:
            return None


if __name__ == '__main__':
    d1 = BookFactory()
    print(d1.product("Book", 2))
    d2 = BookFactory()
    print(d2.product("Magazine", 1, 2, 3, 5))




