#write a pythonprogram to display a userr
# rentere name folowed by 
# good morning using input() function

name = (input("Enter your name\n"))
print ("good morning," + name )

print(input("enter your name"))
print("good morning,")  #wrong fromat

#2. write a program to fill in a letter template given below
#with name and date.

letter = '''Dear <|Name|>
You are selected !!
Date: <|Date|>
'''
name = input("Enter your name\n")
date = input("enter date")
letter = letter.replace("<|Name|>" , name)
letter = letter.replace("<|Date|>" , date)
print(letter)


 