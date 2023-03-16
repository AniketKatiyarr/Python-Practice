#class definition
 
class square():
    side  = 14
    
    def function(self):
        print("This is square")
        
sq = square()
    
print(sq.side) # accessing variable side of class
sq.function ()    # calling method description() of class



class square():
    def func(self,side):
        return side*4

sq1 = square()
print(sq1.func(10))

sq2 = square()
print(sq2.func(20))   
    
