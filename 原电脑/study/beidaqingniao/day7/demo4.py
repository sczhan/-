lt = ["andy", "mike", "tom"]
t = "*".join(lt)
print(t)
tt = t.split("*")
print(tt)
tt = t.split("*", 1)
print(tt)

s = "\oos \oos"
t = s.replace(" ", "")
print(s)
print(t)

b = "Abc"
print(b.ljust(10, "*"))
print(b.rjust(10, "*"))