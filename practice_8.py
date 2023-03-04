#1 greatest of all number
 #def great(a,b,c):
#if(a>b):
#        if(a>c):
#            return a
#        else: 
#            return c
#else:
#        if(b>c):
#            return b
#        else:
#            return c
#m = great(90,98,1000 )
#print("the value is greater then rest of all three," + str(m))         

#2 convert celsius of forenite


def farh(cel):
    return (cel *(9/5)) + 32

c = 50
f = farh(c)

print("farehemit value is,\t", str(f))



#3 prevent a new line 
print("hello" ,end =" ")
print("how", end =" ")          
print("are", end =" ")
print("you", end = " ")
print("?", end = " ")


#4 recursive function to calculate the sum of first n natural number

def sum(n):
    if n<=1:
        return n
    else:
        return n + sum(n-1)

num = 100

if num <0:
    print("enter positive number")
else:
    print("sum of natural number is,",sum(num) )


#5 n line of python * pattern


n =10
for i in range(n):
    print("*" * (n-i))
    
#6 convert inces to cms

def cent(centi):
    return centi/2.54
a = 50
p = cent(a)
print(p)
   

#7 strip and split at the same time


def remove_and_split(string,word):
    newstr  = string.replace(word, "")
    return newstr.strip()

this = "     aniket is good boy"
n = remove_and_split(this, "boy")
print(n)

#8 multiplication

def table(n):
    for i in range(0,11):
        print("table of ", n, "is =", n*(i+1))
        
a = 12
p =  table(a)
print(p)
 
        