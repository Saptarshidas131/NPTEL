"""
Description: Linear search, search a number by going through the list of elements one by one.
@author: Saptarshi Das
"""

def linearSearch(a,x):
    l = len(a)
    flag = 0
    count = 0

    for i in range(l):
        count += 1
        if (a[i]==x):
            print ("Element found at position: ",i+1)
            print ("Count = ",count)
            flag = 1

    if (flag == 0):
        print ("Element not found.")

List = [3,1,334,5,8,12,56,89,0,34]
linearSearch(List,5)
