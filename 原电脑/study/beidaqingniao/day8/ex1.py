# def prime_number(n: int) -> tuple:
#     lt = [i for i in range(2, n + 1)]     # 从2-n的正整数
#     y = []
#     y.append(min(lt))                      # 将lt最小值2加入y
#     while max(y) ** 2 <= lt[-1]:           # 判断y中最大值的平方
#         [lt.remove(i) for i in lt if i % max(y) == 0]
#         y.append(min(lt))
#     y.extend(lt[1:])
#     return tuple(y)                       # 返回
#
#
# if __name__ == '__main__':
#     a = prime_number(10)
#     print(a)
#     print(len(a))


def prime_number(n: int) -> tuple:
    x = [i for i in range(n, 1, -1)]
    y = []
    while len(x):
        c = x.pop
        for n in x:
            if n % c == 0:
                x.remove(n)
        y.append(c)
    return y


if __name__ == '__main__':
    a = prime_number(10)
    print(a)