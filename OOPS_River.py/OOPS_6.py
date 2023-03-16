#class attributes
class employee:
    company ="Google"
    
Aniket = employee()
Risabh = employee()
print(Aniket.company)
print(Risabh.company)
Aniket.company   
employee.company = "Microsoft"
print(Aniket.company)
print(Risabh.company) 


#self attribute

class employee:
    company = "Google"
    def Gsalary(self):
        print(f"salary of this personn {self.company} is{self.salary}")
Aniket = employee()
Aniket.salary =  50000
Aniket.Gsalary()
          
              
        
        
    