class A:
    def __init__(self, firstName):
        self.firstName = firstName
    
    def printName():
        print('First Name:', self.firstName)
Class B(A):
    def __init__(self, secondName):
        self.secondName = secondName
        A.__init__(self, firstName)
class C(B):
    def _init__(self):
        
a = A()
a.printName()
