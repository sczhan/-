score = []  # 创建空列表score
student_1 = [81]  # 学号1成绩
student_2 = [92]
student_3 = [85]
student_4 = [100]
student_5 = [55]
student_6 = [60]
student_7 = [16]
student_8 = [78]
student_9 = [95]
student_10 = [99]
score = student_1 + student_2 + student_3 + student_4 + student_5 + \
        student_6 + student_7 + student_8 + student_9 + student_10
# score.append(81)
# score.extend([81, 55, 65, 89, 98, 75, 56, 12, 13, 99])
print(score)
print(score[2])                 # 打印第3个元素的数值
print(score[:6])                # 打印 1~6 个元素的值
print(max(score))               # 打印最高分
print(min(score))               # 打印最低分
num = input("请输入分数: ")     # 输入num
print(int(num) in score)        # num是否在score中
student_score = input("请输入要查询的学号(1-10): ")
print("学号{}的成绩是: ".format(student_score), score[int(student_score)-1])   # 打印学号对应的值


