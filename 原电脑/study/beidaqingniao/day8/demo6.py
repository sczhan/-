from typing import *


def compare_elevations_within_row(elevation_map: List[List[int]],
                                  row_number: int, elevation: int) -> List[int]:
    if row_number >= len(elevation_map):
        raise ValueError("参数不合法")
    row_data = elevation_map[row_number]
    # a = b = c = 0
    # for n in row_data:
    #     if n < elevation:
    #         a += 1
    #     elif n == elevation:
    #         b += 1
    #     else:
    #         c += 1
    # return [a, b, c]
    return [len([x for x in row_data if x < elevation]),
            len([x for x in row_data if x == elevation]),
            len([x for x in row_data if x > elevation]),
            ]


if __name__ == '__main__':
    maps = [[1, 2, 1], [4, 6, 5], [7, 8, 9]]
    a = compare_elevations_within_row(maps, 1, 4)
    print(a)