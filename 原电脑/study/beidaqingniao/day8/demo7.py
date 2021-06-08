from typing import *


def update_elevation(elevation_map: List[List[int]], start_cell:List[int],
                     end_cell: List[int], change: int):
    if start_cell[0] < 0 or start_cell[0] >= len(elevation_map):
        raise ValueError("起始位置行号参数不对")
    if start_cell[1] < 0 or start_cell[1] >= len(elevation_map[0]):
        raise ValueError("起始位置列号参数不对")
    if end_cell[0] < 0 or end_cell[0] >= len(elevation_map):
        raise ValueError("结束位置行号参数不对")
    if end_cell[1] < 0 or end_cell[1] >= len(elevation_map[0]):
        raise ValueError("结束位置列号参数不对")
    if not (start_cell[0] == end_cell[0] or start_cell[1] == end_cell[1]):
        raise ValueError("不在同一行或者同一列")
    if end_cell[0] == start_cell[0] and end_cell[1] < start_cell[1]:
        raise ValueError("起始位置的列号大于结束位置")
    if end_cell[1] == start_cell[1] and end_cell[0] < start_cell[0]:
        raise ValueError("起始位置的行号大于结束位置")

    for r in range(start_cell[0], end_cell[0] + 1):
        for c in range(start_cell[1], end_cell[1] + 1):
            elevation_map[r][c] += change
            elevation_map[r][c] = 1 if elevation_map[r][c] < 1 else elevation_map[r][c]
            elevation_map[r][c] = elevation_map[r][c] if elevation_map[r][c] < 10 else 9


if __name__ == '__main__':
    try:
        maps = [[1, 2, 1], [4, 6, 5], [7, 8, 9]]
        a = update_elevation(maps, [0, 2], [2, 2], -5)
        print(maps)
    except ValueError as e:
        print(e)