# merge two lists
def merge(A,B): # Merge A[0:m],B[0:n]
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0) # Current positions in A,B

    while i+j < m+n: # i+j is number of elements merged so far
        if i == m: # Case 1: A is empty
            C.append(B[j])
            j = j+1
        elif j == n: # Case 2: B is empty
            C.append(A[i])
            i = i+1
        elif A[i] <= B[j]: # Case 3: Head of A is smaller
            C.append(A[i])
            i = i+1
        elif A[i] > B[j]: # Case 4: Head of B is smaller
            C.append(B[j])
            j = j+1
    return(C)

# merge sort
def mergesort(A,left,right):
    # Sort the slice A[left:right]

    if right - left <= 1: # Base case
        return(A[left:right])

    if right - left > 1: # Recursive call

        mid = (left+right)//2

        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return(merge(L,R))

A = [90,34,25,13,5,9,44]
left = 0
right = 7
print(mergesort(A,left,right))

