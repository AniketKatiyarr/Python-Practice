class square():
    def func(self):
        return self.side*4
sq1 = square()
sq1.side = 10
print(sq1.func())

sq2 = square()
sq2.side =20
print(sq2.func())