def divides(m,n):
	if (n%m == 0):
		return(True)
	else:
		return(False)

def even(n):
	return(divides(2,n))
	
def odd(n):
	return(not divides(2,n))
	
m = int(input("Enter m: "))
n = int(input("Enter n: "))

print(str(m) + " divides " + str(n) + " is ",divides(m,n))
print(str(n) + " is even ",even(n))
print(str(n) + " is odd ",odd(n))
