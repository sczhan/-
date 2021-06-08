# import random
#
# lt = [i for i in range(0, 101)]
# random_num = random.choice(lt)    # 生成随机数
# num__t = 0                        # 猜的次数
#
# while True:
#     num__t += 1
#     num = int(input("请输入一个数字: "))
#     if num < random_num:
#         print("猜小了, 你猜了{}次\n".format(num__t))
#     elif num > random_num:
#         print("猜大了, 你猜了{}次\n".format(num__t))
#     else:
#         print("猜对了, 你猜了{}次. 这个随机数是{}".format(num__t, random_num))
#         break


import random

import beidaqingniao.shuruhanshu.shuru as ex


def guess_number():
    low = 1
    high = 100
    random_number = random.randint(low, high)
    print(random_number)
    count = 0
    while True:
        user_guess = ex.accept_int(low, high)
        count += 1
        if random_number == user_guess:
            print(f'猜对了，猜了{count}次。')
            break
        if random_number < user_guess:
            print('大了, 请输入{} - {}之间的整数, 猜了{}次'.format(low, user_guess - 1, count))
            high = user_guess-1
        else:
            print('小了, 请输入{} - {}之间的整数, 猜了{}次'.format(user_guess + 1, high, count))
            low = user_guess+1


if __name__ == '__main__':
    guess_number()