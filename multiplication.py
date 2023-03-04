#1 mutiply of tables given by users
num = int(input("enter your number"))
for i in range(1,11):
    print(str(num) + "X" + str(i) + "=" + str(i*num))
    
#2 greet

li = ["harry","sohan","sahil","rahul"]
for name in li:
    if name.startswith("s"):
        print("good morning" + name)
        
        
#3 factorial problems


num = int(input("enter the number"))
factorial = 1
for i in range (1,num+1):
    factorial = factorial*i
    print(factorial)
         