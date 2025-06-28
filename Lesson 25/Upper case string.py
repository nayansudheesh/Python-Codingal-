class IOstring:
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("enter any string:")
    def printstring(self):
        print("Result is:" , self.str1.upper())
#create object
str1 = IOstring()

#calling
str1.getstring()
str1.printstring()
