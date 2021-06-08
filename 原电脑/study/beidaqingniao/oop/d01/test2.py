from beidaqingniao.oop.d01.book import Book
from beidaqingniao.oop.d01.magazine import Magazine

if __name__ == '__main__':
    book1 = Book(title="l", publisher="2", price=11)                           # 创建对象
    book2 = Book(title="4", publisher="5", price=6)
    book3 = Book(title="7", publisher="8", price=9)
    magazine1 = Magazine(title="2", publisher="8", price=9, period=3)
    magazine2 = Magazine(title="5", publisher="8", price=10, period=3)
    magazine3 = Magazine(title="6", publisher="8", price=8, period=3)
    book = [book1, book2, book3, magazine1, magazine2, magazine3]
    for i in book:
        print(i)
    book.sort(key=lambda b: b.price * b.period if isinstance(b, Magazine) else b.price)
    print("*" *20)
    for i in book:
        print(i)
        # 对象放入列表
    # book_price = []
    # for i in book:
    #     if isinstance(i, Magazine):                                            # 是不是杂志对象
    #         book_price.append(i.price * i.period)
    #     else:
    #         book_price.append(i.price)
    # book_sort = []
    # while len(book_price):                                                      # 用价格进行排序
    #     a = book_price.index(min(book_price))
    #     book_sort.append(book[a])
    #     book_price.pop(a)
    #     book.pop(a)
# print(book_sort)

