def test1(a):
    a[0] = 100


def test2(a):
    a = [100, 200, 300]
    # a[0] = [100, 200, 300]
    # print(a)


lt = [5, 6, 2]
print(lt)
test1(lt)
print(lt)   # 100, 6, 2
print("*" * 20)

test2(lt)
print(lt)
print("*" * 20)

# tp = (1, 3, 5)
# print(tp)
# test1(tp)  # 产生异常
# print(tp)

