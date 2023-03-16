#class programmer:
#    company = "Microsoft"
#    def fun (self):
#        return self.product
#
#fun1 = programmer()
#fun1.product = "Harry"
#fun1.salary = 1000
#
#fun2 = programmer()
#fun2.product = "manas"
#fun2.salary = 100000
#
#print(fun1.programmer)
#print(fun2.programmer)
#

class calculator:
    def __init__(self,num):
        self.number = num
    
    def square(self):
        print(f"the square of {self.number}  is {self.number**2}")
    def squareroot(self):
        print(f"the square of {self.number}  is {self.number**0.5}")
    def cube(self):
        print(f"the cube of the {self.number} is {self.number **3}") 

a = calculator(3) 
a.square()
a.squareroot()
a.cube()
                