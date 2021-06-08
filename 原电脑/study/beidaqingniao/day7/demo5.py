s = "   hello world    "
print(f"[{s}]")
t = s.lstrip()
print(f"[{t}]")

t = s.rstrip()
print(f"[{t}]")

t = s.strip()
print(f"[{t}]")


s = "   ###hello world***    "
t = s.strip(" #*").replace(" ", "")
print(f"[{t}]")

s = "hello world"
t = s.replace("l", "x", 2)
print(t)
t = s.replace("l", "x")
print(t)
