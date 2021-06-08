class ItemDao:
    __items = None

    def __init__(self):
        if ItemDao.__items is None:
            print("加载商品数据")
            ItemDao.__items = load("item.dat")

    def __save(self):
        return save("item.dat")