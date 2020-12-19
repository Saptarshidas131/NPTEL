# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:43:05 2020

@author: saptarshi
"""


import random

movies = ['anand','drishyam','nayakan','anbe sivan','gol maal','vikram vedha','black friday','dangal','manichithrathazhu','taare zameen par']

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c = movie.count(letter)
    if c == 0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append(ref[i])
            else:
                    temp.append('*')
    qn_new = ''.join(str(x) for x in temp)
    return qn_new
    

def play():
    p1name = input('Player 1: Please enter your name: ')
    p2name = input('Player2 : Please enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn%2 == 0:
            # player1
            print (p1name, 'Your turn ')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print (qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if is_present(letter,picked_movie):
                    # unlock
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print (modified_qn)
                    d = input('Enter 1 to guess the movie or 2 to unlock another letter' )
                    if d == '1':
                        ans = input('Enter your answer: ')
                        if ans == picked_movie:
                            pp1 = pp1 + 1
                            print ('Correct')
                            not_said = False
                            print (p1name,' Your score: ',pp1)
                        else:
                            print ('Wrong answer, try again.')
                else :
                    print (letter, 'not found ')
            c = input('Print 1 to continue or 0 to quit ')
            if c == '0':
                print (p1name,' Your score: ',pp1)
                print (p2name,' Your score: ',pp2)
                print('Thanks for playing')
                willing = False
        else:
            # player 2
            print (p2name, 'Your turn ')
            picked_movie = random.choice(movies)
            qn = create_question(picked)
            print (qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if is_present(letter,picked_movie):
                    # unlock
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print (modified_qn)
                    d = input('Enter 1 to guess the movie or 2 to unlock another letter' )
                    if d == '1':
                        ans = input('Enter your answer: ')
                        if ans == picked_movie:
                            pp2 = pp2 + 1
                            print ('Correct')
                            not_said = False
                            print (p2name,' Your score: ',pp2)
                        else:
                            print ('Wrong answer, try again.')
                else :
                    print (letter, 'not found ')
            c = input('Print 1 to continue or 0 to quit ')
            if c == '0':
                print (p1name,' Your score: ',pp1)
                print (p2name,' Your score: ',pp2)
                print('Thanks for playing')
                willing = False
        turn = turn + 1

play()