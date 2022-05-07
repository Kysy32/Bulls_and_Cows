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

def secret_number():
    '''
    Generate secret number for game
    '''
    secret = "".join((str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))))
    print(secret)
    return secret

def tip():
    '''
    Inserts a player's tip
    '''
    tip = input('Enter a number: ')
    if len(tip) == 4 and tip.isnumeric():
        print(f">>> {tip}")
    else:
        print(f">>> {tip}")
        print('Invalid input, try again!!!')
    return(tip)

def game():
    introduction()
    secret = secret_number()
    game = True
    count_attemp = 0
    while game:
        attemp = tip()
        if attemp == secret:
            print('You got it')
            count_attemp += 1
            break
        else:
            pass

        count_attemp += 1
    print(count_attemp)


    print('Super you find the secret number :)')

def play():
    '''
    Play the game Bulls&Cows
    '''
    game()
    #return result

play()