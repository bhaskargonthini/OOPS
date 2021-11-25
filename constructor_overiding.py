# class parent:
#     def __init__(self):
#         print('parent clss constructor')
# class child:
#     def __init__(self):
#         print('child class constructor')
# c = child()
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class employee(person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
    def display(self):
        print('employee name:', self.name)
        print('employee age:', self.age)
        print('employee  no:', self.eno)
        print('employee salary:', self.esal)
e1 = employee('Durga',48,872425,26000)
e1.display()
e2 = employee('Sunny', 39,872426, 36000)
e2.display()