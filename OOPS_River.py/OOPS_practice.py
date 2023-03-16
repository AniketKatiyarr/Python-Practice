#1 
class programmer:
   company = "Microsoft"
   def __init__(self,name,product):
       self.name = name
       self.product = product
   def getinfo(self):
       print(f"the company is {self.company} and the name of employee is {self.name} and product is {self.product}\n")

Aniket = programmer("Aniket", "Perfume")
Raghav = programmer("Raghav","Lens")

Aniket.getinfo()
Raghav.getinfo()
               
#2

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

#3
class hero:
    a = "Aniket katiyar"
    
obj = hero() 
obj.a = "Vikky"

print(obj.a)
print(hero.a)   

#4

class calculator:
    def __init__(self,num):
        self.number = num
    
    def square(self):
        print(f"the square of {self.number}  is {self.number**2}")
    def squareroot(self):
        print(f"the square of {self.number}  is {self.number**0.5}")
    def cube(self):
        print(f"the cube of the {self.number} is {self.number **3}") 
    @staticmethod
    def greet():
        print("hello u are doing well keep it up")

a = calculator(3) 
a.square()
a.squareroot()
a.cube() 
a.greet()           