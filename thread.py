import threading
t = threading.current_thread().getName()
print("hekko fbsk")
print(t)

#2 creating a thread without using a class

from threading import Thread
# thread_obj = Thread(target = function,args = (arfg2,arg2,arg3))
def disp(a,b):
    print("thread running",a,b)
for i in range(5):
 t = Thread(Target = disp,args = (10,20))
t.start()

#3. STart of thread
from threading import Thread
def disp(a,b):
    print("thread runninh",a,b)
for i in range(5):
  t  = Thread(target = disp,args = (10,20))
t.start()


from threading import Thread
def disp():
    for i in range(5):
     print("child thread")
t = Thread(target = disp)
t.start()

for i in range(5):
    print("main thread")

#get name and set name

from threading import Thread, current_thread
def disp():
    print("child thread", current_thread().getName())

t = Thread(target = disp)
t.start()
print("main thread", current_thread().getName()
      )

#set name    
from threading import Thread, current_thread
def disp():
    print("child thread", current_thread().getName())
    current_thread().setName('thread ka namm')
t = Thread(target = disp)
t.start()
print("main thread", current_thread().getName())
current_thread().setName('thread ka doosra name') 


#create a thread by creating a child class to thread class
#class ChildclassName(Thread)
#statements
#threadobj = chilsclass name    
class MYthread(Thread):
    pass
t = MYthread()

from threading import Thread
class mythread(Thread):
    pass
t = mythread()
print(t.name)

#thread class method
#run() , join(), start()

#create a thread without creating child class to thread claass
#class classnamee:
#    statment
class threadname:
    def disp(self,a,b):print(a,b)
myt = threadname()
t = Thread(target=myt.disp,args = 10,29)

class classname:
    def disp(self,a,b):print(a,b)
myt = threadname()
t = thread(Targer  =myt.disp,atgs = 10,20)
 
 
 
 
from threading import Thread
class name:
 def disp(a,b):
     print(a,b)
obj = name()

t = Thread(target = obj.disp,args = (10, 30) )
t.start()

f = open("example.txt",'f')
print(f.read())
f.close()

with open("exampls.txt") as f:
    print(f.read())
