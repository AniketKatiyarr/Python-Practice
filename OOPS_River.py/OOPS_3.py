#class attributes access by the calss


class loop:
    leg = 200
print("Leg are:", loop.leg)


#new attribute define outside the class


class loop:
    leg = 200
print("Leg are:", loop.leg)

loop.hand = 50
print("Hands are:" , loop.hand)

#4

class complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginery = i
    def __add__(self,c):
        return complex(self.real + c.real, self.imaginery + c.imaginery)
    def __mul__(self,m):
        return complex(self.real * m.real, self.imaginery * m.imaginery)
    def __str__(self):
        return f"{self.real} + {self.imaginery}i"
    def __str__(self):
        return f"{self.real} * {self.imaginery}"
C1 = complex(1,3)
C2 = complex(2,4)
print(C1 + C2)
  
        