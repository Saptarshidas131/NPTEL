# find gcd of two numbers
# a better gcd alogrithm

# function to find gcd
def gcd(m,n):
    # common factors list
    cf = []
    # iterating from 1 to minimum of m and n
    for i in range(1,min(m,n)+1):
	# if i divides both m and n, then add to list of common factors
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    # return last element of common factors list, highest factor
    return(cf[-1])

# input two numbers
m = int(input())
n = int(input())
# output gcd of two numbers
print (gcd(m,n))
