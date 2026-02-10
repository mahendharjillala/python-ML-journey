class Parent:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show(self):
        print(self.name, self.age, self.marks)


class Student:
    def __init__(self, parent):
        self.parent = parent

    def show(self):
        self.parent.show()



P = Parent('Mahendhar', 20, 99)
s = Student(P)

P.show()
s.show()
