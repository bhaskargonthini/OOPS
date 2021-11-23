class Apple:
    def myname(self):
        print('from class A')
class Ball:

    def myname(self):
        print('from class b')
class Cat:
    def myname(self):
        print('from class c')
class Doll:
    pass
print(Doll.__mro__)
print(Cat.mro())
