import pandas as pd

file = pd.DataFrame(pd.read_excel("5月工时.xls", usecols="D"))

# row = np.shape(file)[0]
# print(file, row)
#

# print(file["Unnamed: 3"].unique())
for i in file["Unnamed: 3"].unique():
    print(i)
# def zhhex(vol):
#     data = hex(vol).replace("0x", "").upper()
#     return data
# # #
# # #
# # # file["Alarm CODE"] = file["Alarm CODE"].apply(zhhex)
# # # # print(file, type(file))
# # # print(file)
# # # pd.DataFrame(file).to_excel("2.xlsx", sheet_name="Alarm", )
# #
# # # i = 1
# # # print(hex(1065).replace("0x", ""))
# # import openpyxl
# #
# # # 加载 excel 文件
# # # wb = openpyxl.load_workbook('EQProfile_20201119.xlsx')
# # #
# # # # 得到sheet对象
# # # sheet = wb['Alarm']
# # # print(sheet["1"])
# # # # sheet['A1'] = '修改一下'
# # # #
# # # # ## 指定不同的文件名，可以另存为别的文件
# # # # wb.save('income-1.xlsx')
# # # import pandas as pd
# # #
# # # file = pd.read_excel("EQProfile_20201119.xlsx")
# # # for i in file:
# # #     print(i)
# # # df1 = pd.read_excel(r'EQProfile_20201119.xlsx')
# # #
# # # with pd.ExcelWriter('3.xlsx') as writer:
# # # 	# df1.to_excel(writer, sheet_name='Sheet_name_1')
# # # 	print(writer.sheets)
# # # 	# df2.to_excel(writer, sheet_name='Sheet_name_2')
# # # # writer.save()
# # import openpyxl                                                #引入excel的操作模块
# # wb = openpyxl.load_workbook('EQProfile_20201119.xlsx')                    #读取excel文件
# #
# # #功能1：打印工作表名称
# # sheet_name = wb.sheetnames                                     #下面的代码等价于 sheet_name
# # #                                                                # = wb.get_sheet_names()
# # #                                                                #注意get_sheet_names这个函数在新版python                                                       #中已经不使用了
# # wb.close()
# # # # with pd.ExcelWriter('4.xlsx') as writer:
# # # # for i in sheet_name:
# # # #     file = pd.read_excel('EQProfile_20201119.xlsx', sheet_name="".format(i))
# # # #     print(file)
# # #     # file.to_excel(writer, sheet_name=i)
# # #
# # for i in sheet_name:
# #     print(i)
# #     file = pd.read_excel('EQProfile_20201119.xlsx', sheet_name="".format(i))
# #
# #     print(file)
# #     file.clear()
# import xlwings as xw
#
# Excel = xw.App(visible=True, add_book=False)
# Excel.display_alerts = False
# Excel.screen_updating = False
# # 开始Excel程序，定义打开文档格式
#
# ExcelFile = Excel.books.open("EQProfile_20201119.xlsx")
# sheet = ExcelFile.sheets['Alarm']
# # 读取具体文档，表格
#
# mail = sheet.range('A2').expand("down").value
# # 读取某列数据
# print(mail)
# # extract_qq = []
# hexlist = []
# for i in mail:
#     hex16 = hex(int(i)).replace("0x", "").upper()
#     hex16 = str(hex16)
#     hexlist.append(hex16)
# #
#
# # print(hex16)
# # 使用range().api.NumberFormat = XXX即可修改格式
# """
# range('A1:A10').api.NumberFormat = "@"  #设置为文本格式
# range('A1:A10').api.NumberFormat = "0.0"  #设置为小数格式
# range('A1:A10').api.NumberFormat = "yyyy-mm-dd"  #设置为"-"连接的日期格式
#
# """
# sheet.range('E:E').api.NumberFormat = "@"
# sheet.range('E2').options(transpose=True).value = hexlist
# # # 写入表格，列表使用transpose将自动填成一列
# #
# ExcelFile.save()  # 保存文档
# ExcelFile.close()  # 关闭文档
# Excel.quit() #停止excel程序
