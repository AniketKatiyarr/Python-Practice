from logging import exception


while(True):
    print("press Q to quit your game")
    a = input("Enter Your Number:")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
             print("you enteres greater than 6")
    except exception as e:
        print(e)

print("thanks for playing this game")   