import random

from beidaqingniao.oop.new_supermarket.utils.util import save, load


class LotteryDao:
    __lottery = None

    def __init__(self):
        if LotteryDao.__lottery is None:
            print("用户加载数据")
            LotteryDao.__lottery = load("user.dat")

    def __save(self):
        return save("user.dat", LotteryDao.__lottery)

    def lottery(self, list):
        lottery = random.randrange(0, len(list))
        return list[lottery]


