import os


def mask_four_letter_word(src: str, dest: str) -> bool:
    if not(os.access(src, os.F_OK))or os.access(dest, os.F_OK):           # 源文件不存在、目标文件存在
        return False
    fr = open(src, "r", encoding="UTF-8")                                 # 打开文件
    fw = open(dest, "w", encoding="UTF-8")
    fw.writelines([" ".join([word if len(word) != 4 else "****" for word in sline.split()]) + "\n"
              for sline in fr.readlines()])
    # while True:
    #     row = fr.readline()
    #     if row == "":                                                     # 读取一行是空白的话而不是\n的话,结束循环
    #         break
    #     words = row.strip("\n").split(" ")                                # 将每一行单词分割成单个单词
    #     for word in words:
    #         if len(word) != 4:                                            # 判断单词的长度
    #             fw.write(word)                                            # 写入
    #         else:
    #             word = "****"                                                # 替换
    #             fw.write(word)
    #         fw.write(" ")                                                 # 每一个单词一空格
    #     fw.write("\n")                                                    # 写完一行换行
    fr.close(), fw.close()                                                # 文件关闭
    return True                                                           # 返回


if __name__ == '__main__':
    a = mask_four_letter_word("word.txt", "5.txt")
    print(a)