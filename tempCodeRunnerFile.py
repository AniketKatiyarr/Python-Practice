if __name__ == '__main__':
  
   n = int(input())
   i = map(int,input().split())
   tup = ()
   for x in i:
       tup += (x,)
       
   print(hash(tup))