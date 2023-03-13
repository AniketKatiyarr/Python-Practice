#simple handling exception

a = input("Enter a number")
try:
    a = int(a)
    print("You entered integer value")
except Exception as e:
    print(e)
    print("please....!! Enter integer value")
    
 
 
#handling with given values  



try:
    a = int(input("enter no"))
    c = 1/a
    print(c)
except ValueError as e:
    print(e)
    print("enter correct value")
except ZeroDivisionError as e:
    print("enter greater than 0")
print("thanks")


#raise exception by ourself

def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("not good")

a = increment('dba939')
print(a)

  
 
