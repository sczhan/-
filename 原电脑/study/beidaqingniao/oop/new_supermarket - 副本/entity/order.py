from beidaqingniao.oop.new_supermarket.utils.sno import Sno


class Order:

    def __init__(self, user_id, items):
        self.__id = Sno.get_no()
        self.__user_id = user_id
        self.__items = items

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def items(self):
        return self.__items

