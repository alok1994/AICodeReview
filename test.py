class A:
    def __init__(self, firstName):
        self.firstName = firstName
    
    def printName():
        print('First Name: ', self.firstName)
class B(A):
    def __init__(self, secondName):
        self.secondName = secondName
        A.__init__(self, firstName)

a = A()
a.printName()
