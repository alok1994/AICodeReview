class A:
    def __init__(self, firstName):
        self.firstName = firstName
    
    def printName():
        print('First Name:', self.firstName)
Class B(A):
    def __init__(self, secondName):
        self.secondName = secondName
        A.__init__(self, firstName)
    def printFullName(self):
        print('Full name:', self.firstName, self.secondName)

a = A()
a.printName()
