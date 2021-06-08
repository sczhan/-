# import time
#
#
# def id_attestation(st: str) -> bool:
#     if len(st) != 18 or not st[0].isdigit() or st[0] == 0:    # 判断 开头, 长度
#         return False
#     if (not st[-1].isdigit() and st[-1] != 'X') or not st[1:-1].isdigit():    # 判断结尾
#         return False
#     try:                                                        # 生日是否合法
#         time.strptime(st[6:14], '%Y%m%d')
#     except ValueError:
#         return False
#     a = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
#     n = sum([int(a[i]) * int(st[i]) for i in range(len(a))])
#     r = n % 11
#     dt = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
#     t = dt[r]
#     if t != st[-1]:                     # 判断身份证最后一位校验码是否正确
#         return False
#     return True
#
#
# if __name__ == '__main__':
#     print(id_attestation('320721199804245211'))


import time


def id_attestation(st: str) -> bool:
    if len(st) != 18 or not("1" <= st[0] <= "9"):
        return False
    if not(st[-1].isdigit() or st[-1] == "X"):
        return False
    if not(st[:17].isdigit()):
        return False
    try:
        time.strptime(st[6:14], "%Y%m%d")
    except:
        return False
    a = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    r = sum([int(a[s]) * int(st[s])for s in range(17)]) % 11
    tail = "10X98765432"
    return tail[r] == st[-1]


if __name__ == '__main__':
    t = id_attestation('320721199804245210')
    print(t)
