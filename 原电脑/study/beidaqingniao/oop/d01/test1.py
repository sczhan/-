from beidaqingniao.oop.d01.book import Book


if __name__ == '__main__':
    book1 = Book(title="l", publisher="2", price=11)         # 创建对象
    book2 = Book(title="4", publisher="5", price=6)
    book3 = Book(title="7", publisher="8", price=9)
    book = [book1, book2, book3]                            # 将对象放入列表
    for i in book:
        print(i)                                      # 依次输出图书信息
    book_price = [i.price for i in book]
    book.sort(key=lambda b: b.price)                                      # 排序
    print("*" * 20)
    for i in book:
        print(i)
    # [[m.__str__() for m in book if m.price == i] for i in book_price]   # 依次输出图书信息

    # for i in book_price:
    #     for m in book:
    #         if m.price == i:
    #             m.__str__()


