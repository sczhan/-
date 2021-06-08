from typing import *


def get_average_elevation(elevation_map: List[List[int]]) -> float:
    # index = 0
    # a = 0
    # lens = 0
    # while index < len(elevation_map):
    #     a += sum(elevation_map[index])
    #     lens += len(elevation_map[index])
    #     index += 1
    #     p = a / lens
    # return float(p)
    b = []
    [b.extend(x) for x in elevation_map]
    return sum(b) / len(b)


if __name__ == '__main__':
    maps = [[1, 2, 1], [4, 6, 5], [7, 8, 9]]
    a = get_average_elevation(maps)
    print(f"a = {a :.5}")
