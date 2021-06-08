import os
import os.path as op


def get_new_file_name(dest: str, sno: str):
    rt = op.split(dest)
    tt = op.splitext(rt[1])
    if rt[0] == "":
        f_name = tt[0] + " " + str(sno) + tt[1]
    else:
        f_name = rt[0] + "\\" + tt[0] + " " + str(sno) + tt[1]
    return f_name


def copy_file(src: str, dest: str):
    if os.access(dest, os.F_OK):
        print(f"目标文件{dest}已存在, 请选择： ")
        choice = input("o-覆盖， c-取消， s-保留二者(o/c/s): ")
        if choice == "c":
            return
        if choice == "s":
            sno = 2
            while True:
                nf_name = get_new_file_name(dest, sno)
                if os.access(nf_name, os.F_OK):
                    sno += 1
                else:
                    break
            dest = nf_name
            print(dest)
    fr = open(src, "r", encoding="UTF-8")
    fw = open(dest, "w", encoding="UTF-8")
    while True:
        s1 = fr.readline()
        if s1 == "":
            break
        fw.write(s1)


if __name__ == '__main__':
    copy_file("demo1.py", "demo.py")
    f = open("4.txt", "r", )
    print(f)