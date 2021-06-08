# from __future__ import print_function, division
# import tensorflow as tf
#
# tf.compat.v1.disable_eager_execution()
# x = tf.compat.v1.placeholder(dtype=tf.float32, name="x")
# # b = tf.constant(3, name="b")
# a = tf.constant(2.0, name="a")
# b = tf.constant(3, dtype=tf.float32, name="b")
#
# # b = tf.compat.v1.placeholder(tf.float32, name="b")
#
# y1 = a*x + b
# y2 = tf.add(x, b, name="add_op")
#
# sess = tf.compat.v1.Session()
#
# print(sess.run(y1, feed_dict={
#     x: 3
# }))
# print(sess.run(y2, feed_dict={
#     x: 3
# }))
# from random import random
# print("产品名称： 排球比赛模拟分析器")
# print("产品概述： 通过输入2个队伍A和B的能力值(0到1之间的小数表示)，能够模拟多次2个队伍A和B的排球竞技比赛，从而得出各自的胜率！")
#
# def getInputs():
#     '''
#     function: 获得用户输入的参数
#     '''
#     while True:
#         try:
#             probA = eval(input("请输入队伍A的能力值(0~1)："))
#             probB = eval(input("请输入队伍B的能力值(0~1)："))
#             if probA < 1.0 or probB < 1.0:
#                 n = eval(input("请输入需要模拟比赛的场次数："))
#                 break
#             print("请输入0-1之间的数值")
#         except Exception as e:
#             print("输入的数值类型不对", e)
#     return probA, probB, n
#
#
# def simNGames(n, probA, probB):
#     '''
#     function: 模拟n场比赛
#     n: 模拟n场比赛
#     probA, probB: 分别为队伍A和B的能力值
#     winA, winB: 队伍A和B在一场比赛中获胜的局数
#     winsA, winsB: 队伍A和B赢得比赛的场数，总共n场
#     '''
#     winsA, winsB = 0, 0
#     for _ in range(n):
#         winA, winB = simOneGame(probA, probB)
#         if winA > winB:
#             winsA += 1
#         else:
#             winsB += 1
#     return winsA, winsB
#
# def simOneGame(probA, probB):
#     '''
#     function: 模拟一场比赛，包括五局，采取五局三胜制
#     probA, probB： 分别为队伍A和B的能力值
#     return: 返回队伍A和B在本场比赛中获胜的局数
#     scoreA, scoreB: 分别为队伍A和B一局比赛获得的分数
#     winA, winB: 分别为队伍A和B一场比赛获胜的局数
#     '''
#     n = 1 # 代表本次比赛的局次
#     winA, winB = 0, 0
#     for _ in range(5):
#         scoreA, scoreB = simNGame(n, probA, probB)
#         if scoreA > scoreB:
#             winA += 1
#         else:
#             winB += 1
#         n += 1
#         if winA == 3 or winB == 3:
#             break
#     return winA, winB
#
# def simNGame(n, probA, probB):
#     '''
#     function: 模拟一局比赛
#     N: 代表本次比赛的局次
#     probA, probB： 分别为队伍A和B的能力值
#     return: 返回队伍A和B在本局比赛中获得的分数
#     '''
#     scoreA, scoreB = 0, 0    # 分别为队伍A和B一局比赛获得的分数
#     serving = 'A'            # 发球方
#     while not GameOver(n, scoreA, scoreB):
#         if serving == 'A':
#             if random() > probA:
#                 scoreB += 1
#                 serving = 'B'
#             else:
#                 scoreA += 1
#         if serving == 'B':
#             if random() > probB:
#                 scoreA += 1
#                 serving = 'A'
#             else:
#                 scoreB += 1
#     return scoreA, scoreB
#
# def GameOver(n, scoreA, scoreB):
#     '''
#     function: 定义一局比赛的结束条件
#     N: 代表当前局次(第五局为决胜局)
#     return: 若比赛结束的条件成立返回真，否则为假
#     '''
#     if n <= 4:
#         return (scoreA>=25 and abs(scoreA-scoreB)>=2) or (scoreB>=25 and abs(scoreA-scoreB)>=2)
#     else:
#         return (scoreA>=15 and abs(scoreA-scoreB)>=2) or (scoreB>=15 and abs(scoreA-scoreB)>=2)
#
# def printResult(n, winsA, winsB):
#     '''
#     function: 输出模拟比赛的结果
#     '''
#     print("竞技分析开始，共模拟{}场比赛。".format(n))
#     print(">>>队伍A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
#     print(">>>队伍B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
#
# def main():
#     probA,probB,n=getInputs()
#     winsA,winsB=simNGames(n,probA,probB)
#     printResult(n,winsA,winsB)
#
#
# if __name__ == '__main__':
#         main()
