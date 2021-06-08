# dt
dt = {}.fromkeys((1, 2, 5))
print(dt)

dt1 = {}.fromkeys((1, 2, 5), "tess")
print(dt1)

dt2 = {}.fromkeys((1, 2, (5, 5)), "tess")
print(dt2)

# print(dt["2"])  # 报错
print(dt1.get("4", "no"))
print(dt1.get("4",))
print(dt1.get(2, "no"))
