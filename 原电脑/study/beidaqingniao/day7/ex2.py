def check_email(email: str):
    # number_a = email.count("@")                                                 # @的数量
    # index_a = email.find("@")                                                   # @的位置
    # number_dot = email.count(".")                                               # "." 的数量
    # index_dot = email.find(".")                                                 # ".' 的位置
    # underline = email[index_a:].count("_")                                      # @之后"_" 的数量
    # q_email = email[:index_a].replace("_", "a")                                 # 将@之前的"_"替换
    # q_email = q_email.encode("US-ASCII", errors="replace").decode("US-ASCII")   # 将@之前的字符进行编码 ASCII (防止有汉字) ASCII进行解码
    # h_email = email[index_a + 1:].replace(".", "a")                             # 将@之后的"."替换
    # h_email = h_email.encode("US-ASCII", errors="replace").decode("US-ASCII")   # 将@之后的字符进行编码 ASCII (防止有汉字) ASCII进行解码
    # if number_a == 1 and 0 < index_a < len(email) - 1 and number_dot == 1 and underline == 0 \
    #         and index_a + 1 < index_dot < len(email) - 1:                          # 判断
    #     if q_email.isalnum() and h_email.isalnum():                                # 判断
    #         return True
    #     return False
    # return False
    at1 = email.find("@")
    at2 = email.rfind("@")
    if at1 != at2 or 0 == at1 or at1 == len(email) - 1:
        return False
    p = email[: at1]
    l = [ch for ch in p if ch.isdigit() or ("a" <= ch.lower() <= "z") or ch == "_"]
    if len(p) != len(l):
        return False
    drop = email.find(".")
    drop2 = email.rfind(".")
    if drop == at1 + 1 or drop == len(email) - 1 or drop != drop2:
        return False
    return True


if __name__ == '__main__':
    a = check_email("15a_bDc@qq.com")
    print(a)
