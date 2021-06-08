from typing import *


def square(a: List[int]):
    index = 0
    while index < len(a):          # 判读索引位置是否超出
        a[index] = a[index] ** 2   # 修改列表中的值
        index += 1


if __name__ == '__main__':
    lt = [1, 2, 4]
    print(lt)
    square(lt)
    print(lt)

