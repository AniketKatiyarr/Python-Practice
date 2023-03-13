#from threading import Thread   
#def des():
#    for i in range(5):
#        print(":chile mile")
#t = Thread(target =des )
#t.start()
#for i in range(5):
#    print("main thread")
#    
from threading import Thread , current_thread

def disp():
    print("child",current_thread())
t = Thread(target = disp) 
t.start()

print("main thread, ", current_thread())    