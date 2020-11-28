"""
	Author: AnOnYmOus001100
	Date: 28/11/2020
	Description: To list first n primes
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

# function to find n primes
def nprimes(n):
	# initialize count = 0, i = 1 and plist = []
	(count,i,plist) = (0,1,[])
	# iterate as long as count is less than n
	while(count < n):
		# if i is prime, then increment count by 1 and add i to plist
		if isprime(i):
			(count,plist) = (count+1,plist+[i])
		i = i + 1
	# return the prime list
	return(plist)

# input
n = int(input("Enter a range n to get first n primes:"))
print(nprimes(n))
