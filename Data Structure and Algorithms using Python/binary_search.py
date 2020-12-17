# binary search for sorted list
def bsearch(seq,v,l,r):
    # search for v in seq[l:r], seq is sorted

    if (r - l == 0):
        return(False)

    mid = (l + r) // 2 # integer division

    if (v == seq[mid]):
        return (True)

    if (v < seq[mid]):
        return (bsearch(seq,v,l,mid))
    else:
        return (bsearch(seq,v,mid+1,r))

# assigning values
seq = [2,4,9,20,67,79]
v = int(input("Enter a value to search: "))
l = 0
r = 6
print(bsearch(seq,v,l,r))
