# class Test():
#     def sum(self, a = None, b = None, c = None, d = None):
#         if(a!=None and b!=None and c!=None and d!=None):
#             print('sum is:', a+b+c)
#         elif(a!=None and b!=None):
#             print('sum is:', a+b)
#         else:
#             print('minimum two arguments is needed to do addition')
# t = Test()
# t.sum(10,20,30,40)
# t.sum(10,20)
# t.sum(10)

# class edpresso:
#     def Hello(self, Name = None):
#         if Name is not None:
#             print('Hello', Name)
#         else:
#             print('Hello')
# obj = edpresso()
# obj.Hello('Bobby')
# obj.Hello()

class Human:
    def sayhello(self, Name = None, Age = None):
        if Name is not None and Age is None:
            print('Hello '+Name)
        elif Name is not None and Age is not None:
            print('Hello '+Name+' Your Age is:', f'{Age}')
        else:
            print('Hello')
obj = Human()
obj.sayhello('Bobby')
obj.sayhello('Bhaskar',23)
obj.sayhello()
