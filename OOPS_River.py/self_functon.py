class employee:
    company = "Google"
    def getsalary(self):
        print(f"salary of this employee wroking in {self.company} is approx {self.salary}")
        
Aniket  = employee()
Aniket.salary = 1000000
Aniket.getsalary() #automaticaly convert into 
#employee.getsalary(Aniket)


#two paramteres

class employee:
    company = "Google"
    def getsalary(self,signature):
        print(f"salary of this employee wroking in {self.company} is approx {self.salary}\n {signature}")
        
Aniket  = employee()
Aniket.salary = 1000000
Aniket.getsalary("Thanks")
