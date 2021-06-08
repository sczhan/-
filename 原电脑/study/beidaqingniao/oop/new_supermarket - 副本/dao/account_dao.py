from beidaqingniao.oop.new_supermarket.utils.util import save, load


class AccountDao:
    __accounts = None

    def __init__(self):
        if AccountDao.__accounts is None:
            print("加载收银员数据")
            AccountDao.__accounts = load("account.dat")

    def __save(self):
        return save("account.dat", AccountDao.__accounts)

    def exist_id(self, name):
        for a in AccountDao.__accounts:
            if a.name == name:
                return True
        return False

    def add(self, account):
        if self.exist_id(account.name):
            return False
        AccountDao.__accounts.append(account)
        self.__save()
        return True

    def login(self, account):
        for a in AccountDao.__accounts:
            if a.name == account.name and a.password == account.password:
                return True
        return False

    def updata_password(self,account, new_password):
        for a in AccountDao.__accounts:
            if a.name == account.name and a.password == account.password:
                a.password = new_password
                return self.__save()
        return False

    def delete(self, name):
        for a in AccountDao.__accounts:
            if a.name == name:
                AccountDao.__accounts.remove(a)
                break
        return self.__save()

