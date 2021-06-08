import random
# lt = [i for i in range(1, 53)]
# lt2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# lt3 = ["黑桃", "红桃", "梅花", "方片"]
# black_peck = [x + y for x in lt3 for y in lt2]
# dt = {i: black_peck[i - 1] for i in lt}
# b = random.shuffle(lt)
# play1, play2, play3, play4 = lt[::4], lt[1::4], lt[2::4], lt[3::4]
# play1.sort(), play2.sort(), play3.sort(), play4.sort()
# print("玩家1的牌是:\n" + "  ".join([dt[i] for i in play1]))
# print("玩家2的牌是:\n" + "  ".join([dt[i] for i in play2]))
# print("玩家3的牌是:\n" + "  ".join([dt[i] for i in play3]))
# print("玩家4的牌是:\n" + "  ".join([dt[i] for i in play4]))


def poke(j: int):
    a = ["黑桃", "红桃", "梅花", "方片"]
    b = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return str(a[(j - 1) // 13]) + str(b[(j - 1) % 13])


num = [i for i in range(1, 53)]
# num = random.shuffle(num)
num.sort(key=lambda x: random.random())


for i in range(1, 5):
    plays = {}.fromkeys(["玩家" + str(i) + "的牌是"])
    plays_poker = num[i - 1::4]
    plays_poker.sort()
    plays["玩家" + str(i) + "的牌是"] = plays_poker
    print("玩家" + str(i) + "的牌是: ")
    for p in plays["玩家" + str(i) + "的牌是"]:
        print(poke(p), end=" ")
    print()
