# print("hello, world")
# import this

# print("hello", "world", "!", sep="**")
# print("second line", end="")
# print("\n")
# print()
# # print("\n")
# print(12, end="")


# 创建一个文件对象
f = open("1.txt", "w")
print("hello, world", file=f, flush=True)
print("ok")
# print(f.read()) 读取的时候要 "r"
# 关闭文件
f.close()
