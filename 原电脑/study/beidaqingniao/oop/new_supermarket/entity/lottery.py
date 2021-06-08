class Lottery:
    def __init__(self, user):
        self.__user = user

    @property
    def user(self):
        return self.__user.point

    def list(self):
        a = {"一等奖": 1, "二等奖": 1, "三等奖": 1, "安慰奖": 6}
        b = []
        [[b.append(k) for t in range(v)] for k, v in a.items()]
        return b


