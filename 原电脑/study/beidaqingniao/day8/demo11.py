from typing import *


def find_local_sink(elevation_map: [List[int]], cell: List[int]) -> List[int]:
    if cell[0] > len(elevation_map) or cell[1] > len(elevation_map[0]):
        return False

    def local(min_map):
        return min_map[min(min_map)]

    dt = {elevation_map[cell[0]][cell[1]]: [cell[0], cell[1]]}

    if cell[0] > len(elevation_map) or cell[1] > len(elevation_map[0]):
        return False

    if cell[0] >= 0:
        dt[elevation_map[cell[0] + 1][cell[1]]] = [cell[0] + 1, cell[1]]
    if cell[0] <= len(elevation_map) - 1:
        dt[elevation_map[cell[0] - 1][cell[1]]] = [cell[0] - 1, cell[1]]
    if cell[1] >= 0:
        dt[elevation_map[cell[0]][cell[1] + 1]] = [cell[0], cell[1] + 1]
    if cell[0] <= len(elevation_map) - 1:
        dt[elevation_map[cell[0]][cell[1] - 1]] = [cell[0], cell[1] - 1]

    return local(dt)


if __name__ == '__main__':
    maps = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    a = find_local_sink(maps, [1, 1])
    print(a)


