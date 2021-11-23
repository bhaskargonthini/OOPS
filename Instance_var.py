# class Employee:
# inside a constructor by using self variable
#     def __init__(self):
#         self.id = 100
#         self.name = 'raghu'
#         self.sal = 60000
# e = Employee()
# print(e.__dict__)
# class Test:
# #instance variable can be declared inside instance method by using self variables
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def m1(self):
#         print(self.a)
#         print(self.b)
#         self.c = 30
# t = Test()
# t.m1()
# print(t.__dict__)
#instance variable can be declared outside of the class by using object reference variable.
# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 'bobby'
#         self.c = 50000
#     def m1(self):
#         self.c = 'bhaskar'
# t = Test()
# t.m1()
# t.d = 'hi'
# print(t.__dict__)
class Test:
    def __init__(self):
        self.name = 'bobby'
        self.salary = 50000
        self.a = 10
        self.b = 20
    def m1(self):
        del self.a
t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.b
print(t.__dict__)
