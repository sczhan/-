# dict字典的定义
dt = {}
print(type(dt))
dt = {1: "a", "first": "a", 2: "b"}
print(type(dt))
print(dt[1])
dt[4] = "four"
print(dt)
dt[2] = "two"
print(dt)
dt[(4, )] = "four"
print(dt)

print(dt.get((4,)))


for key, value in dt.items():
    print(key, "---", value)