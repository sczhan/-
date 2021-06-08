#
# class A(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def work(self):
#         print("monkey")
#
#
# class B(A):
#     def __init__(self, name, age, sex):
#         super().__init__(name, age, sex)
#
#     def work(self):
#         A.work(A)
#         super().work()
#         print("moo")
#         print(self.name, self.age, self.sex)
#
#
# b = B("kk", 18, "man")
# b.work()
# print(b.__dict__)
# print(A.__dict__)
# print(B.__dict__)
# print(A.__mro__)
# print(B.__mro__)
# print()

import tkinter
a = tkinter.Tk()
a.title("我爱你")
l = tkinter.Label(a, text="我爱刘梦")
l.pack()
ll =tkinter.Label(a, text="绿色", background="green")
ll.pack()
a.mainloop()
