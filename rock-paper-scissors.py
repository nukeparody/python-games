import random

def game():
    moves = ['rock', 'paper', 'scissors']
    user = input('rock paper scissors? ')

    cpu = random.choice(moves)

    if user == cpu:
        print('\nthe computer chose', cpu, end = ', you tied!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    if user == 'rock' and cpu == 'paper':
        print('\nthe computer chose', cpu, end = ', you lose!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    if user == 'paper' and cpu == 'scissors':
        print('\nthe computer chose', cpu, end = ', you lose!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    if user == 'scissors' and cpu == 'rock':
        print('\nthe computer chose', cpu, end = ', you lose!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    if user == 'rock' and cpu == 'scissors':
        print('\nthe computer chose', cpu, end = ', you win!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    if user == 'paper' and cpu == 'rock':
        print('\nthe computer chose', cpu, end = ', you win!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    if user == 'scissors' and cpu == 'paper':
        print('\nthe computer chose', cpu, end = ', you win!')

        while True:
            again = input('\ndo you want to play again? ')

            if again == 'no':
                print('okay, play again later!')
                exit()

            elif again == 'yes':
                print()
                game()

            else:
                print('\nplease enter either yes or no!')

    else:
        print('\nplease enter either rock, paper or scissors!')
        game()

print('welcome to rock paper scissors!')
name = input('what is your name? ')

print()

while True:
    print('hello ', name, end = ', ')
    ready = input('are you ready to play? ')

    if ready == 'no':
        print('\nokay, play again later!')
        exit()

    elif ready == 'yes':
        print()
        game()

    else:
        print('\nplease enter either yes or no!')
