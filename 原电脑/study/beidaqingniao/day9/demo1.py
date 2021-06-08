# f = open("1.txt", "r", encoding="utf-8")
# print(f)
# f.close()

# f = open("1.txt", "w")
# print(f)
# f.close()

f = open("2.txt", "w", encoding="utf-8")
print("欢迎s5d5", file=f)
f.close()

# f = open("1.txt", "w")
# print("欢迎", file=f)
# f.close()

f = open("3.txt", "a", encoding="UTF-8")
print(f)
f.write("上课较好的会计师")
f.close()
