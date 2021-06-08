score = [78, 56, 45, 98, 85, 65, 53]
average_s = sum(score)/len(score)  # 求出平均分
print(average_s)
min_diff = max(score)
diff_index = 0

for sc in score:
    diff = sc - average_s if average_s < sc else average_s - sc
    if diff < min_diff:
        min_diff = diff
        diff_index = sc

print(min_diff, diff_index)









