# import os
# import os.path as op
# size = []
# dt = {}
#
#
# def list_path(path: str):
#     while op.isdir(path):                                   # 判断path是否是目录
#         size.append(0)
#         son_files = os.listdir(path)                        # 打印出path包含的文件或文件夹
#         for son_file in son_files:
#             son_file = op.join(path, son_file)               # 与路径结合
#             if op.isfile(son_file):                         # 如果是文件的话添加到size
#                 size.append(op.getsize(son_file))
#             else:
#                 paths = son_file                            # 如果不是文件的话
#                 list_path(paths)                            # 调用函数 paths = son_file = path + "\\" + son_file 这是一个文件夹的路径
#         dt["size"], dt["num"] = sum(size), len(size)        # 添加字典
#         return dt                                           # 返回
#     return None
#
#
# if __name__ == '__main__':
#     a = list_path(r"F:\北大青鸟\讲义\day9")
#     print(a)
# 用os.walk()也可以
# import os
# import os.path as op
# size = []
# dt = {}
#
#
# def list_path(path: str):
#         son_files = os.walk(path)                        # 打印出path包含的文件或文件夹
#         for path, son_file,  files in son_files:
#             for file in files:
#                 file_path = path + "\\" + file
#                 size.append(op.getsize(file_path))
#         dt["size"], dt["num"] = sum(size), len(size)
#         return dt
#
#
# a = list_path(r"F:")
# print(a)

import os
import os.path as op


def list_path(path: str):
    if not os.access(path, os.F_OK) or not op.isdir(path):
        return None
    size = 0
    count = 1

    def __count_size_number(paths):
        files = os.listdir(paths)
        nonlocal size
        nonlocal count
        for file in files:
            count += 1
            if op.isfile(op.join(paths, file)):
                size += op.getsize(op.join(paths, file))
            if op.isdir(op.join(paths, file)):
                __count_size_number(op.join(paths, file))

    __count_size_number(path)
    return {"size": size, "num": count}


if __name__ == '__main__':
    a = list_path(r"F:\北大青鸟\讲义\day9")
    print(a)