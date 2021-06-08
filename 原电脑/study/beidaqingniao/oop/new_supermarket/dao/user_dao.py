from beidaqingniao.oop.new_supermarket.utils.util import save, load


class UserDao:
    __users = None

    def __init__(self):
        if UserDao.__users is None:
            print("用户加载数据")
            UserDao.__users = load("user.dat")

    def __save(self):
        return save("user.dat", UserDao.__users)

    def exist_id(self, user_name):
        for u in UserDao.__users:
            if u.user_name == user_name:
                return True
        return False

    def add(self, user):
        if self.exist_id(user.user_name):
            return False
        UserDao.__users.append(user)
        self.__save()
        return True

    def login(self, user):
        for u in UserDao.__users:
            if u.user_name == user.user_name and u.password == user.password:
                return True
        return False

    def find_by_id(self, user_id):
        for u in UserDao.__users:
            if u.user_name == user_id:
                return u
        return None

    def find_by_user_id(self, user_id):
        for u in UserDao.__users:
            if u.user_name == user_id:
                return u.user_name
        return None

    def update_point(self, user):
        find = self.find_by_id(user.user_name)
        if find is None:
            return False
        find.point += user.point
        return self.__save()

    def return_update_point(self, user):
        find = self.find_by_id(user.user_name)
        if find is None:
            return False
        find.point -= user.point
        return self.__save()

    def select_all(self):
        return UserDao.__users

    def lottery_point(self, user):
        for u in UserDao.__users:
            if u.user_name == user.user_name:
                if u.point >= 1000:
                    u.point = u.point - 1000
                    return self.__save()
                else:
                    return False


    def find_by_point(self, user_id):
        for u in UserDao.__users:
            if u.user_name == user_id:
                return u.point
        return None