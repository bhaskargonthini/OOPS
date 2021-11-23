#job of destructor is not to destroy object and it is just to perform clean up activities
class Test:
    def __init__(self):
        print('constructor execution')
    def __delattr__(self):
        print('destructor execution')
t = Test()
t1 = Test()