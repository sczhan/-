
class Admin:
    def __init__(self, name="admin", password="123456"):
        self.__name = name
        self.__password = password

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password




