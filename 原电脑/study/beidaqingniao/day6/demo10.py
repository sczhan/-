# 生成器 generator: 函数使用yield返回即生成器
def my_generator(lt: tuple):
    index = 0
    while index < len(lt):
        yield lt[index]
        index += 1


t = my_generator((1, 2, 4))
print(type(t))
print(type(next(t)))
print(next(t))
print(next(t))
# print(next(t))