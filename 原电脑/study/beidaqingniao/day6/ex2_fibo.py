
def fibo(index: int) -> int:
    if index < 1:
        raise ValueError('必须是正整数')
    if index <= 2:
        return 1
    return fibo(index-1)+fibo(index-2)


def fibo2(index: int) -> int:
    if index < 1:
        raise ValueError("必须是正整数")
    if index <= 2:
        return 1
    a = b = 1
    for n in range(index - 2):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    n = fibo(10)
    print(n)
    n = fibo2(10)
    print(n)