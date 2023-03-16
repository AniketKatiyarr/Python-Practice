def Fibnocci(n):
	if n < 0:
		print("Incorrect input")

	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else:
		return Fibnocci(n-1) + Fibnocci(n-2)

print(Fibnocci(10))

def function(n):
    if n == 0 and n ==1:
        return 1
    else:
        return n* function(n-1)
print(function(10))
