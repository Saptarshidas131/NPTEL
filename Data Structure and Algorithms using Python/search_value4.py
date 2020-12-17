# search a value in list, a more better approach with else
def findpos(l,v):
    for i in range(len(l)):
        if l[i] == v:
            # Exit and report position of x
            pos = i
            break
    # else pos is -1
        else:
            pos = -1
    return(pos)

l = [5,20,9,8,43,72]
v = int(input("Enter a number to search: "))
print(findpos(l,v))
