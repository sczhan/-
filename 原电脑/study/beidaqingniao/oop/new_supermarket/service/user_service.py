from beidaqingniao.oop.new_supermarket.dao.user_dao import UserDao


class UserService:
    __udao = UserDao()

    def reg(self, user):
        return UserService.__udao.add(user)

    def login(self, user):
        return UserService.__udao.login(user)

    def find_user_id(self, user_id):
        return UserService.__udao.find_by_user_id(user_id)

    def query_all(self):
        return UserService.__udao.select_all()

    def point(self, user_name):
        return UserService.__udao.find_by_point(user_name)

