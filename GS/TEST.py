# for i in ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O"]:
#     a = "=SUMPRODUCT((COUNTIF('Check List'!{0}12:{0}119,".format(i)
#     B = '"O")/COUNTIF('
#
#     C = "'Check List'!{0}12:{0}119,".format(i)
#     D = '"<>")))'
#     print(a + B + C + D)
a = ""

for i in range(6, 19):
    b = "E{}*0.1 + ".format(i)
    a += b

print(a)
A = ("1", "2")

b = "*0.1 "

print(b.join(A))


str = "-"
seq = ("a", "b", "c")# 字符串序列
print(str.join( seq ))

inf = float("inf")
print(inf, type(inf))



import numpy as np
a = np.zeros([10, 10])
print(a)

class Tree:
    def __init__(self, kid, next=None):
        self.kid = self.val = kid
        self.next = next


a = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
print(a.kid.kid)

import random
a = [random.randrange(1000) for i in range(1000)]

print(42 in a)

import timeit
# if __name__ == '__main__':
#     # acb = [[1, 2, 3], [4, 5], [6], [7]]
#     # print(timeit.timeit('a = sum([[1, 2, 3], [4, 5], [6], [7]], [])'))
#     def main():
#         res = []
#         for i in [[1, 2, 3], [4, 5], [6], [7]]:
#             res.extend(i)
#         # print(sum(range(10)))
#
#     import cProfile
#     cProfile.run("main()")
print(timeit.timeit('a = sum([[1, 2, 3], [4, 5], [6], [7]], [])', number=100000))
# print(timeit.timeit('for i in [[1, 2, 3], [4, 5], [6], [7]]:  a= []; a.extend(i) '))
def main():
    res = []
    for i in [[1, 2, 3], [4, 5], [6], [7]]:
        res.extend(i)
print(timeit.timeit("main", number=100000))
print(sum(0.1 for i in range(10)) == 1)
from decimal import *
print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
print(round(abs(sum(0.1 for i in range(10)) - 1)) == 0)
print(round(abs(sum(0.1 for i in range(10)) -  1)))

import math
print(1.0/(math.sqrt(8762348761.13+1) - math.sqrt(8762348761.13)))
print(math.sqrt(8762348761.13+1) - math.sqrt(8762348761.13))
print(1/187214.83660896108)
print((math.sqrt(8762348761.13+1) - math.sqrt(8762348761.13)))
print(math.sqrt(8762348761.13+1) )
print(math.sqrt(8762348761.13))
print(1.0*5.341455107554793e-06)