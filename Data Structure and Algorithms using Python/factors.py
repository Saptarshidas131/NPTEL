"""
	Author: AnOnYmOus001100
	Date: 28/11/2020
	Description: To find all the factors of a number n
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
	
# input	
n = int(input("Enter a number to find its factors:"))
print(factors(n))
