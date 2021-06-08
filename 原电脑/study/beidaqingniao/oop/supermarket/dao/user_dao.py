import os
import pickle as pk


class UserDao:
    __users = None

    def __init__(self):
        if UserDao.__users is None:
            print("加载数据")
            if os.access("user.dat", os.F_OK):
                f = open("user.dat", "rb")
                UserDao.__users = pk.load(f)
                f.close()
            else:
                UserDao.__users = []

    def __save(self):
        try:
            f = open("user.dat", "wb")
            pk.dump(UserDao.__users, f)
            f.close()
            return True
        except:
            print("用户数据保存失败")
            return False

    def exist_id(self, user_id):
        for u in UserDao.__users:
            if u.userid == user_id:
                return True
            return False

    def add(self, user):
        if self.exist_id(user.userid):
            return False
        UserDao.__users.append(user)
        self.__save()
        return True

    def login(self, user):
        for u in UserDao.__users:
            print(u.userid, UserDao.__users)
            if u.userid == user.userid and u.password == user.password:
                return True
        return False

#
# if __name__ == '__main__':
#     dao = UserDao()
#     user = User(user_id="123123456", password="987654")
#     rt = dao.add(user)
#     rt = dao.login(user)
#     print(rt)
