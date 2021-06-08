def abbreviation(n: str):                  # 定义一个函数
    # t = n.split(" ")                       # 将参数分割成字符串列表
    # index = 0                              # 索引
    # abbreviations = ""
    # while index < len(t):
    #     abbreviations += t[index][0].upper()      # 每个字符串的首字母大写
    #     index += 1
    # return abbreviations                          # 返回字符串的首字母缩写
    return "".join([i[0] for i in n.split()]).upper()

if __name__ == '__main__':
    a = abbreviation("center process unit")
    print(a)
