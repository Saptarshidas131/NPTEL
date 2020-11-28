#Euclid's algorithm modified1
# finding gcd of two numbers using euclid's algorithm

def gcd(m,n):
    #Assume m >= n
    if m < n:
        (m,n) = (n,m)

    if (m%n) == 0:
        return (n)
    else:
        diff = m - n
        #diff > n? Possible
        return gcd(max(n,diff),min(n,diff))

# input
print("Input value for m:")
m = int(input())
print("Input value for n:")
n = int(input())
# output
print (gcd(m,n))
