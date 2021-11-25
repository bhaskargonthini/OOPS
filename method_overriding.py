class parent:
    def property(self):
        print('Land+Gold+Cash+other')
    def marry(self):
        print('marry Appalamma')
# class child(parent):
#     def marry(self):
#         print('marry sruthi')
class child(parent):
    def marry(self):
        super(child, self).marry()
        print('marry sruthi')
c = child()
c.property()
c.marry()