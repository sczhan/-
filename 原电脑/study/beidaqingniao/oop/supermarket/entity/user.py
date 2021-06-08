class User:
    def __init__(self, user_id, password="123456", point=1000):
        self.__uid = user_id
        self.__password = password
        self.point = point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if 0 <= point:
            self.__point = point
        else:
            self.__point = 0

    @property
    def userid(self):
        return self.__uid

    @property
    def password(self):
        return self.__password



