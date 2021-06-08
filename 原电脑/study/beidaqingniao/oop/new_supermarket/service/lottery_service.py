from beidaqingniao.oop.new_supermarket.dao.lottery_dao import LotteryDao
from beidaqingniao.oop.new_supermarket.dao.user_dao import UserDao


class LotteryService:
    _ldao = LotteryDao()
    __udao = UserDao()

    def lottery(self, list, user):
        if LotteryService.__udao.lottery_point(user):
            print("积分 -1000")
            return LotteryService._ldao.lottery(list)
        else:
            print("积分不足")


