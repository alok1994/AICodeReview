class A:
    def __init__(self, firstName):
        self.firstName = firstName
    
    def printName():
        print('First Name:', self.firstName)
Class B(A):
    def __init__(self, secondName):
        self.secondName = secondName
        A.__init__(self, firstName)

    def printFirstSecondName(self):
        print("First and Second Name:", self.firstName, self.secondName)

a = A()
a.printName()
