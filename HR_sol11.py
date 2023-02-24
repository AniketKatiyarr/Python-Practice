#x = int(input())
#y = int(input())
#z = int(input())
#n = int(input())
#l = []
#for i in range(x+1):
#    for j in range(y+1):
#        for k in range(z+1):
#            if(i+j+k) !=n:
#                l.append([x,y,z])
#print(l)
#
#def main():
#    x = int(input())
#    y = int(input())
#    z = int(input())
#    n = int(input())
#    a = [[x,y,z]  for i in range(x+1) for j in range(y+1) for k in range (z+1) if (x+y+z != n)]
#    print(a)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

l =[]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k)!=n:
               l.append([x,y,z])
print(l)