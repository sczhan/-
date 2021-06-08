#
# import re, time, os
# from urllib import request
# import requests
# import pandas as pd
# import xlwings as xw
# from openpyxl import load_workbook
#
#
#
# value = input("请输入证券分类: ")
# key = str(bytes(value, encoding="utf-8")).replace("\\x", "%").replace("b'", "").replace("'", "").upper()
# save_a = False
#
#
# def lianjie(key):
#     """
#     :param key: 输入关键字
#     :return: None
#     """
#     url = "http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchPageAPI.ashx?callback=jQuery18301" \
#           "9982303452915473_1608796013779&m=0&key={}&_=1608796014008".format(key)
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
#     }
#     rsp = request.Request(url, headers=headers)
#     rep = request.urlopen(rsp)
#     html = rep.read().decode()
#     counts = re.findall(r'"FundListTotalCount":\d*,', html)
#     global count
#     count = str(counts[0]).replace(",", "").split(":")[1]
#     if count == 0:
#         pass
#     else:
#         url = "http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchPageAPI.ashx?" \
#               "callback=jQuery18308281986363928_{0}&m=1&key={1}&pageindex=0&pagesize={2}&_={3}"\
#             .format(int(time.time()*1000), key, count, int((time.time()-10000)*1000))
#         html = requests.get(url, headers)
#     names = re.findall(r'"_id":.*?,"STOCKMARKET":""', html.text)
#     # print(names)
#     for name in names:
#         # print(name)
#         id = re.findall(r'"CODE":"\d{6}', name)[0].split('"')[3]
#         jjname = re.findall(r'"NAME":".*?"', name)[0].split('"')[3]
#         url = "http://fundgz.1234567.com.cn/js/{}.js?rt={}".format(id, int(time.time() * 100))
#         page(url, jjname, id)
#
# def page(url, name, id):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
#     }
#     html = requests.request(url=url, headers=headers, method="get")
#     guzhi = re.findall(r'"gszzl":".*?,"', html.text)
#     if guzhi != []:
#         # print(guzhi)
#         code = guzhi[0].split('"')[3] + "%"
#         # print(guzhi)
#     else:
#         code = "null"
#     # global jj_guzhi, jj_name
#     jj_name.append(name)
#     jj_guzhi.append(code)
#     jj_code.append(id)
#     # print(jj_guzhi, len(jj_code))
#     #
#     # save(jj_name, jj_guzhi)
#     # print(name, id, code)
#
#     # save(name, id, code)
#
#
# def save(name, id, code):
#     # Excel = xw.App(visible=True, add_book=False)
#     # Excel.display_alerts = False
#     # Excel.screen_updating = False
#
#     path = "{}{}.xlsx".format(value, time.strftime("%Y%m%d%H", time.localtime()))
#     s = pd.DataFrame(data={'基金名称': name, '基金代码': id, '估值': code, "时间": time.strftime("%Y-%m-%d %H:%M:%S",
#                                                                             time.localtime())})
#     if os.path.exists(path):
#         # print(os.path.exists(path))
#         # 开始Excel程序，定义打开文档格式
#         # book = load_workbook(path)
#         # writer = pd.ExcelWriter(path, engine='openpyxl')
#         writer = pd.ExcelWriter(path)
#         read = pd.read_excel(path)
#         read.to_excel(writer)
#         d = pd.DataFrame(data={'基金名': name, '基金代': id, '估': code, "时": time.strftime("%Y-%m-%d %H:%M:%S",
#                                                                             time.localtime())})
#         # d = pd.DataFrame(data=[name, id, code, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
#         # s.sort_values("估值", ascending=False, inplace=True)
#         print(read.shape[0], d)
#         d = d.reset_index(drop=True)
#         d.index += read.shape[0] + 1
#         d.to_excel(writer, startrow=read.shape[0]+1, sheet_name='sheet1', )
#         writer.save()
#     else:
#         s.sort_values("估值", ascending=False, inplace=True)
#         # s = s.sort_values("估值", ascending=False)
#         """
#         df=df.reset_index()
#         这时候会多出一列，多出的一列是原来index的内容
#         如果不想要多出一列的话（有时候 保留原来的index还是挺有用的）
#         df=df.reset_index(drop=True)"""
#         s = s.reset_index(drop=True)
#         s.index += 1
#         s.to_excel(path)
#     # print(s)
#
#
# if __name__ == "__main__":
#     count = 0
#     jj_name, jj_guzhi, jj_code = [], [], []
#     lianjie(key)
#     save(jj_name, jj_code, jj_guzhi)


from turtle import *


def go_to(x, y):
   up()
   goto(x, y)
   down()


def big_Circle(size):  #函数用于绘制心的大圆
   speed(10)
   for i in range(150):
       forward(size)
       right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
   speed(10)
   for i in range(210):
       forward(size)
       right(0.786)

def line(size):
   speed(1000)
   forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   left(150)
   begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   end_fill()

def arrow():
   pensize(10)
   setheading(0)
   go_to(-400, 0)
   left(15)
   forward(150)
   go_to(339, 178)
   forward(150)

def arrowHead():
   pensize(1)
   speed(10000)
   color('red', 'red')
   begin_fill()
   left(120)
   forward(20)
   right(150)
   forward(35)
   right(120)
   forward(35)
   right(150)
   forward(20)
   end_fill()


def main():
   pensize(2)
   color('red', 'pink')
   getscreen().tracer(1, 0) #取消注释后，快速显示图案
   heart(200, 0, 1)          #画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
   setheading(0)             #使画笔的方向朝向x轴正方向
   heart(-80, -100, 1.5)     #画出第二颗心
   arrow()                   #画出穿过两颗心的直线
   arrowHead()               #画出箭的箭头
   go_to(400, -300)
   write("小可爱：张丽雯", move=True, align="left", font=("宋体", 30, "normal"))
   done()

main()