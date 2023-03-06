#def square(num):
#    return num*num

#l = [1,2,3,4,5,6]
#l2 = []
#
#for item in l:
#    l2.append(square(item))
#print(l2)

def square(num):
    return num*num

l = [1,2,3,4,5]
l2 = []

#2 method 
print(list(map(square,l))) #suqare is function and l is input list


#filter method

def greater(num):
    if num>5:
        return True
    else:
        False
g10 = lambda num:num>50
l = [1,2,3,4,5,5,6,7,8,9,7,65,44,33,45,66,2,4]
print(list(filter(greater,l)))
print(list(filter(g10,l)))


#reduce method

from functools import reduce
sum = lambda a,b:a+b
l = [1,2,3,4,5]
val = reduce(sum,l)
print(val)
#sequential computation

