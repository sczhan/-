try:
    lt = [1, 2, 3]
    a = 10
    b = int(input("输入数字: "))
    dt = {"one": 1}
    c = a / b
    print(lt[b])
    print(dt["two"])
except ZeroDivisionError as e1:
    print("error:", e1)
except ValueError as e2:
    print("error:", e2)
except KeyError as e3:
    print("error:", e3)
except IndexError as e4:
    print("error:", e4)
except:
    print("other error")
