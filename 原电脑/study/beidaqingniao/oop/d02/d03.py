import math
class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{(self.x, self.y)}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Coord):
            return math.sqrt((self.x + other.x) ** 2 + (self.y + other.y) ** 2)
        else:
            raise ValueError("必须是坐标")

    def __sub__(self, other):
        if isinstance(other, Coord):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        else:
            raise ValueError("必须是坐标")

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        else:
            raise ValueError("必须是坐标")

    def __lt__(self, other):
        if isinstance(other, Coord):
            return (self - Coord()) < (other - Coord())
        else:
            raise ValueError("必须是坐标")


if __name__ == '__main__':
    c1 = Coord(4, 4)
    c2 = Coord(4, 3)
    print(c2 - c1)
    print(c2 + c1)
    print(c1 == c2)
    # print(c1 == 3)
    coords = [c1, c2, Coord(5, 2)]
    coords.sort()
    for i in coords:
        print(i)