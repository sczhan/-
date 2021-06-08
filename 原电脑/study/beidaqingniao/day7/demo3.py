s = "hello world"
print(s.find("l"))
print(s.rfind("l", 0, -3))
print(s.find("L"))     # find 未找到返回-1

print(s.index("l"))
print(s.rindex("l"))
# print(s.index("k"))   index 未找到会报异常 ValueError
print("*" * 20)

print("1234".isdigit())
print("123ahb".isalpha())
print("12一千".isnumeric())
print("sg12".isalnum())

s = "hello world, python"
print(s.lower().islower())
print(s.upper().isupper())
t = s.title()
print(t, t.istitle(), type(t))
print(s)


s = "hell\tworld   python"
print(s.expandtabs())