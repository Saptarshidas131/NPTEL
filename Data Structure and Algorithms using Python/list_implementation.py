# linked list or list implementation

class Node:
    
    # constructor to initialise value and address of next node
    def __init__(self,initval=None):
        self.value = initval
        self.next = None
    
    # to check if list is empty returns the value of list
    def isempty(self):
        if self.value == None:
            return(True)
        else:
            return(False)
    
    # to append a node, append recursive
    def append(self,v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            (self.next).append(v)
        return()
        
    # insert a value at the head of the list
    def insert(self,v):
        if self.isempty():
            self.value = v
            return()
        
        newnode = Node(v)
        
        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)
        
        return()

    # delete first value in list, delete iterative
    def delete(self,x):
         if self.isempty():
             return()
         
         if self.value == x: # value to delete is in first node
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return()
         
         temp = self # first x to delete
         while temp.next != None:
             if temp.next.value == x:
                 temp.next = temp.next.next
                 return
             else:
                 temp = temp.next
         return()

    # printing the list
    def __str__(self):
        selflist = []
        
        if self.value == None:
            return(str(selflist))
        
        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)
        
        return(str(selflist))
