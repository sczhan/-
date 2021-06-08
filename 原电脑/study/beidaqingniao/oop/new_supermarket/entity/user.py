from beidaqingniao.oop.new_supermarket.entity.Person import Person


class User(Person):

    def __init__(self, user_name, user_password="123456", point=1000):
        Person.__init__(self, user_name, user_password)
        self.point = point

    @property
    def user_name(self):
        return self.name

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        if 0 <= point:
            self.__point = point
        else:
            self.__point = 0

    def __str__(self):
        return f"顾客ID: {self.user_name}, 积分: {self.point} "

