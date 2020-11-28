"""
	Author: AnOnYmOus001100
	Date: 28/11/2020
	Description: To check if a number n is prime or not
"""

# find factors till n
def factors(n):
	# list of factors
	factorlist = []
	# iterating till n and if n is divisible by i, add it to factorlist
	for i in range(1,n+1):
		if n%i == 0:
			factorlist = factorlist + [i]
	# return the list
	return(factorlist)
	
# function to check if a number is prime or not
def isprime(n):
        # return True if factors are only 1 and n
                return(factors(n) == [1,n])

# input
n = int(input("Enter a number to check if it is prime:"))
print(isprime(n))
