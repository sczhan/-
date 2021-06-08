# 二进制方式操作方式, 不能指定字符编码
f = open("4.txt", "wb")
print(f)
# 在对字符串进行编码转换时指定
f.write("hello碶欢迎".encode(encoding="UTF-8"))
# 错误写法
# print("hello欢迎", file=f)
f.close()

