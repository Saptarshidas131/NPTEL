#Euclid's alogorithm modified2
# finding gcd of two numbers using euclid's algorithm, while loop

def gcd(m,n):
    if m < n:   #Assume m >= n
        (m,n) = (n,m)

    while (m%n) != 0:
        diff = m-n
        #diff > n? Possible
        (m,n) = (max(n,diff),min(n,diff))

    return n

# input
print("Input value for m:")
m = int(input())
print("Input value for n:")
n = int(input())
# output
print (gcd(m,n))

