from beidaqingniao.oop.new_supermarket.dao.item_Dao import ItemDao


class ItemService:
    __idao = ItemDao()

    def add(self, item):
        return ItemService.__idao.add(item)

    def query_all(self):
        return ItemService.__idao.select_all()

    def find_price(self, item_id):
        ret = ItemService.__idao.find_by_id(item_id)
        if ret is None:
            return None
        return ret.price
