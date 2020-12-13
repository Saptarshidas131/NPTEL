# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 06:33:37 2020

@author: SAPTARSHI DAS
"""

from PIL import Image
import random

#end is 100
end = 100

#opens the image of the board
def show_board():
    img = Image.open('sl.jpg')
    img.show()

#checks for ladder and returns points
def checkladder(points):
    #ladder start list
    ls = [2,4,9,33,52,80]
    #ladder end list
    le = [38,14,31,85,88,99]

    for s in range(len(ls)+1):
        for e in range(len(le)+1):
            
            if points==ls[s]:
                return le[s]
            else:
                return points
            
#checks for snakes and returns points
def checksnake(points):
    #snake start list
    ss = [51,56,62,92,98]
    #snake end list
    se = [11,15,57,53,8]

    for s in range(len(ss)+1):
        for e in range(len(se)+1):
            
            if points==ss[s]:
                return se[s]
            else:
                return points

#check for end of game
def reachedend(points):
    if points==end:
        return True
    else:
        return False
    
    
#play function
def play():
    #player1 name
    p1 = input("Enter Player1 name:")
    #player2 name
    p2 = input("Enter player2 name:")
    
    #initial player points
    pp1 = 0
    pp2 = 0
    
    #initialize turn
    turn = 0
    
    #turn based playig start
    while(1):
        if turn%2==0:
            #player1 turn
            print (p1," your turn")
            #choice to continue playing
            c = input("want to continue(y/n):")
            if c=='n':
                print (p1," scored ",pp1)
                print (p2," scored ",pp2)
                print ("Quitting now.")
                break
            
            #generate a random number from 1 to 6
            dice = random.randint(1,6)
            print ("Dice: ",dice)
            #add points
            pp1 += dice
            
            #check for ladder
            pp1 = checkladder(pp1)
            
            #check for snake
            pp1 = checksnake(pp1)
            
            #check if player goes beyond board
            if pp1>end:
                pp1 = end
            
            print (p1," score ",pp1)
            
            if reachedend(pp1):
                print (p1,'won')
                break
        else:
            #player2 turn
            print (p2," your turn")
            #choice to continue playing
            c = input("want to continue(y/n):")
            if c=='n':
                print (p1," scored ",pp1)
                print (p2," scored ",pp2)
                print ("Quitting now.")
                break
            
            #generate a random number from 1 to 6
            dice = random.randint(1,6)
            print ("Dice: ",dice)
            #add points
            pp2 += dice
            
            #check for ladder
            pp2 = checkladder(pp1)
            
            #check for snake
            pp2 = checksnake(pp1)
            
            #check if player goes beyond board
            if pp2>end:
                pp2 = end
            
            print (p2," score ",pp2)
            
            if reachedend(pp2):
                print (p2,'won')
                break
        
        #increment turn
        turn += 1

show_board()
play()
