import os
import stat
rt = os.access("other.txt", os.F_OK | os.W_OK | os.R_OK | os.X_OK)
print(rt)
os.chmod("other.txt", stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
rt = os.access("other.txt", os.F_OK | os.W_OK | os.R_OK | os.X_OK)
print(rt)

src_path = "F:\北大青鸟\讲义\day1"
lt = os.listdir(src_path)
for p in lt:
    full_path = src_path + "\\" + p
    print(full_path)
    try:
        f = open(full_path, 'a')
    except:
        print(full_path+' is 文件夹')
    print(f.tell())
