from beidaqingniao.oop.new_supermarket.utils.util import save, load


class ReturnItemDao:
    __returns = None

    def __init__(self):
        if ReturnItemDao.__returns is None:
            print("加载退货数据")
            ReturnItemDao.__returns = load("order.dat")

    def __save(self):
        return save("return_item.dat", ReturnItemDao.__returns)

    def find_sno(self, sno):
        for o in ReturnItemDao.__returns:
            if o.id == sno:
                return o
        return None

    def find_sno_return(self, sno):
        for o in ReturnItemDao.__returns:
            if o.id == sno:
                return sno
        return None

    def remove_item(self, order):
        find = self.find_sno(order)
        if find is None:
               return False
        order.items.remove(find)
        return self.__save()