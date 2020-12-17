def Quicksort(A,l,r): # sort A[l:r]
	if r - l <= 1: # Base case
		return ()
		
	# Partiion with respect to pivot, a[l]
	yellow = l+1
	
	for green in range(l+1,r):
		if A[green] <= A[l]:
			(A[yellow],A[green]) = (A[green],A[yellow])
			yellow = yellow + 1
			
	# Move pivot into place
	(A[l],A[yellow-1]) = (A[yellow-1],A[l])
	
	Quicksort(A,l,yellow-1) # Recursive calls
	Quicksort(A,yellow,r)

l = list(range(1000,0,-1))	
#l = [2,3,18,21,4,1,7,33]
Quicksort(l,0,len(l))
print(l)
