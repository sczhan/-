# 定义一个Person类


class Person:
    # 成员变量
    # name = "mike"
    # age = 20

    def eat(self):
        print(self.__name + " is am eating")

    def intro(self):
        print(f'{self.__name}今年{self.__age}岁')

    def __init__(self, name="mike", age=20):
        self.__name = name
        self.age = age

    # getter 方法
    @property
    def name(self):
        return self.__name

    # setter方法
    @name.setter
    def name(self, name):
        self.__name = name

    # getter 方法
    @property
    def age(self):
        return self.__age

    # setter方法
    @age.setter
    def age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            self.__age = 1


if __name__ == '__main__':
    p = Person()
    print(p.name)
    p.eat()
    p.intro()
    p.name = "jj"
    p.intro()
    print("*" * 20)
    q = Person(name="jerry", age=23)
    q.name = "w"
    q.age = -23
    q.intro()
    print(q.name)
    q.eat()