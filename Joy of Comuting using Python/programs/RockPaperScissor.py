"""
Description: rock paper scissor game, between two
players with a secret bit position for secrecy.
@author: Saptarshi Das
"""

def rock_paper_scissor(num1,num2,bit1,bit2):
    p1 = int(num1[bit1])%3
    p2 = int(num2[bit2])%3
    if (player_one[p1]==player_two[p2]):
        print ("Draw")
    elif (player_one[p1]=="rock" and player_two[p2]=="scissor"):
        print ("Player 1 wins.")
    elif (player_one[p1]=="rock" and player_two[p2]=="paper"):
        print ("Player 2 wins.")
    elif (player_one[p1]=="paper" and player_two[p2]=="scissor"):
        print ("Player 2 wins.")
    elif (player_one[p1]=="paper" and player_two[p2]=="rock"):
        print ("Player 1 wins.")
    elif (player_one[p1]=="scissor" and player_two[p2]=="rock"):
        print ("Player 2 wins.")
    elif (player_one[p1]=="scissor" and player_two[p2]=="paper"):
        print ("Player 1 wins.")

player_one = {0:'rock',1:'paper',2:'scissor'}
player_two = {0:'paper',1:'rock',2:'scissor'}
while(1):
    num1 = input("Player 1, Enter choice: ")
    num2 = input("Player 2, Enter choice: ")
    bit1 = int(input("Player 1, Enter the secret bit position:"))
    bit2 = int(input("Player 2, Enter the secret bit position:"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch = input("Do you want to continue? y/n")
    if(ch=='n'):
        break
    
    
    
        
    
