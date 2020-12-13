"""
Description: Sorts the elements in a list in acending order, by comparing two adjacent elements.
@author: Saptarshi Das
"""

#bubblesort function
def bubbleSort(List):
    l = len(List)          #length of list a

    #swap two elements if the next element is smaller than current element
    for i in range(l):
        for j in range(0,l-i-1):
            if(List[j]>List[j+1]):
                tmp = List[j]
                List[j] = List[j+1]
                List[j+1] = tmp

#list a
a = [3,1,5,7,9,0,2,4,8]
bubbleSort(a)           #function calling by passing a
#print the sorted list
for e in a:
    print (e)
