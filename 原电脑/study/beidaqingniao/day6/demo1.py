def test1(a, b):
    return a + b, a * b


n, m = test1(2, 5)
print(n, m)
n = test1(2, 5)
print(n)