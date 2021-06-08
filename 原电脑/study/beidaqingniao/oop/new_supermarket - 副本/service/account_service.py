from beidaqingniao.oop.new_supermarket.dao.account_dao import AccountDao


class AccountService:
    __adao = AccountDao()

    def login(self, account):
        return AccountService.__adao.login(account)

    def add(self, account):
        return AccountService.__adao.add(account)

    def modify(self, account, new_password):
        return AccountService.__adao.updata_password(account, new_password)

    def remove(self, name):
        return AccountService.__adao.delete(name)
