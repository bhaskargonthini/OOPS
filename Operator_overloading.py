# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):
#         return self.pages+other.pages
# b1 = Book(250)
# b2 = Book(300)
# print('total no of pages:', b1+b2)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __gt__(self, other):
        return self.marks>other.marks
    def __lt__(self, other):
        return self.marks<=other.marks
print('10>20', 10>20)
S1 = Student('durga', 30)
S2 = Student('Malli', 40)
print('S1>S2', S1>S2)
print('S1<S2', S1<S2)
print('S1>=S2', S1<=S2)
print('S1<=S2', S1>=S2)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def __mul__(self, other):
#         return self.salary*other.days
# class Timesheet:
#     def __init__(self, name, days):
#         self.name  = name
#         self.days = days
# e = Employee('durga', 500)
# t = Timesheet('durga', 25)
# print("salary of the employee " f'{e.name} ' "is:", e*t)

