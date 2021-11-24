class Test():
    def sum(self, *a):
        total  = 0
        for x in a:
            total = total+x
        print('sum is:', total)
t = Test()
t.sum(10,20,30,4,55)
t.sum(11)
t.sum(11,44,33)
t.sum()