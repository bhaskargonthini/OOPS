class Test:
    def m1(self):
        print('no arguments')
    def m1(self, a):
        print('one argument')
    # def m1(self, a, b):
    #     print('two arguments')
t = Test()
# t.m1()
t.m1(10)
# t.m1(10,20)