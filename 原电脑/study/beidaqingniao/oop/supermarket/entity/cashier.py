class Cashier:
    def __init__(self, cashier_name, cashier_password):
        self.__cashier_name = cashier_name
        self.__cashier_password = cashier_password

    @property
    def cashier_name(self):
        return self.__cashier_name

    @property
    def cashier_password(self):
        return self.__cashier_password

    @cashier_password.setter
    def cashier_password(self, password):
        self.__cashier_password = password

