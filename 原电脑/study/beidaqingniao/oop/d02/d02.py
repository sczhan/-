class Preson:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"今年{self.age}岁"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            self.__age = 1

    def __add__(self, other):
        if isinstance(other, int):
            self.age += other
            return self
        else:
            raise ValueError("必须是正整数")


if __name__ == '__main__':
    p = Preson(20)
    print(p)
    p.age += 1
    print(p)
    p = p + 2
    print(p)