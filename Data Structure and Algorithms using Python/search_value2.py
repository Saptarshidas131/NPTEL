# search a value in list, a more better approach
def findpos(l,v):
    (pos,i) = (-1,0)
    for x in l:
        if x == v:
            # Exit and report position of x
    # Loop over, report -1 if we did not find the value
            pos = i
            break
        i = i+1
    # If pos not reset in loop, pos is -1
    return(pos)

l = [5,20,9,8,43,72]
v = int(input("Enter a number to search: "))
print(findpos(l,v))
