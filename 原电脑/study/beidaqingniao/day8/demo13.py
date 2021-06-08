from typing import *


def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:

    def cell(a):
        x, y, z, m = [], [], [], []
        [[x.append(elevation_map[i][j]) for j in range(a)] for i in range(a)]
        [[y.append(elevation_map[i][j]) for j in range(a, len(elevation_map[i]))] for i in range(a)]
        [[z.append(elevation_map[i][j]) for j in range(a)] for i in range(a, len(elevation_map))]
        [[m.append(elevation_map[i][j]) for j in range(a, len(elevation_map[i]))] for i in range(a, len(elevation_map))]
        print(x)
        first = [int(sum(x) / len(x)), int(sum(y) / len(y))]
        second = [int(sum(z) / len(z)), int(sum(m) / len(m))]
        return [first, second]
    if len(elevation_map) % 2 == 0:
        b = len(elevation_map) // 2
        return cell(b)
    b = len(elevation_map) // 2 + 1
    return cell(b)


if __name__ == '__main__':
    maps1 = [[1, 6, 5, 6], [2, 5, 6, 8], [7, 2, 8, 1], [4, 4, 7, 3]]
    maps2 = [[7, 9, 1], [4, 2, 1], [3, 2, 3]]
    maps3 = [[1, 6, 5, 6, 1, 5], [2, 5, 6, 8, 1, 8], [7, 2, 8, 1, 2, 6], [4, 4, 7, 3, 5, 5], [2, 5, 6, 8, 1, 8], [7, 2, 8, 1, 2, 6]]
    a = get_lower_resolution(maps1)
    m = get_lower_resolution(maps2)
    v = get_lower_resolution(maps3)
    print(a, m, v)
