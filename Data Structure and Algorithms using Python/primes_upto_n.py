"""
	Author: AnOnYmOus001100
	Date: 28/11/2020
	Description: To list all the prime numbers upto n
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

# function to find primes upto n
def primesupto(n):
	# create a empty list
	primelist = []
	# iterate from 1 to n-1
	for i in range(1,n):
		# if i is prime then add to primelist
		if isprime(i):
			primelist = primelist + [i]
	# return primelist
	return(primelist)

# input
n = int(input("Enter a range n:"))
print(primesupto(n))
