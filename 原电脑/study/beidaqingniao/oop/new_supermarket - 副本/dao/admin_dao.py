from beidaqingniao.oop.new_supermarket.entity.admin import Admin


class AdminDao:
    __adao = Admin()

    def login(self, admin):
        return AdminDao.__adao.name == admin.name and AdminDao.__adao.password == admin.password