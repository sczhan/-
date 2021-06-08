import pickle as pk

from beidaqingniao.oop.supermarket.entity.admin import Admin


class AdminDao:
    __admin = Admin()

    def login(self, admin):
        return AdminDao.__admin.name == admin.name and AdminDao.__admin.password == admin.password


if __name__ == '__main__':
    admin = Admin()
    f = open("admin.dat", "wb")
    pk.dump(admin, f)
    f.close()

    # 测试读取数据
    f = open("admin.dat", "rb")
    admin = pk.load(f)
    f.close()
    print(admin.name, admin.password)
