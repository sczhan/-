from beidaqingniao.oop.supermarket.dao.cashier_dao import CashierDao


class CashierServer:
    ___cdao = CashierDao()

    def reg(self, cashier):
        return CashierServer.___cdao.add(cashier)

    def login(self, cashier):
        return CashierServer.___cdao.login(cashier)

    def change_pd(self, cashier, password):
        return CashierServer.___cdao.change_pw(cashier=cashier, password=password)