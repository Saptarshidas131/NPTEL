# code to implement selection sort

def SelectionSort(l):

	# Scan slices l[0:len(l)], l[1:len(l)], -
	for start in range(len(l)):
	
		# Find minimum value in slice ...
		# setting minimum to the starting of the list
		minpos = start
		# iterating through the list
		for i in range(start,len(l)):
			# if the item in the list is less than the minimum value, then assign the index to the minimum index
			if l[i] < l[minpos]:
				minpos = i
				
		# . . . and move it to start of slice
		(l[start],l[minpos]) = (l[minpos],l[start])

l = [2,3,18,21,4,1,7,33]
SelectionSort(l)
print(l)
