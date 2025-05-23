"""
This module is where the score and violation keeping functions are defined.
"""
score = 0.0
games = 0.0    #These are meant to be in MainKeeper.py but I need them here to prevent unnecessary errors
sets = 0.0

player1 = 'Zak'      #Same for these variables, they will be a user input in the main code
player2 = 'Rocco'

import random


def coinFlip():
    coin = random.randint(1,2)           
    if coin == 1:
        return 'Heads'
    else:
        return 'Tails'


def codeViolation(player, violation, side):
    str(violation) #Player is going to have to be a variable created in MainKeeper to keep track of how many violations.
    str(side)
    if player == 0:                           #e.g. p1violations or p2violations
        player + 1
        if side == 'right':
            print("Code violation ", violation, ", warning, ", player1)
        if side == 'left':
            print("Code violation ", violation, ", warning, ", player2)
    elif player == 1:
        player + 1
        if side == 'right':
            print("Code violation ", violation, ", point penalty, ", player1)
        if side == 'left':
            print("Code violation ", violation, ", point penalty, ", player2)
        if side == 'left':
            if score == 0.0:
                score = 0.15
            if score == 15.0:
                score = 15.15
            if score == 0.15:
                score = 0.30
            if score == 15.15:
                score = 15.30
            if score == 30.15:
                score = 30.30
            if score == 15.30:
                score = 15.40
            if score == 30.30:
                score = 30.40
            if score == 40.30:
                score = 40.40
            if score == 30.40:
                score = 0.0
                games + 0.1
                if games == 0.6 or 1.6 or 2.6 or 3.6 or 4.6 or 5.7 or 6.7:
                    sets + 0.1
                    if sets == 1.2:
                        print('Game, Set, Match ', player2)
                        quit()
                    print("Game and set, ", player2)
                if games == 6.6:
                    print('Tiebreakers not supported, please play a normal game')
            if score == 40.40:
                score = 40.41
            if score == 41.40:
                score = 40.40
            if score == 40.41:
                score = 0.0
                games + 0.1
                if games == 0.6 or 1.6 or 2.6 or 3.6 or 4.6 or 5.7 or 6.7:
                    sets + 0.1
                    if sets == 1.2:
                        print('Game, Set, Match ', player2)
                        quit()
                    print("Game and set ", player2)
                if games == 6.6:
                    print('Tiebreakers not supported, please play a normal game')
        elif side == 'right':
            if score == 0.0:
                score = 15.0
            if score == 15.0:
                score = 30.0
            if score == 0.15:
                score = 15.15
            if score == 15.15:
                score = 30.15
            if score == 30.15:
                score = 40.15
            if score == 15.30:
                score = 30.30
            if score == 30.30:
                score = 40.30
            if score == 40.30:
                score = 0.0
                games + 1.0
                if games == 6.0 or 6.1 or 6.2 or 6.3 or 6.4 or 7.5 or 7.6:
                    sets + 1.0
                    if sets == 2.1:
                        print('Game, Set, Match ', player1)
                        quit()
                    print('Game and set ', player1)
                if games == 6.6:
                    print('Tiebreakers not supported, please play a normal game')
            if score == 30.40:
                score = 40.40
            if score == 40.40:
                score = 41.40
            if score == 41.40:
                score = 0.0
                games + 1.0
                if games == 6.0 or 6.1 or 6.2 or 6.3 or 6.4 or 7.5 or 7.6:
                    sets + 1.0
                    if sets == 2.1:
                        print('Game, Set, Match ', player1)
                        quit()
                    print('Game and set ', player1)
                if games == 6.6:
                    print('Tiebreakers not supported, please play a normal game')
            if score == 40.41:
                score = 40.40
        else:
            print("Please check your inputs, side must be either 'left' or 'right'.")
    elif player == 2:
        player + 1
        if side == 'right':
            print("Code violation ", violation, ", game penalty, ", player1)
        if side == 'left':
            print("Code violation ", violation, ", game penalty, ", player2)
        if side == 'left':
            if games == 0.0:
                games = 0.1
            if games == 1.0:
                games = 1.1
            if games == 0.1:
                games = 0.2
            if games == 1.1:
                games = 1.2
            if games == 2.1:
                games = 2.2
            if games == 1.2:
                games = 1.3
            if games == 2.2:
                games = 2.3
            if games == 3.2:
                games = 3.3
            if games == 2.3:
                games = 2.4
            if games == 3.3:
                games = 3.4
            if games == 4.3:
                games = 4.4
            if games == 3.4:
                games = 3.5
            if games == 4.4:
                games = 4.5
            if games == 5.4:
                games = 5.5
            if games == 4.5:
                games = 0
                sets + 0.1
                if sets == 1.2:
                    print('Game, Set, Match ', player2)
                    quit()
                print("Game and set, ", player2)
            if games == 5.5:
                games = 5.6
            if games == 6.5:
                games = 6.6
                print('Tiebreakers not supported, please play a normal game')
            if games == 5.6:
                games = 0
                sets + 0.1
                if sets == 1.2:
                    print('Game, Set, Match ', player2)
                    quit()
                print("Game and set, ", player2)
            if games == 6.6:
                games = 0
                sets + 0.1
                if sets == 1.2:
                    print('Game, Set, Match ', player2)
                    quit()
                print("Game and set, ", player2)
        elif side == 'right':
            if games == 0.0:
                games = 1.0
            if games == 1.0:
                games = 2.0
            if games == 0.1:
                games = 1.1
            if games == 1.1:
                games = 2.1
            if games == 2.1:
                games = 3.1
            if games == 1.2:
                games = 2.2
            if games == 2.2:
                games = 3.2
            if games == 3.2:
                games = 4.2
            if games == 2.3:
                games = 3.3
            if games == 3.3:
                games = 4.3
            if games == 4.3:
                games = 5.3
            if games == 3.4:
                games = 4.4
            if games == 4.4:
                games = 5.4
            if games == 5.4:
                games = 0
                sets + 1.0
                if sets == 2.1:
                    print('Game, Set, Match ', player1)
                    quit()
                print("Game and set, ", player1)
            if games == 4.5:
                games = 5.5
            if games == 5.5:
                games = 6.5
            if games == 6.5:
                games = 0
                sets + 1.0
                if sets == 2.1:
                    print('Game, Set, Match ', player1)
                    quit()
                print("Game and set, ", player1)
            if games == 5.6:
                games = 6.6
                print('Tiebreakers not supported, please play a normal game')
            if games == 6.6:
                games = 0
                sets + 1.0
                if sets == 2.1:
                    print('Game, Set, Match ', player1)
                    quit()
                print("Game and set, ", player1)
    elif player == 3:
        if side == 'right':
            print("Code violation ", violation, ", ", player1)
            print('Game, Set, and Match ', player2)
            quit()
        if side == 'left':
            print("Code violation ", violation, ", ", player2)
            print('Game, Set, and Match ', player1)
            quit()
def addPoint(side):
    if side == 'right':
        if score == 0.0:
            score = 0.15
        if score == 15.0:
            score = 15.15
        if score == 0.15:
            score = 0.30
        if score == 15.15:
            score = 15.30
        if score == 30.15:
            score = 30.30
        if score == 15.30:
            score = 15.40
        if score == 30.30:
            score = 30.40
        if score == 40.30:
            score = 40.40
        if score == 30.40:
            score = 0.0
            games + 0.1
            if games == 0.6 or 1.6 or 2.6 or 3.6 or 4.6 or 5.7 or 6.7:
                sets + 0.1
                if sets == 1.2:
                    print('Game, Set, Match ', player2)
                    quit()
                print("Game and set, ", player2)
            if games == 6.6:
                print('Tiebreakers not supported, please play a normal game')
        if score == 40.40:
            score = 40.41
        if score == 41.40:
            score = 40.40
        if score == 40.41:
            score = 0.0
            games + 0.1
            if games == 0.6 or 1.6 or 2.6 or 3.6 or 4.6 or 5.7 or 6.7:
                sets + 0.1
                if sets == 1.2:
                    print('Game, Set, Match ', player2)
                    quit()
                print("Game and set ", player2)
            if games == 6.6:
                print('Tiebreakers not supported, please play a normal game')
    if side == 'left':
        if score == 0.0:
            score = 15.0
        if score == 15.0:
            score = 30.0
        if score == 0.15:
            score = 15.15
        if score == 15.15:
            score = 30.15
        if score == 30.15:
            score = 40.15
        if score == 15.30:
            score = 30.30
        if score == 30.30:
            score = 40.30
        if score == 40.30:
            score = 0.0
            games + 1.0
            if games == 6.0 or 6.1 or 6.2 or 6.3 or 6.4 or 7.5 or 7.6:
                sets + 1.0
                if sets == 2.1:
                    print('Game, Set, Match ', player1)
                    quit()
                print('Game and set ', player1)
            if games == 6.6:
                print('Tiebreakers not supported, please play a normal game')
        if score == 30.40:
            score = 40.40
        if score == 40.40:
            score = 41.40
        if score == 41.40:
            score = 0.0
            games + 1.0
            if games == 6.0 or 6.1 or 6.2 or 6.3 or 6.4 or 7.5 or 7.6:
                sets + 1.0
                if sets == 2.1:
                    print('Game, Set, Match ', player1)
                    quit()
                print('Game and set ', player1)
            if games == 6.6:
                print('Tiebreakers not supported, please play a normal game')
        if score == 40.41:
            score = 40.40
    print('Sets: ', sets)
    print('Games: ', games)
    print('Score: ', score)








"""
This is a template for the copying and pasting of the score and game possibilities.
Surely there is a better way to do this, but I've yet to figure it out.

if score == 0.0:
    score = 
if score == 15.0:
    score = 
if score == 0.15:
    score = 
if score == 15.15:
    score = 
if score == 30.15:
    score = 
if score == 15.30:
    score = 
if score == 30.30:
    score = 
if score == 40.30:
    score = 
if score == 30.40:
    score =
if score == 40.40:
    score = 
if score == 41.40:
    score = 
if score == 40.41:
    score =



if games == 2.3:
    games = 
if games == 3.3:
    games = 
if games == 4.3:
    games = 
if games == 3.4:
    games =
if games == 4.4:
    games = 
if games == 5.4:
    games =
if games == 4.5:
    games = 
if games == 5.5:
    games = 
if games == 6.5:
    games =
if games == 5.6:
    games = 
if games == 6.6:
    games = 
"""