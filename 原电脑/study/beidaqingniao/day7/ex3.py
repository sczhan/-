def st_sum(st: str):
    # st = st.lower()     # 将所有字符小写
    # sum = 0             # 字符的数值和
    # index = 0           # 下标
    # while index < len(st):
    #     sum += ord((st[index])) - 96   # 利用ord将每一个字符转换成对应的ASCII码
    #     index += 1
    return sum([ord(i) - 96 for i in st.lower()])                     # 返回 sum


if __name__ == '__main__':
    a = st_sum("Zelle")
    print(a)
