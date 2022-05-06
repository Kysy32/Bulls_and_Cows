"""
game.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Jakub Kyselý
email: jkysely@centrum.cz
discord: Kysy#6104
"""
import random

SEPARATOR = '-' * 47

def introduction():
    '''
    Print greeting and game rules
    '''
    return print(f"Hi there\n"
            f"{SEPARATOR}\n"
            f"I've generated a random 4 digit number for you.\n"
            f"Let's play a bulls and cows game.\n"
            f"{SEPARATOR}")

#introduction()

def game():
    game = True
    secret = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]



def play():
    introduction()
    return result

game()