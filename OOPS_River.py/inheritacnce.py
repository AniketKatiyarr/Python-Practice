# inhertiance or can say single inheritance
class employee:
    company = "Google"
    
    def showdetails(self):
        print("helllo, i am coder")
    
class programmmer(employee):
    lang = "Python"
    def getlang(self):
        print(f"Hello, i am a python programmer with {self.lang}")
    def showdetails(self):
        print("helllo, i am programmer")
a = employee()
a.showdetails()
b = programmmer() 
b.showdetails()
             
#Multiple inheritance 

class employee():
   company = "Google"
class freelancer():
    company = "Fever"
    level = 0
    def upgrade(self):
        self.level = self.level +1
class programmmer(employee,freelancer):
     name = "Vikky"

p = programmmer()
p.upgrade()
print(p.level)

# Multilevel Inheritance

class person:
    country = "London"
    def takebreak(self):
        print("I am a human so i take break") 

class employee(person):
    def takebreak(self):
        print("i am resource so i give u a chance to breadth")

class programmer(employee):
    def salary(self): 
      print(f"salary of employee {self.salary}")                       

p = person()
p.takebreak()
a = employee()
a.takebreak()
b = programmer()
b.takebreak()      


#super() method,

class person:
    country = "London"
    def takebreak(self):
       
        print("I am a human so i take break") 

class employee(person):
    def takebreak(self):
        
        print("i am resource so i give u a chance to breadth")

class programmer(employee):
    def salary(self): 
         super().takebreak()
    print("hello i am stuck")                       

p = person()
p.takebreak()
a = employee()
a.takebreak()
b = programmer()
b.takebreak()     
 
  