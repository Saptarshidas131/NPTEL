# search a value in list, a more better approach improved
def findpos(l,v):
    pos = -1
    for i in range(len(l)):
        if l[i] == v:
            # Exit and report position of x
    # Loop over, report -1 if we did not find the value
            pos = i
            break
    # If pos not reset in loop, pos is -1
    return(pos)

l = [5,20,9,8,43,72]
v = int(input("Enter a number to search: "))
print(findpos(l,v))
