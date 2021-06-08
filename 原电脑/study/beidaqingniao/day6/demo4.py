def test1():
    print("1.test1")

    def test2():
        # print("test2")
        return "v"
    print("2.test2")
    return print(test2())


test1()