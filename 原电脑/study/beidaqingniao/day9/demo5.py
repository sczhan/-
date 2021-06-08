import os
import os.path as op

print(os.access("demo22.py", os.F_OK))
print(op.split("demo.py"))
t = op.split("demo.py")
print(op.splitext(t[1]))
s = op.split(r"F:\study\beidaqingniao\day9\demo.py")
print(s)