# list difference, list of all elements in A but not in B
def list_diff(A,B):
    (C,m,n) = ([],len(A),len(B)) # Merge A[0:m],B[0:n]
    (i,j) = (0,0) # current position in A,B

    while i+j < m+n: # i+j is number of elements merged so far
        if i == m: # Case 1: A is empty
            return(C)
        elif j == n: # Case 2: B is empty
            C = A[:]
        else: # Case 3: Head of A or B is smaller
            if A[i] != B[j]:
                C.append(A[i])
            i = i+1
           # j = j+1
    return(C)

A = [12,2,5,6,7,19]
B = [2,6,1,9]
print(list_diff(A,B))
