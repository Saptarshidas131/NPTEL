# find gcd of two numbers
# somewhat better algorithm than the first 2 algorithms

# function to find the gcd of two numbers, this does not uses list, instead stores the maximum recent common factor of the two numbers
def gcd(m,n):
    # iterate from 1 to minimum of (m and n) + 1
    for i in range(1,min(m,n)+1):
        # if m and n is divisible i then assign i to mrcf
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i
    # return the maximum common factor found
    return mrcf

# input two numbers
m = int(input())
n = int(input())
# output gcd
print (gcd(m,n))
