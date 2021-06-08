from typing import *


def test1(a):
    print(a, type(a))


def test2(a: int):
    print(a, type(a))


def test3(a: int, b: int) -> int:
    print(a, type(a))
    return a + b, a * b


def test4(a: int, b: List, c: Tuple, d: Set, e: str, f:Dict):
    print(a, type(a), b, c)


def test5(a: int, b: List[int]):
    print(a, type(a))


if __name__ == '__main__':
    test1("a")
    test1(1)
    test1((1, 2))
    test2(1)
    test2("a")
    test3(4, 5)
    test4(1, 2, 3, 4, 4, 5)
    test4(1, [2, ],  (3, ), {4}, "4", {5: "five"})
    test5("A", ["A", ])
    test5(1, [1, ])