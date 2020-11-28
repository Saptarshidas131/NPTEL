# Original Euclid's algorithm using while loop
# finding gcd of two numbers using euclid's algorithm

def gcd(m,n):
    if m < n: #Assume m >= n
        (m,n) = (n,m)

    while (m%n) != 0:
        (m,n) = (n,m%n) # m%n < n, always
    return(n)

# input
print("Input value for m:")
m = int(input())
print("Input value for n:")
n = int(input())
# output
print (gcd(m,n))
