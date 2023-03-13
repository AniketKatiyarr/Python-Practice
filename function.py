#1easy funtion 1
from unicodedata import name


marks = [23,34,45,56,78,]
average1 = (sum(marks)/500)*100

marks2= [23,34,65,43,23]  
average2 = (sum(marks2)/500)*100

print(average1,average2)

#2 function

def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [23,34,45,67]
percentage1 = percent(marks1)

marks2 = [99,98,8,75]
percentage2 = percent(  marks2)

print(percentage1,percentage2)


#3 
def greet(name):
    print("good mroning,"+ name)
    return

greet("haeelp")

#4 function of sum
def mysum(num1,num2):
    return(num1+num2)
s = mysum(60,40)
print(s)

#4 count the numbers
def len(corona):
    count = 0 
    for i in corona:
        count+=1
        
    return count
l = [1,2,3,4,55,6,7,34,56,7,8]
l2 =[8,4,53,34,67,98,6,33,22,56,86,32]


print(len(l))
print(len(l2))




