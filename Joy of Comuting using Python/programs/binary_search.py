"""
Description: Binary search, using recursion.
Search for an element within a sorted list by dividing
 into half and then checking the
first and the second half using conditional statement
making it faster and better than linear search.

@author: Saptarshi Das
"""

def binarySearch(l,x,start,end):
    # base case: 1 element
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        #divide the array into halves
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            #left half
            return binarySearch(l,x,start,mid-1)
        else:
            #right half
            return binarySearch(l,x,mid+1,end)

l = [20,45,60,90,110,145,230]
x = int(input("Enter number to search: "))
index = binarySearch(l,x,0,len(l)-1)
if index==-1:
    print (x," not found")
else:
    print (x," is found at position ",index+1)
