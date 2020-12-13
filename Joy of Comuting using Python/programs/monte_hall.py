"""
Description: Monte hall problem, simulates the problem
of having three closed doors and a prize behind a door,
the objective is to choose a door, then another door will
 be opened which doesn't consists of the prize and a
 choice is given to swap if wished otherwise not, finally
 all the doors are revealed along with the prize behind a
 door. On correct choice of door with prize it's a win else lose.
 @author: Saptarshi Das
 """

#Note: It is found that in monte hall problem, the chances of
# win is higher when choosed to swap contrary when not swapped.

import random

doors = [0]*3 #all the doors now contains 0
goatdoor = [0]*2 #door with no prize
swap = 0 #no. of swap wins
no_swap = 0 #no. of no swap wins
x = random.randint(0,2) #xth door will randomly contain prize
doors[x] = "BMW"

#filling all doors with goat except xth door
for i in range(0,3):
    if (i==x):
        continue
    else:
        doors[i] = "Goat"
        goatdoor.append(i)

#choice and play      
choice = int(input("Choose a door: "))
door_open = random.choice(goatdoor) #open a door that has goat
while (door_open==choice):   #door_open shouldn't be equal to choice
    door_open = random.choice(goatdoor)
ch = input("Do you want to swap? y/n ") #prompt for swap
if (ch=='y'):
    if (doors[choice]=='Goat'):
        print ("You won.")
        swap = swap+1
    else:
        print ("You lost.")
else:
    if (doors[choice]=='Goat'):
        print ("You lost.")
    else:
        print ("You won.")
        no_swap = no_swap+1
print (swap)
print (no_swap)
