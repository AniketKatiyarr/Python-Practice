##def function(n):
 #   if i==0 or i==1:
 #           return 1
 #   else:
 #       return n*factorial(n-1)
 #   a = (int(input("enter")))
 #   print(a)
 #    
 
def funtion(n):
    product =1
    for i in range(n):
        product = product*(i+1)
        print(product)
        