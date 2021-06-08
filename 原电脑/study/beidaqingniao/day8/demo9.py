from typing import *


def find_peak(elevation_map: List[List[int]]) -> List[int]:
    # 普通方法
    # row = 0
    # col = 0
    # temp = elevation_map[row][col]
    # for i in range(len(elevation_map)):
    #     for j in range(len(elevation_map[i])):
    #         if elevation_map[i][j] >= temp:
    #             temp = elevation_map[i][j]
    #             row, col = i, j
    # return [row, col]

    lst = [max(m) for m in elevation_map]
    pos = [m.index(max(m)) for m in elevation_map]
    row = lst.index(max(lst))
    return [row, pos[row]]


if __name__ == '__main__':
    maps = [[1, 2, 3], [9, 8, 7], [5, 5, 6]]
    a = find_peak(maps)
    print(a)