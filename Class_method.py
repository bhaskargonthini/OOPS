#class method
# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls, name):
#         print('{} walks with {} legs....' .format(name,cls.legs))
# Animal.walk('dogs')
# Animal.walk('goat')
#program to find number of objects creted for a class
class Test:
    count = 0
    @classmethod
    def __init__(self):
        Test.count = Test.count+1
    @classmethod
    def number_of_Object(cls):
        print('Number of Objects created ', cls.count)
t1 = Test()
t2 = Test()
t3 = Test()
Test.number_of_Object()