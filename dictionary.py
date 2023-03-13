mydic = {
    "first" : "hello sir" ,
    "second" : "good bye sir"
    
}

print(mydic['first'])
print(mydic['second'])


#keys method
print(mydic.keys())
print(type(mydic))
#values ,update
print(mydic.values())

#items
print(mydic.items())

#update
updatedic = {
    "hello" : "nohello",
    "no one" : "i am"
}
 
mydic.update(updatedic)
print(mydic)   

#
dic = ([(1,'key'), (2,'Numbers')])
print(dic)
