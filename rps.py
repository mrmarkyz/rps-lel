import random
import time
print('''
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ██████   ██████   ██████ ██   ██     ██████   █████  ██████  ███████ ██████      ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ██   ██ ██    ██ ██      ██  ██      ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██      ██ ██      ██      ██    ██ ██   ██    ███  
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ██████  ██    ██ ██      █████       ██████  ███████ ██████  █████   ██████      ███████ ██      ██ ███████ ███████ ██    ██ ██████    ███   
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██   ██ ██    ██ ██      ██  ██      ██      ██   ██ ██      ██      ██   ██          ██ ██      ██      ██      ██ ██    ██ ██   ██  ███    
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      ██   ██  ██████   ██████ ██   ██     ██      ██   ██ ██      ███████ ██   ██     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ 
                                                                                                                                                                                                                                     ''')





def win_cond(rps):
    print('\033[44m{}\033[00m' .format('i choose...'))
    time.sleep(0.9)
    print(rps)
    time.sleep(1)
    print('\033[42m{}\033[00m'.format('I WIN!!!'))
    time.sleep(2)
    print('nerd!')
    play()


def lose_cond(rps):
    print('\033[44m{}\033[00m' .format('i choose...'))
    time.sleep(0.9)
    print(rps)
    time.sleep(1)
    print('\033[41m{}\033[00m'.format('GAH!!! I LOSE!!!'))
    play()

def play():
    play = input('you wanna play!? yes or no / y or n: ')
    if (play == 'yes' or 'y'):
        game()
    elif (play == 'no' or play == 'n'):
        print('okay lol')
    else:
        print('what,,,')
        
        
def tie():
    print('\033[43m{}\033[00m' .format('tie,,'))
    play()


def game():
    rpsU = input('\033[104m{}\033[00m' .format('welcome to the game ong!! choose rock, paper, scissors, lizard, or spock! ')).lower()
    rps = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
        
    if (rpsU == 'rock' and (rps == 'paper' or rps == 'spock')):
        win_cond(rps)
    elif (rpsU == 'rock' and rps == 'rock'):
        tie()
    elif (rpsU == 'rock' and (rps == 'lizard' or rps == 'scissors')):
        lose_cond(rps)
    
    
    if (rpsU == 'spock' and (rps == 'lizard' or rps == 'paper')):
        win_cond(rps)
    elif (rpsU == 'spock' and rps == 'spock'):
        tie()
    elif (rpsU == 'spock' and (rps == 'scissors' or rps == 'rock')):
        lose_cond(rps)
    
    if (rpsU == 'scissors' and (rps == 'spock' or rps == 'rock')):
        win_cond(rps)
    elif (rpsU == 'scissors' and rps == 'scissors'):
        tie()
    elif (rpsU == 'scissors' and (rps == 'paper' or rps == 'lizard')):
        lose_cond(rps)
    
    if (rpsU == 'paper' and (rps == 'lizard' or rps == 'scissors')):
        win_cond(rps)
    elif (rpsU == 'paper' and rps == 'paper'):
        tie()
    elif(rpsU == 'paper' and (rps == 'spock' or rps == 'rock')):
        lose_cond(rps)

    if (rpsU == 'lizard' and (rps == 'rock' or rps == 'scissors')):
        win_cond(rps)
    elif (rpsU == 'lizard' and rps == 'lizard'):
        tie()
    elif (rpsU == 'lizard' and (rps == 'spock' or rps == 'paper')):
        lose_cond(rps)

    if (rpsU != 'rock' and rpsU != 'paper' and rpsU != 'scissors' and rpsU != 'lizard' and rpsU != 'spock'):
        print('what the freakazoids!?')
        
        
play()