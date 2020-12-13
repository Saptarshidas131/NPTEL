#print the smaller number of the two
a,b = input().split()
"""
#easy way
if int(a)<int(b):
    print (int(a))
else:
    print (int(b))
"""
#another way
x = int(a) if int(a)<int(b) else int(b) #var = var1 if True else var2
print (x)
