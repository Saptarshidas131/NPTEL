# find the gcd of two numbers
# gcd calculating mininum of m and n from backwards using while loop

# function to find the gcd, this function is more optimised and instead of iterating from 1 to min(m,n) it starts from min(m,n) to 1 i.e, scan backwards
# this takes less time compared to first three algorithms
def gcd(m,n):

    #start from backwards min(m,n) to 1
    i = min(m,n)

    # iterate as long as i is greater than 0
    while i > 0:
        # if m and n is divisible by i, then return i, otherwise return i-1
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i = i - 1

# input two numbers
m = int(input())
n = int(input())
# output gcd of two numbers
print (gcd(m,n))
