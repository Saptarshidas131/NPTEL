# Original Euclid's algorithm recursive
# finding gcd of two numbers using euclid's algorithm

def gcd(m,n):
    if m < n: #Assume m >= n
        (m,n) = (n,m)

    if (m%n) == 0:
        return (n)
    else:
        return gcd((n,m%n)) # m%n < n, always

# input
print("Input value for m:")
m = int(input())
print("Input value for n:")
n = int(input())
# output
print (gcd(m,n))
