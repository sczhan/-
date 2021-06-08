import os
import pickle as pk


def save(file_name, data):
    try:
        f = open(file_name, "wb")
        pk.dump(data, f)
        f.close()
        print("保存数据成功")
        return True
    except:
        print("保存数据失败")
        return False


def load(file_name):
    if os.access(file_name, os.F_OK):
        f = open(file_name, "rb")
        data = pk.load(f)
        f.close()
    else:
        data = []
    return data


def account_int(msg="请输入一个整数: "):
    while True:
        try:
            n = input(msg)
            num = int(n)
            return num
        except ValueError:
            print("输入的不是整数， 请重新输入")


def account_float(msg="请输入一个数字: "):
    while True:
        try:
            n = input(msg)
            num = float(n)
            return num
        except ValueError:
            print("输入的不是数字， 请重新输入")