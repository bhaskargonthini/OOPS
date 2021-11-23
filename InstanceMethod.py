class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
            print('Hi', self.name)
            print('Your Marks:', self.marks)
    def Grade(self,marks):
            if self.marks>= 60:
                print('First Class')
            elif self.marks>=50:
                print('Second Class')
            elif self.marks>=40:
                print('Third Class')
            else:
                print('Fail')
n = int(input('Enter number of Students:'))
# for i in range(n):
#     name = input('Enter name')
#     marks = int(input('Enter marks'))
#     S = Student(name,marks)
#     S.display()
#     S.Grade(marks)
#     print()
for i in range(n):
    name = input('Enter name')
    marks = int(input('Enter marks'))
    S = Student(name,marks)
    S.display()
    S.Grade(marks)
    print()