from distutils.version import LooseVersion
import random
from telnetlib import WONT
 
def game(com,you):
    if com == you:
        return None
    elif com == 's':
        if you=='w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 'w':
            return False
        elif you == 's':
            return False
          
print("computer turn:snake(s) Wter(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'
       
you = input("yours's turn: snake(s) Wter(w) or Gun(g)?")
a = game(comp,you)

print(f"computer choose {comp}")
print(f"you choose{you}")
if a == None:
    print("THE game is tie")
elif a:
    print("you win...||")
else:
    print("you loose")
    
  