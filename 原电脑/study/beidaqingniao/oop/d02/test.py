from beidaqingniao.oop.d02.factory import BookFactory


if __name__ == '__main__':
    fac = BookFactory()
    books = [fac.product(),
             fac.product("Magazine", period=10),
             fac.product("Book", "python", "py", 15),
             fac.product("Magazine", "js", "jss", 11, 5)]
    for i in books:
        print(i)
    print("*" * 20)
    books.sort()
    print("*" * 20)
    for i in books:
        print(i)
    # book = [
    #          fac.product("Magazine", period=10),
    #         fac.product(),]
    # book.sort()
    # print(book[0])