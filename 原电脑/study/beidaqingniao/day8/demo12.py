from typing import *


def can_hike_to(elevation_map: List[List[int]],  start_cell: List[int], destination_cell: List[int], supplies: int) -> bool:
    def local(cell, num):
        start_high = elevation_map[cell[0]][cell[1]]
        if 0 < cell[0] <= len(elevation_map) - 1:
            north = elevation_map[cell[0] - 1][cell[1]]
        if 0 < cell[1] <= len(elevation_map[cell[0]]) - 1:
            west = elevation_map[cell[0]][cell[1] - 1]
        if cell[0] == destination_cell[0]:
            cell = [cell[0], cell[1] - 1]
            num -= abs(start_high - west)
        elif start_cell[1] == destination_cell[0]:
            cell = [cell[0] - 1, cell[1]]
            num -= abs(start_high - north)
        elif abs(start_high - west) >= abs(start_high - north):
            cell = [cell[0] - 1, cell[1]]
            num -= abs(start_high - north)
        else:
            cell = [cell[0], cell[1] - 1]
            num -= abs(start_high - west)
        if cell == destination_cell and num >= 0:
            return True
        if num < 0:
            return False
        return local(cell, num)
    return local(start_cell, supplies)


if __name__ == '__main__':
    maps = [[1, 2, 3], [9, 2, 7], [4, 8, 6]]
    a = can_hike_to(maps, [2, 2], [2, 0], 5)
    print(a)