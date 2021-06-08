# 测试继承
from beidaqingniao.oop.d01.d01 import Person


class Student(Person):
    def __init__(self, name="Tom", age=16, score=60):
        Person.__init__(self, name, age)
        self.score = score

    def show_score(self):
        print( __class__.name)

    # @property
    # def score(self):
    #     return self.__score__
    #
    # # setter方法
    # @score.setter
    # def score(self, score):
    #     if 0 <= score <= 100:
    #         self.__score__ = score
    #     else:
    #         self.__score__ = 0


if __name__ == '__main__':
    st1 = Student(score=-70)
    print(Student.name)
    # st1.intro()
    # st1.show_score()