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
    secret = [str(random.randint(1,9))]

    while len(secret) < 4:
        number = str(random.randint(0, 9))
        if number in secret:
            pass
        else:
            secret.append(number)
    secret_num = "".join(secret)
    print(secret_num)
    return secret_num

def tip():
    '''
    Inserts a player's tip and control them
    '''
    tip = input('Enter a number: ')
    print(SEPARATOR)
    if len(tip) == 4 and tip.isnumeric():
        print(f">>> {tip}")
    else:
        print(f">>> {tip}")
        print('Invalid input, try again!!!')
    return(tip)

def game():
    '''

    '''
    introduction()
    secret = secret_number()
    game = True
    attemp = 0
    while game:
        user_attemp = tip()
        if user_attemp == secret:
            print('You got it')
            attemp += 1
            break
        else:
            bulls = 0
            cows = 0
            for x, number in enumerate(user_attemp):
                if number in secret:
                    if number == secret[x]:
                        bulls += 1
                    else:
                        cows += 1

            print(f"{bulls} bulls, {cows} cows\n"
                  f"{SEPARATOR}")

            attemp += 1
    count(attemp)

def count(count_attemp: int):
    '''
    Print players score
    '''
    if count_attemp == 1:
        return print(f"You are seer!!! You used just {count_attemp} tip")
    elif count_attemp > 1 and count_attemp <= 4:
        return print(f"You are amazing!!! You used {count_attemp} tip")
    elif count_attemp > 4 and count_attemp <= 8:
        return print(f"You are good!!! You used {count_attemp} tip")
    elif count_attemp > 8 and count_attemp <= 12:
        return print(f"Not good but not bad!!! You used {count_attemp} tip")
    elif count_attemp > 12 and count_attemp <= 16:
        return print(f"That is really bad!!! You used {count_attemp} tip")
    else:
        return print(f"Shame on you!!! You used {count_attemp} tip")

def play():
    '''
    Play the game Bulls&Cows
    '''
    game()


play()