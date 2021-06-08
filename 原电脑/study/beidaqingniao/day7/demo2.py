s = "hello world  欢迎"

# bytes
bs = s.encode(encoding="utf-8", errors="ignore")
print(bs, type(bs))

t = bs.decode(encoding="utf-8")
print(t, type(t))


# bytes
bs = s.encode(encoding="US-ASCII", errors="replace")  # errors="replace" 替换
print(bs, type(bs))

t = bs.decode(encoding="US-ASCII")
print(t, type(t))


# bytes
bs = s.encode(encoding="US-ASCII", errors="ignore")   # errors="ignore" 忽略
print(bs, type(bs))

t = bs.decode(encoding="US-ASCII")
print(t, type(t))