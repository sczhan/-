dt = {"name": "mike", "age": 18, "gender": "M"}

for k in dt:
    print(k, dt[k])
print("*" * 20)

for v in dt.values():
    print(v)
print("*" * 20)

for k, v in dt.items():
    print(k, v)
print("*" * 20)

for k in dt.items():
    print(k, type(k))
print("*" * 20)

# 存在即取值
print(dt.setdefault("age"))

# 不存在即复制
print(dt.setdefault("email", "unknown"), dt)
print(dt.setdefault("emails"), dt)
print("*" * 20)

# 存在则修改,不存在则添加
dt.update({"name": "andy", "height": "55"})
print(dt)

# 存在则删除, 不存在则报错
name = dt.pop("name")
print(name, dt)

# dt.pop("namess")