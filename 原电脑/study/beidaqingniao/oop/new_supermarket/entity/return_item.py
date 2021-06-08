class ReturnItem:
    def __init__(self, order_num):
        self.__order_num = order_num

    @property
    def order_num(self):
        return self.__order_num


# if __name__ == '__main__':
#     R = ReturnItem(2)
#     print(R.order_num)