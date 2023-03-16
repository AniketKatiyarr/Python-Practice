class square:
     side = 20
sq1 = square()
sq2 = square()
print(sq1.side + sq2.side)


class  Number:
    def sum(self):
        return self.a + self.b
num = Number()
num.a = 30
num.b = 20
s = num.sum()
print(s)


class RailwayForm:
    formtype = "Railway Type"
    def pri(self):
        print(f"name is{self.name}")
        print(f"age is{self.age}")

appl = RailwayForm()
appl.name = "Ani"
appl.age = "65"
appl.pri()

