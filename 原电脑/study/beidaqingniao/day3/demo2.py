# set定义
st1 = {2, 5, 4}
st2 = set()
# 下列不是set而是dict
# st = {}
st = {}
print(type(st), type(st1), type(st2))
st4 = set("hello, world")
print(type(st4), st4)

st4.add((5, ))
print(st4)
st4.add(5)
print(st4)
st4.add("kilk")
print(st4)
st4.remove("kilk")
print(st4)
# set不可以添加可变类型
# st4.add([5, ])