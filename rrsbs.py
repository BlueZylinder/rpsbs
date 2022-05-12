import random

# score setters
user_score = 0
comp_score = 0


# auto replay
auto_replay = True
while auto_replay == True:

    # user choice setter
    user_choice = ''

    # input and input protection
    while user_choice not in ('ROCK', 'PAPER', 'SCISSORS'):
        user_choice = input('Rock Paper Scissors?\n\n').upper()

    # option list
    options = ['ROCK', 'PAPER', 'SCISSORS']

    # spacer
    print('')

    # computer's choice generator
    comp_choice = random.choice(options)

    # tie
    if comp_choice == user_choice:
        print('Both players chose', user_choice)

    # computer chooses rock conditionals
    elif comp_choice == 'ROCK':
        if user_choice == 'PAPER':
            print('Computer chose', comp_choice + '. You win!')
            user_score = user_score + 1
        else:
            print('Computer chose', comp_choice + '. You lose!')
            comp_score = comp_score + 1

    # computer chooses paper conditionals
    elif comp_choice == 'PAPER':
        if user_choice == 'SCISSORS':
            print('Computer chose', comp_choice + '. You win!')
            user_score = user_score + 1
        else:
            print('Computer chose', comp_choice + '. You lose!')
            comp_score = comp_score + 1

    # computer chooses scissors conditionals
    elif comp_choice == 'SCISSORS':
        if user_choice == 'ROCK':
            print('Computer chose', comp_choice + '. You win!')
            user_score = user_score + 1
        else:
            print('Computer chose', comp_choice + '. You lose!')
            comp_score = comp_score + 1

    # scoreboard generator
    print('\nUSER:', user_choice + '\nCOMP:', comp_choice + '\n\nUser:', str(user_score) + '\nComp:', str(comp_score) + '\n')