##use open function to  read the content of a file 
#
#f = open('sample.txt', 'r')
#data = f.read()
#print(data)
#f.close()
#
##2 f.readline
#
#f = open('sample.txt', 'r')
#data = f.readline()
#print(data)
#data = f.readline()
#print(data)
#f.close()
#
##3 f.open  
#f = open('sample.txt', 'a')
#d = f.write("by shree shree Aniket sir")
#print(d)

with open("sample.txt",'r') as f:
    print(f.tell())
    f.seek(10)
    print(f.read(5))
     
   