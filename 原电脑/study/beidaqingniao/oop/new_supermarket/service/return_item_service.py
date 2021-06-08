from functools import reduce

from beidaqingniao.oop.new_supermarket.dao.item_Dao import ItemDao
from beidaqingniao.oop.new_supermarket.dao.order_dao import OrderDao
from beidaqingniao.oop.new_supermarket.dao.return_item_dao import ReturnItemDao
from beidaqingniao.oop.new_supermarket.dao.user_dao import UserDao
from beidaqingniao.oop.new_supermarket.entity.user import User


class ReturnItemService:
    __rdao = ReturnItemDao()
    __odao = OrderDao()
    __udao = UserDao()
    __idao = ItemDao()

    def return_item(self, order):
        try:
            ReturnItemService.__rdao.remove_item(order)
            sum = reduce(lambda a, b: a + b, map(lambda x: x.price * x.stock, order.items))
            # sum=0
            for i in order.items:
                # sum+=i.stock*i.price
                ReturnItemService.__idao.return_updata_stock(i)
            user = User(user_name=order.user_id, point=int(sum))
            ReturnItemService.__udao.return_update_point(user)
            return True
        except:
            return False

    def return_item_sno(self, sno):
        return ReturnItemService.__rdao.find_sno(sno)

    def return_item_name(self, sno):
        return ReturnItemService.__rdao.find_sno_return(sno)
