# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:14:30 2020

@author: saptarshi
"""

import string
import random

symbols = []
symbols = list(string.ascii_letters+string.digits)
card1 = [0]*5
card2 = [0]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
#print (pos1)
#print (pos2)
# pos1 and pos2 are same symbol  postions in card1 and card2
samesymbol = random.choice(symbols)
symbols.remove(samesymbol)
if pos1 == pos2:
    card2[pos1] = samesymbol
    card1[pos1] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
i = 0
while i<5:
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i = i + 1
print (card1)
print (card2)
ch = input("Spot the similar symbol: ")
if ch == samesymbol:
    print ("Right")
else:
    print ("Wrong")