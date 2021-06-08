s = "hello  world"
for ch in s:
    print(ch, ord(ch))
print("*" * 20)
print("0x1000: ", chr(0x1000))
print("*" * 20)


st = {4, 8, 5, 5, 2}
for t in st:
    print(t)
print("*" * 20)

dt = {1: "one", 2: "two", 3: "three"}
for k in dt:
    print(k, ": ", dt[k])
print("*" * 20)

# for k, v in dt.items():
#     print(k, ": ", v)
# for v in dt.values():
#     print(v)
