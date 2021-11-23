#Static methods, inside static methods we wont provide self or cls arguments at the time of declaration
class Test:
    #static method declaration
    @staticmethod
    def add(x,y):
        print('sum is:', x+y)
    @staticmethod
    def mul(x,y):
        print('mul is:', x*y)
Test.add(10,20)
Test.mul(10,5)