n = input("请输入月份: ")    # 接收用户输入的月份
d = input("请输入日期: ")    # 接收用户输入的日期
date = int(d)                # 将日期转化成int
data = {1: 0 + date, 2: 31 + date, 3: 59 + date, 4: 90 + date, 5: 120 + date, 6: 151 + date,
        7: 181 + date, 8: 212 + date, 9: 243 + date, 10: 273 + date, 11: 304 + date,
        12: 334 + date,
        }
print("这是一年中的第{}天".format(data[int(n)]))



