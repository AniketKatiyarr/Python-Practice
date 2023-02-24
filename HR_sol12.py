x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+k+j)!=n:
                l.append([i,k,j])
print(l)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

l = list()
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != 0:
                l.append([i,j,k])
print(l)
            
x = int(input())
y = int(input())
z = int(input())
n = int(input())

a = [[x,y,z]  for i in range(x+1) for j in range(y+1) for k in range (z+1) if (i+j+k)!= n]

print(a)