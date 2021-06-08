import os
import pickle as pk


class CashierDao:
    __cashier = None

    def __init__(self):
        if CashierDao.__cashier is None:
            if os.access("cashier.dat", os.F_OK):
                f = open("cashier.dat", "rb")
                CashierDao.__cashiers = pk.load(f)
                f.close()
            else:
                CashierDao.__cashiers = []

    def __save(self):
        try:
            f = open("cashier.dat", "wb")
            pk.dump(CashierDao.__cashiers, f)
            f.close()
            print("收银员数据保存成功")
            return True
        except:
            print("收银员数据保存失败")
            return False

    def exist_id(self, cid):
        for c in CashierDao.__cashiers:
            if c.cashier_name == cid:
                return True
            return False

    def add(self, cashier):
        if self.exist_id(cashier.cashier_name):
            print("收银员已存在")
            return False
        CashierDao.__cashiers.append(cashier)
        self.__save()
        return True

    def login(self, cashier):
        for c in CashierDao.__cashiers:
            if c.cashier_name == cashier.cashier_name and c.cashier_password == cashier.cashier_password:
                return True
            return False

    def change_pw(self, cashier, password):
        for c in CashierDao.__cashiers:
            if c.cashier_name == cashier.cashier_name and c.cashier_password == cashier.cashier_password:
                c.cashier_password = password
                self.__save()
                return True
        return False
