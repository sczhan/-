import os


def read_prop(st: str) -> dict:
    if not(os.access(st, os.F_OK)):                               # 判断文件是否存在
        return None
    fr = open(st, "r", encoding="UTF-8")                          # 读取
    dt = {}
    while True:
        row = fr.readline()                                       # 读取一行是空白的话而不是\n的话,结束循环
        if row == "":
            break
        if row[0] != "#" and row != "\n":                         # 判断是不是注释或者空行
            d = row.split("=")
            dt.update({d[0].strip(): d[1].strip()})               # 更新到字典当中
    fr.close()                                                    # 关闭文件
    return dt                                                     # 返回


if __name__ == '__main__':
    a = read_prop("demo.prop")
    print(a)
