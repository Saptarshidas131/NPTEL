# find the gcd of two numbers
# a naive gcd algorithm

# function to find the gcd of two numbers
def gcd(m,n):
    # fm is list of factors of m
    fm = []
    # iterating from 1 to m+1
    for i in range(1,m+1):
        # if remainder of m and i is 0 add i to fm, i.e, m is divisible by i
        if (m%i) == 0:
            fm.append(i)

    # fn is list of factors of n
    fn = []
    # iterating from 1 to n+1
    for j in range(1,n+1):
        # if remainder of n and j is 0 add j to fn, i.e, n is divisible by j
        if (n%j) == 0:
            fn.append(j)

    # common factors of m and n
    cf = []
    # if factor of m is also a factor of n then add f to cf
    for f in fm:
        if f in fn:
            cf.append(f)
    # return the last element of common factors, the highest number in cf, the highes factor
    return(cf[-1])

# input m and n
m = int(input())
n = int(input())
# passing m and n as arguments to gcd
gcd = gcd(m,n)
# output
print (gcd)
