from beidaqingniao.oop.new_supermarket.utils.util import save, load


class OrderDao:
    __odaoers = None

    def __init__(self):
        if OrderDao.__odaoers is None:
            print("加载订单数据")
            OrderDao.__odaoers = load("order.dat")

    def __save(self):
        return save("order.dat", OrderDao.__odaoers)

    def add(self, order):
        OrderDao.__odaoers.append(order)
        return self.__save()

    def select_all(self):
        return OrderDao.__odaoers




    # def exist_id(self,item_id):
    #     for u in OrderDao.__orders:
    #         if u.id==item_id:
    #             return  True
    #     return False
