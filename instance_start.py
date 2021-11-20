

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # self.__secret = 'This is a secret attribute'
        # TODO: add properties
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        else:
            return self.price
        return self.price
    def setdiscount(self, amount):
        self._discount = amount

    # TODO: create instance methods


# TODO: create some book instances
b1 = Book("War and Peace", 'Leo Tolstoy', 1225, 39.95)
b2 = Book("The Catcher in the Rye", 'JD Salinger', 234, 29.95)

print(b1.getprice())
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())
# print(b2.__secret)
# prints error since __Var attribute is strongly private
# and cannot be accesed by the class
# __Var cannot be accessed by ther classes
# and display error if other classes try to access the variable
# we can access the __var by prefixing the with _classname__Var
# this is called nammangling to be accessed by same class but not other classes
# TODO: print the price of book1


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
