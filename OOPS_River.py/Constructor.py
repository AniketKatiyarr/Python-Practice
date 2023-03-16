#used in __init__function

class employee:
    company = "Google"
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        print("Hello, good morning sir")
    def getdetails(self):
       print(f"name {self.name}")
       print(f"name {self.age}")
       
    def getsalary(self):
        print(f"salary of this employee wroking in {self.company} is approx {self.salary}")
        
Aniket  = employee("100000",100)
Aniket.getdetails()

