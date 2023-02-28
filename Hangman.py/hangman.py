from random import randint

#k = randint(2,100)

avengers = ["black panther","captain america","Hulk","thor","iron man","ant man","vision","black widow"]
l= len(avengers)
k = randint(0,l)
print(avengers[k])
s = ""
for i in avengers[k]:
    if i ==' ' or i=='a' or i =='o' or i=='i'or i=='u':
       s+=i 
       s+= " "
       continue
    s+= "- "
print(s)