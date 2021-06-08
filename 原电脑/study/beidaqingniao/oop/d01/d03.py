# 多重继承


class A:
    def say(self):
        print("is class A say")

    def intro(self):
        print("is class A intro")


class B:
    def say(self):
        print("is class B say")

    def intro(self):
        print("is class B intro")


class C(B, A):
    # 方法重写
    def say(self):
        A.say(self)


if __name__ == '__main__':
    c1 = C()
    c1.say()
    c1.intro()