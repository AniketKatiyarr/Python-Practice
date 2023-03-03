#a="1200"
#a=int(a)
#print(type(a))
#print(a+100)

#check for crrent thread
import threading 
t = threading.current_thread().getName()
print("gfgfg") 
print(t)

#create a thread 
#thread class of threading is used to create thread. to create our own thread we
#need to create a object of thread class

#1. create a thread without using a class
from threading import thread
t = thread(target = function,args = (arg1,arg2))
t = Thread(target = disp,args = (10,20))

#start of thread

from threading import Thread
def disp(a,b):
   print("thread running",a,b)
t  = Thread(target =disp,args = (10,22)) 
t.start()


from threading import Thread
def disp(a,b):
   print("thread running",a,b)
for i in range (5):
  t  = Thread(target =disp,args = (10,22)) 
  t.start()
  
from threading import Thread
def des():
    for i in range(5):
        print(":chile mile")
t = Thread(Target =des )
t.start()
for i in range(5):
    print("main thread") 
    
 
 #set and get name
from threading import thread , current_thread

def disp():
    print("child",current_thread())
t = Thread(target = disp) 
t.start()

print("main thread, ", current_thread())    

#get name
from threading import thread , current_thread

def disp():
    print("child",current_thread.getName())
    current_thread.setName('olil')
t = Thread(target = disp) 
t.start()

print("main thread, ", current_thread().getName())
current_thread.settName('lalal') 

#create  a threa a child class to thread clss
from threading import Thread
class childclass(Thread):
    pass
t = childclass()
print(t.name)
    


