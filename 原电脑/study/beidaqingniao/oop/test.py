#
# class Rectangle(object):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     @property
#     def width(self):
#         # 变量名不与方法名重复，改为true_width，下同
#         return self.__width
#     # @width.setter
#     # def width(self, width):
#     #     self.__width = width
#     @property
#     def height(self):
#         return self.true_height
#     @height.setter
#     #与property定义的方法名要一致
#     def height(self, input_height):
#         self.true_height = input_height
# s = Rectangle(2,5)
# # 与方法名一致
# s.width = 1024
# s.height = 768
# print(s.width,s.height)
def list():
    a = {"一等奖": 1, "二等奖": 1, "三等奖": 1, "安慰奖": 6}
    b = []
    for k, v in a.items():

        for c in range(v):
            b.append(k)
    # c = [[b.append(k) for t in range(v)] for k, v in a]
    return b
print(list())