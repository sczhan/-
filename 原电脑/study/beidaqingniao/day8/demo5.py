# import time
# from time import time, strftime
# from time import *
import time as t
print(t.time())

print(t.gmtime())
print(t.localtime())

print(t.strftime("%Y-%m-%d  %H-%M-%S", t.localtime()))
print(t.gmtime(1))
print(t.strftime("%Y-%m-%d  %H-%M-%S", t.gmtime(3600)))

print(t.localtime(1))
print(t.strftime("%Y-%m-%d  %H-%M-%S", t.localtime(3600)))

print("*" * 20)
print(t.ctime())
print(t.asctime())

print("*" * 20)
print(t.ctime(3600))
print(t.asctime(t.localtime(3600)))

print("*" * 20)
tm = t.strptime("2019/6/27 15:39:52", "%Y/%m/%d  %H:%M:%S")
print(tm)
print(t.asctime(tm))
print(t.ctime())
tm = t.strptime("2019/6/27", "%Y/%m/%d")
print(tm)
print(t.asctime(tm))