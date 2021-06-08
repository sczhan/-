from typing import *


def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    if cell[0] > len(elevation_map) or cell[1] > len(elevation_map[0]):
        return False
    a = [elevation_map[cell[0]][cell[1]]]
    if cell[0] >= 0:
        up = elevation_map[cell[0] - 1][cell[1]]
        a.append(up)
    if cell[0] <= len(elevation_map) - 1:
        down = elevation_map[cell[0] + 1][cell[1]]
        a.append(down)
    if cell[1] >= 0:
        right = elevation_map[cell[0]][cell[1] + 1]
        a.append(right)
    if cell[0] <= len(elevation_map) - 1:
        left = elevation_map[cell[0]][cell[1] - 1]
        a.append(left)
    if min(a) == elevation_map[cell[0]][cell[1]]:
        return True
    return False


if __name__ == '__main__':
    maps = [[1, 6, 5],
            [8, 5, 7],
            [7, 1, 5]]
    a = is_sink(maps, [0, 0])
    print(a)