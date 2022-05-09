"""
game.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Jakub Kyselý
email: jkysely@centrum.cz
discord: Kysy#6104
"""
import random
import time

SEPARATOR = '-' * 47

def introduction():
    '''
    Print greeting and introduction
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
    #print(secret_num)
    return secret_num

def tip():
    '''
    Inserts a player's tip and control them
    '''
    control = True
    while control:
        tip = input('Enter a number: ')
        print(SEPARATOR)
        if tip.startswith('0'):
            print(f">>> {tip}")
            print('Invalid input, try again!!! \n'
                  'Please insert 4 unique numbers')
            print(SEPARATOR)

        elif len(tip) == 4 and tip.isnumeric():
            if len(set(tip)) == 4:
                print(f">>> {tip}")
                return tip
            else:
                print(f">>> {tip}")
                print('Invalid input, try again!!! \n'
                      'Please insert 4 unique numbers')
                print(SEPARATOR)
        else:
            print(f">>> {tip}")
            print('Invalid input, try again!!! \n'
                  'Please insert 4 unique numbers')
            print(SEPARATOR)

def game():
    '''
    Start game, control player turns and print the final score.
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

            bulls_result = bull_count(bulls)
            cows_result = cow_count(cows)

            print(f"{bulls_result}, {cows_result}")
            print(SEPARATOR)

            attemp += 1
    count(attemp)

def bull_count (bulls):
    '''
    Decide if use bull or bulls
    '''
    if bulls == 0:
        return f"{bulls} bulls"
    elif bulls == 1:
        return f"{bulls} bull"
    else:
        return f"{bulls} bulls"

def cow_count (cows):
    '''
    Decide if use cow or cows
    '''
    if cows == 0:
        return f"{cows} cows"
    elif cows == 1:
        return f"{cows} cow"
    else:
        return f"{cows} cows"

def count(count_attemp: int):
    '''
    Print players score
    '''
    if count_attemp == 1:
        return print(f"You are seer!!! You used just {count_attemp} tip")
    elif count_attemp > 1 and count_attemp <= 5:
        return print(f"You are amazing!!! You used {count_attemp} tip")
    elif count_attemp > 5 and count_attemp <= 10:
        return print(f"You are good!!! You used {count_attemp} tip")
    elif count_attemp > 10 and count_attemp <= 15:
        return print(f"Not good but not bad!!! You used {count_attemp} tip")
    elif count_attemp > 15 and count_attemp <= 20:
        return print(f"That is really bad!!! You used {count_attemp} tip")
    else:
        return print(f"Shame on you!!! You used {count_attemp} tip")

def play():
    '''
    Play the game Bulls&Cows
    '''
    start_time = time.time()
    game()
    execution_time = (time.time() - start_time)
    print(F'Your game time is {round(execution_time)} sec.')

play()