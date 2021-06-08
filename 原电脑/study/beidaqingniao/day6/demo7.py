def test1():
    a = 10
    print(f"1. test1 a ={a}")       # 10

    def test2():
        nonlocal a
        print(f"2. test2 a ={a}")   # 10
        a = 99
        print(f"3. test2 a ={a}")   # 99
    test2()
    print(f"4. a ={a}")             # 99
    return test2()                  # 99  99


if __name__ == '__main__':
    test1()
