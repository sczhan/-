import os

#
# def caesar_cipher(src: str, dest: str, offset: int) -> bool:
#     if not(os.access(src, os.F_OK))or os.access(dest, os.F_OK):         # 源文件不存在、目标文件存在
#         return False
#     if offset % 26 == 0:                                                # 偏移量是26的整倍数
#         return False
#     fr = open(src, "r", encoding="UTF-8")                               # 打开文件
#     fw = open(dest, "a", encoding="UTF-8")
#     while True:
#         row = fr.readline()
#         if row == "":                                                  # 读取一行是空白的话而不是\n的话,结束循环
#             break
#         if row == "\n":                                                # 读取\n的时候
#             fw.write("\n")
#         else:
#             for cs in row.lower().strip("\n"):                         # 去掉每一行的\n, 全部小写
#                 if cs == " ":                                          # 等于" " 就写入" "
#                     fw.write(" ")
#                 else:
#                     a = ord(cs) + offset                               # 与偏移量相加
#                     if a > 122:                                        # 大于122 时候就从97开始
#                         s = a - 26
#                         fw.write(chr(s))
#                     elif a < 97:                                       # 小于97  时候就从122开始
#                         s = a + 26
#                         fw.write(chr(s))
#                     else:                                              # 其他正常情况
#                         s = a
#                         fw.write(chr(s))
#             fw.write("\n")                                              # 写入换行
#     fr.close(), fw.close()                                              # 关闭文件
#     return True                                                         # 返回
#
#
# if __name__ == '__main__':
#     a = (caesar_cipher("saka3.txt", "saka4.txt", 6))
#     print(a)


def caesar_cipher(src: str, dest: str, offset: int) -> bool:
    if not(os.access(src, os.F_OK))or os.access(dest, os.F_OK):         # 源文件不存在、目标文件存在
            return False
    if offset % 26 == 0:                                                # 偏移量是26的整倍数
        return False
    def __cipher(ch):
        if "a" <= ch <= "z":

            return chr((ord(ch) - 97 + offset) % 26 + 97)
        if "A" <= ch <= "Z":
            return chr((ord(ch) - 65 + offset) % 26 + 65)
        return ch
    fr = open(src, "r", encoding="UTF-8")                               # 打开文件
    fw = open(dest, "a", encoding="UTF-8")
    fw.writelines(["".join([__cipher(ch) for ch in sline]) for sline in fr.readlines()])
    # s = []
    # for sline in fr.readlines():
    #     for ch in sline:
    #         if "a" <= ch <= "z":
    #             s.append(chr((ord(ch) - 97 + offset) % 26 + 97))
    #         elif "A" <= ch <= "Z":
    #             s.append(chr((ord(ch) - 65 + offset) % 26 + 65))
    #         else:
    #             s.append(ch)
    # fw.writelines(s)
    fr.close()
    fw.close()
    return True


if __name__ == '__main__':
    a = (caesar_cipher("saka.txt", "saka8.txt", 6))
    print(a)