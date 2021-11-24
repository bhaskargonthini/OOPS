#  in python constructor overloading is not possible, if we try to retrieve constructor overloading, the last constructor
# will get executed
# class Test():
#     def __init__(self, a):
#         print('one argument')
#     def __init__(self, a, b):
#         print('Two arguments')
#  t = Test()
# t = Test(10,20)
# similar to method overloading constructor overloading can be done in python by default arguements and
# keyword arguments
# constructor overloading with efault arguments
# class Test():
#     def __init__(self, a = None, b = None, c = None, d = None):
#         print('Need one or more arguements')
# t = Test()
# t = Test(10,20)
# t = Test(10,30,40)

class Test():
    def __init__(self, *a):
        print('Constructor overloading with keyword arguments')
t = Test()
t = Test(10)
t = Test(10,20)
t = Test(10,20,50,89)