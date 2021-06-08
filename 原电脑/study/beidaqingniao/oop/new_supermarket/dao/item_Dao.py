from beidaqingniao.oop.new_supermarket.utils.util import save, load


class ItemDao:
    __items = None

    def __init__(self):
        if ItemDao.__items is None:
            print('加载商品数据')
            ItemDao.__items = load('item.dat')

    def __save(self):
        return save('item.dat', ItemDao.__items)

    def exist_id(self, id):
        for i in ItemDao.__items:
            if i.id == id:
                return True
        return False

    def add(self, item):
        if self.exist_id(item.id):
            return False
        ItemDao.__items.append(item)
        return self.__save()

    def select_all(self):
        return ItemDao.__items

    def find_by_id(self, id):
        for i in ItemDao.__items:
            if i.id == id:
                return i
        return None

    def updata_stock(self, item):
        find = self.find_by_id(item.id)
        if find is None:
            return False
        find.stock -= item.stock
        return self.__save()

    def return_updata_stock(self, item):
        find = self.find_by_id(item.id)
        if find is None:
            return False
        find.stock += item.stock
        return self.__save()
