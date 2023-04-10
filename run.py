# Project 3: Python Project - Word Game

import os
import random
import time
import colorama
from colorama import Fore

# Initialize colorama
colorama.init(autoreset=True)

draw_line = '═'
draw_space = ' '


def random_word_function():
    """
    Chooses a random word from the list
    """
    words = ["grape",
             "orange",
             "mango",
             "kiwi",
             "lemon",
             "date",
             "banana",
             "apple",
             "avocado"]
    word = random.choice(words)

    return word


def welcome_screen():
    """
    Prints Initial Game Screen
    Gives option to continue the game
    """
    msg = (Fore.BLUE + 'Press ENTER to continue')

    wrong_option = True
    while wrong_option:
        os.system('clear')
        print('╒' + draw_line * 78 + '╕')
        print('                               _______  _______  ______  ')
        print("                     |\\     /|(  ___  )(  ____ )(  __  \\ ")
        print('                     | )   ( || (   ) || (    )|| (  \\  )')
        print('                     | | _ | || |   | || (____)|| |   ) |')
        print('                     | |( )| || |   | ||     __)| |   | |')
        print('                     | || || || |   | || (\\ (   | |   ) |')
        print('                     | () () || (___) || ) \\ \\__| (__/  )')
        print('                     (_______)(_______)|/   \\__/(______/ ')
        print('                                                         ')
        print('                      _______  _______  _______  _______ ')
        print('                     (  ____ \\(  ___  )(       )(  ____ \\ ')
        print('                     | (    \\/| (   ) || () () || (    \\/')
        print('                     | |      | (___) || || || || (__    ')
        print('                     | | ____ |  ___  || |(_)| ||  __)   ')
        print('                     | | \\_  )| (   ) || |   | || (      ')
        print('                     | (___) || )   ( || )   ( || (____/\\ ')
        print('                     (_______)|/     \\||/     \\|(_______/')
        print('')
        print('╞' + draw_line * 78 + '╡')
        print(f'                         ⇉ {msg} ⇇  ')
        welcome_input = input('prompt: ')

        # if user choice valid - break loop
        if welcome_input == '':
            wrong_option = False

        # if user choice invalid - different message - loop
        else:
            msg = (Fore.RED + 'Press ENTER')


def player_name_screen():
    """
    Get Player name to personalize the Game
    Prints screen
    accepts user input and returns player's name
    """
    greeting1 = 'Welcome to the Word Guessing Game'
    greeting2 = 'Good to see you here'
    name_request = 'PLEASE ENTER YOUR NAME'
    msg = (Fore.BLUE + 'Type your NAME')

    wrong_option = True
    while wrong_option:
        os.system('clear')
        print('╒' + draw_line * 78 + '╕')
        print('')
        print((Fore.YELLOW + draw_space * 23 + greeting1))
        print((Fore.YELLOW + draw_space * 28 + greeting2))
        print('')
        print('')
        print('')
        print(' Rules:')
        print('')
        print('  1. You have total 10 attempts to guess the word.')
        print('  2. Every false guess will be counted as one attempt.')
        print('')
        print('                                   Have fun!')
        print('')
        print('')
        print('')
        print((Fore.RED + draw_space * 28 + name_request))
        print('')
        print('')
        print('╞' + draw_line * 78 + '╡')
        print(f'                             ⇉ {msg} ⇇  ')
        player_name_input = input(' prompt: ').upper()

        # if user choice valid - break loop
        if player_name_input.isalpha():
            wrong_option = False

        # if user choice invalid - different message - loop
        else:
            msg = (Fore.RED + 'Type your NAME')

    return player_name_input


def options_screen(player_name):
    """
    Prints the option screen
    Gives the user options to play the game or exit
    Runs a loop to validate the user option input
    """

    # inital message
    msg = (Fore.BLUE + 'Type an option NUMBER')

    # user input loop
    wrong_option = True
    while wrong_option:
        os.system('clear')
        print('╒' + draw_line * 78 + '╕')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print(draw_space * 27 + f'{Fore.YELLOW}Hi {player_name},')
        print('')
        print(draw_space * 27 + 'Choose an Option:')
        print(draw_space * 29 + (Fore.BLUE + '1 Play Game'))
        print(draw_space * 29 + (Fore.BLUE + '2 Exit Game'))
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('╞' + draw_line * 78 + '╡')
        print(f'                           ⇉ {msg} ⇇  ')
        option_input = input('prompt: ')

        # if user choice valid - break loop
        if option_input in ('1', '2'):
            wrong_option = False

        # if user choice invalid - different message - loop
        else:
            msg = (Fore.RED + 'Choose only 1 or 2')

    # return valid user input
    return option_input


def game_scrn(player_name):
    """
    Main Game Code
    accepts and validates user input
    gets random word
    runs a while loop to determine if annd when the game is finished
    runs a for loop to hide/show the letters
    prints the game screen
    gives option to user to quit or play the game again.
    """

    random_word = random_word_function()

    # setup variables for game logic
    maximum_attempts = 10
    a_counter = 0
    user_input = ''
    display = ''
    guessed = []

    # inital message
    msg = (Fore.BLUE + 'Type only LETTERS a-z')

    # for hint
    word_length = len(random_word)

    while a_counter < maximum_attempts:
        display = ''
        for letter in random_word:
            if letter in guessed:
                display += ' ' + letter + ' '
            else:
                display += ' _ '

        os.system('clear')
        print('╒' + draw_line * 78 + '╕')
        print(f'  Name: {Fore.YELLOW}{player_name}')
        print('╘' + draw_line * 78 + '╛')
        print('')
        print(f' {Fore.BLUE} Maximum attempts: {maximum_attempts}')
        print(f' {Fore.BLUE}    Your attempts: {Fore.RED} {a_counter}')
        print('')
        print(f'  {Fore.RED}  Its a Fruit and has {word_length} letters')
        print('')
        print('')
        print('')
        print('')
        print(f'                                  {display}')
        print('')
        print('')
        print('')
        print('')
        print('')
        print((Fore.RED + ' Type "2" anytime to exit'))
        print('╞' + draw_line * 78 + '╡')
        print(f'                  ⇉ {msg} ⇇  ')
        user_input = input('prompt: ').lower()
        
        # if user input is in random word
        if user_input in random_word:
            # append to guessed list
            guessed.append(user_input)
            # if user guessed all letters
            if set(random_word) == set(guessed):
                return ['c', a_counter, maximum_attempts, random_word]
            # if word is not complete
            else:
                msg = (Fore.GREEN + 'Correct Guess, Please enter next letter!')
        # if wrong user input
        elif user_input == '2':
            return ['exit', a_counter, maximum_attempts, random_word]
        else:
            msg = (Fore.RED + 'Oops, wrong guess, please try again')
            a_counter += 1
    # attempt maximum reached
    if a_counter == maximum_attempts:
        return ['failed', a_counter, maximum_attempts, random_word]


def congrats_screen(player_name, attempt_counter, maximum_attempts):
    """
    Prints Congratulation Screen
    gives the user options to exit or play the game again
    """
    # draw Congratulation Screen
    # user input loop

    # inital message
    msg = (Fore.BLUE + 'Type an option NUMBER')

    wrong_option = True
    while wrong_option:
        os.system('clear')
        print('╒' + draw_line * 78 + '╕')
        print(f'  Name:{Fore.YELLOW} {player_name}')
        print('╘' + draw_line * 78 + '╛')
        print('')
        print(f' {Fore.BLUE} Maximum attempts: 10')
        print(f' {Fore.BLUE}    Your attempts:{Fore.RED} {attempt_counter}')
        print('')
        print('')
        print('')
        print(draw_space * 25 + f'{player_name},{Fore.YELLOW} CONGRATULATIONS')
        print(draw_space * 27 + 'You are a genius!')
        print('')
        print('')
        print('                           Choose an Option:')
        print((Fore.BLUE + '                             1 Play again'))
        print((Fore.BLUE + '                             2 Exit Game'))
        print('')
        print('')
        print('')
        print('╞' + draw_line * 78 + '╡')
        print(f'                          ⇉ {msg} ⇇  ')
        congrats_input = input('prompt: ')

        # if user choice valid - break loop
        if congrats_input in ('1', '2'):
            wrong_option = False

        # if user choice invalid - different message - loop
        else:
            msg = (Fore.BLUE + 'Choose only 1 or 2')
    return congrats_input


def failed_screen(player_name, attempt_counter, maximum_attempts, random_word):
    """
    Print Failed Screen
    gives the user options to exit game or to play again
    """
    # inital message
    msg = (Fore.BLUE + 'Type an option NUMBER')

    # user input loop
    wrong_option = True
    while wrong_option:
        os.system('clear')
        print('╒' + draw_line * 78 + '╕')
        print(f'  Name: {Fore.BLUE}{player_name}')
        print('╘' + draw_line * 78 + '╛')
        print('')
        print(f' {Fore.BLUE} Maximum attempts: {maximum_attempts}')
        print(f'  {Fore.BLUE}   Your attempts:{Fore.RED} {attempt_counter}')
        print('')
        print('')
        print('')
        print(draw_space * 20 +
              (Fore.RED + player_name +
               ', you tried but you FAILED this time.'))
        print('')
        print(draw_space * 20 +
              'The word was ' + (Fore.YELLOW +
                                 random_word.upper()))
        print('')
        print('                           Choose an Option:')
        print((Fore.BLUE + '                             1 Play again'))
        print((Fore.BLUE + '                             2 Exit Game'))
        print('')
        print('')
        print('')
        print('╞' + draw_line * 78 + '╡')
        print(f'                          ⇉ {msg} ⇇  ')
        failed_input = input('prompt: ')

        # if user choice valid - break loop
        if failed_input in ('1', '2'):
            wrong_option = False

        # if user choice invalid - different message - loop
        else:
            msg = (Fore.RED + 'Choose only 1 or 2')

    return failed_input


def goodbye_screen(player_name):
    """
    Print Game end splash screen
    allows user to enter any key to exit the game
    """
    os.system('clear')
    print('╒' + draw_line * 78 + '╕')
    print(f'{Fore.YELLOW} Name: {player_name}')
    print('╘' + draw_line * 78 + '╛')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('                   _____                 _ _  ')
    print('                  / ____|               | | | ')
    print('                 | |  __  ___   ___   __| | |__  _   _  ___ ')
    print("                 | | |_ |/ _ \\ / _ \\ / _` | '_ \\| | | |/ _ \\ ")
    print('                 | |__| | (_) | (_) | (_| | |_) | |_| |  __/ ')
    print(draw_space * 18 + '\\_____|\\___/ \\___/ \\__,_|_.__/ \\__, |\\___|')
    print('                                                  __/ | ')
    print('                                                 |___/ ')
    print('')
    print('')
    print('')
    print('╞' + draw_line * 78 + '╡')
    print((Fore.BLUE + draw_space * 25 + '⇉ Thank you for playing! ⇇'))
    time.sleep(3)
    os.system('clear')


def main():
    """
    Runs all program function to Start Game
    """
    # initial screen - game start
    welcome_screen()

    # get player's name
    player_name = player_name_screen()

    display = ''

    # display game menu
    option = options_screen(player_name)

    # while loop for user input
    do_not_exit = True
    while do_not_exit:
        # option screen - user selection "1"
        if option == '1':
            # call game screen
            game_input, attempt_counter, maximum_attempts, random_word = game_scrn(player_name)
            # if user wins
            if game_input == 'c':
                congrats_input = congrats_screen(player_name,
                                                 attempt_counter,
                                                 maximum_attempts)
                if congrats_input == '1':
                    do_not_exit = True
                    option = '1'
                elif congrats_input == '2':
                    do_not_exit = False
                    option = '2'
            if game_input == 'failed':
                congrats_input = failed_screen(player_name,
                                               attempt_counter,
                                               maximum_attempts,
                                               random_word)
                if congrats_input == '1':
                    do_not_exit = True
                    option = '1'
                elif congrats_input == '2':
                    do_not_exit = False
                    option = '2'
            if game_input == 'exit':
                goodbye_screen(player_name)
                return 'Thank you'
        if option == '2':
            break
    if option == '2':
        goodbye_screen(player_name)


main()
