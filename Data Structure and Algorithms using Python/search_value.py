# search for a value in a list
def findpos(l,v):
	# return first position of v in l
	# return -1 if v not in l
	# set found to False and i to 0
	(found,i) = (False,0)
	while i < len(l):
                if l[i] == v:
			(found,pos) = (True,i)
	if not found:
		pos = -1
		
	return(pos)
	
l = [8,2,5,23,12,45,33]
v = int(input("Enter a value to search: "))
print(findpos(l,v))
