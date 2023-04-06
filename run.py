# Project 3: Python Project - Word Game 

# for os.system clear: clears screen
import os

# for choosing random word from list
import random

def random_word_function():
    """
    Generate a random Word
    """
    # create a list of random words
    # choose a word form the list
    words = ["grape", "orange", "strawberry", "watermelon", "lime", "date", "banana", "apple", "avocado"]
    word = random.choice(words)

    # future implementation: use request library, to get random word from open API

    # return random word
    return word

def welcome_screen():
    """
    Initial Game Screen
    """
    # Initial Game Screen
    # draw initial screen
    # anykey to continue
    os.system('clear')
    print('╒══════════════════════════════════════════════════════════════════════════════╕')
    print('                               _______  _______  ______  ')
    print("                     |\     /|(  ___  )(  ____ )(  __  \ ")
    print('                     | )   ( || (   ) || (    )|| (  \  )')
    print('                     | | _ | || |   | || (____)|| |   ) |')
    print('                     | |( )| || |   | ||     __)| |   | |')
    print('                     | || || || |   | || (\ (   | |   ) |')
    print('                     | () () || (___) || ) \ \__| (__/  )')
    print('                     (_______)(_______)|/   \__/(______/ ')
    print('                                                         ')
    print('                      _______  _______  _______  _______ ')
    print('                     (  ____ \(  ___  )(       )(  ____ \ ')
    print('                     | (    \/| (   ) || () () || (    \/')
    print('                     | |      | (___) || || || || (__    ')
    print('                     | | ____ |  ___  || |(_)| ||  __)   ')
    print('                     | | \_  )| (   ) || |   | || (      ')
    print('                     | (___) || )   ( || )   ( || (____/\ ')
    print('                     (_______)|/     \||/     \|(_______/')
    print('                                                                                ')
    print('╞══════════════════════════════════════════════════════════════════════════════╡')
    print('                         ⇉ Press ENTER to continue ⇇  ')
    enter = input('prompt: ')


def player_name_screen():
    """
    Get Player Name, to personalize the Game
    """
    # clear screen
    # draw screen
    # wait for user input (player's name)
    # return value = player's name
    os.system('clear')
    print('╒══════════════════════════════════════════════════════════════════════════════╕')
    print('                               _______  _______  ______  ')
    print('                     |\     /|(  ___  )(  ____ )(  __  \ ')
    print('                     | )   ( || (   ) || (    )|| (  \  )')
    print('                     | | _ | || |   | || (____)|| |   ) |')
    print('                     | |( )| || |   | ||     __)| |   | |')
    print('                     | || || || |   | || (\ (   | |   ) |')
    print('                     | () () || (___) || ) \ \__| (__/  )')
    print('                     (_______)(_______)|/   \__/(______/ ')
    print('                                                         ')
    print('                      _______  _______  _______  _______ ')
    print('                     (  ____ \(  ___  )(       )(  ____ \ ')
    print('                     | (    \/| (   ) || () () || (    \/')
    print('                     | |      | (___) || || || || (__    ')
    print('                     | | ____ |  ___  || |(_)| ||  __)   ')
    print('                     | | \_  )| (   ) || |   | || (      ')
    print('                     | (___) || )   ( || )   ( || (____/\ ')
    print('                     (_______)|/     \||/     \|(_______/')
    print('                                                                                ')
    print('╞══════════════════════════════════════════════════════════════════════════════╡')
    print('                             ⇉ Type your NAME ⇇  ')
    player_name = input('prompt: ').upper()
    return player_name

def options_screen(player_name):
    """
    Options Menu
    """
    # Play or Exit

    # inital message
    msg = 'Type an option NUMBER'
    
    # user input loop
    wrong_option = True
    while wrong_option:
        os.system('clear')
        print('╒══════════════════════════════════════════════════════════════════════════════╕')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print(f'                           Hi {player_name},')
        print('')
        print('                           Choose an Option:')
        print('                             1 Play Game')
        print('                             2 Exit Game')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('╞══════════════════════════════════════════════════════════════════════════════╡')
        print(f'                           ⇉ {msg} ⇇  ')
        option_input = input('prompt: ')
        
        # if user choice valid - break loop
        if option_input in ('1', '2'):
            wrong_option = False
        
        # if user choice invalid - different message - loop
        else:
            msg = 'Choose only 1 or 2'
    
    # return valid user input
    return option_input

def game_screen(player_name):
    """
    Main Game Code
    """
    # Main Game Code
    # accept user input
    # check input validity

    # get random word
    random_word = random_word_function()

    # setup variables for game logic
    maximum_attempts = 10
    attempt_counter = 0
    user_input = ''
    display = ''
    guessed = []

    # inital message
    msg = 'Type only LETTERS a-z'

    # for hint
    word_length = len(random_word)

    while attempt_counter < maximum_attempts:
        display = ''
        for letter in random_word:
            if letter in guessed:
                display += ' ' +  letter + ' '
            else: 
                display += ' _ '   
        os.system('clear')
        print('╒══════════════════════════════════════════════════════════════════════════════╕')
        print(f'  Name: {player_name}')
        print('╘══════════════════════════════════════════════════════════════════════════════╛')
        print('')
        print(f'  Maximum attempts: {maximum_attempts}')
        print(f'     Your attempts:  {attempt_counter}')
        print('')
        print(f'    Its a Fruit and has {word_length} letters')
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
        print('')
        print('╞══════════════════════════════════════════════════════════════════════════════╡')
        print(f'                  ⇉ {msg} ⇇  ')
        user_input = input('prompt: ').lower()

        # if user input is in random word
        if user_input in random_word:
            # append to guessed list
            guessed.append(user_input)
            # if user guessed all letters
            if set(random_word) == set(guessed):
                return ['congratulations',attempt_counter, maximum_attempts, random_word]
            # if word is not complete
            else:
                msg = 'Correct Guess, Please enter next letter!'
        # if wrong user input
        else:
            msg = 'Oops, that was not in the word, please try again'
            attempt_counter += 1
    # attempt maximum reached
    if attempt_counter == maximum_attempts:
        return ['failed',attempt_counter, maximum_attempts, random_word]
        

def congrats_screen(player_name, attempt_counter, maximum_attempts):
    """
    Display Congratulation Screen
    """
    # draw Congratulation Screen
    os.system('clear')
    print('╒══════════════════════════════════════════════════════════════════════════════╕')
    print(f'  Name: {player_name}')
    print('╘══════════════════════════════════════════════════════════════════════════════╛')
    print('')
    print('  Maximum attempts: 10')
    print(f'     Your attempts: {attempt_counter}')
    print('')
    print('')
    print('')
    print(f'                          {player_name}, CONGRATULATIONS.')
    print('                             You are a genius!')
    print('')
    print('')
    print('                           Choose an Option:')
    print('                             1 Play again')
    print('                             2 Exit Game')
    print('')
    print('')
    print('')
    print('╞══════════════════════════════════════════════════════════════════════════════╡')
    print('                          ⇉ Type an option NUMBER ⇇  ')
    congrats_input = input('prompt: ')
    return congrats_input


def failed_screen():
    """
    Display Failed Screen
    """
    # Player loses
    # draw failed screen

def goodbye_screen():
    """
    Game end splash screen
    """
    # draw goodbye screen

def main():
    """
    Start Game
    """
    # program main control flow
    # call welcome screen
    # call player name screen
    # call option screen
    # call game screen
    # call congrats screen
    # call failed screen
    # call goodbye screen

    # initial screen - game start
    welcome_screen()

    # get player's name
    player_name = player_name_screen()

    # display game menu
    option = options_screen(player_name)

    # display game screen
    game_screen(player_name)

    do_not_exit = True
    while do_not_exit:
        # option screen - user selection "1"
        if option == '1':
            # call game screen
            game_input, attempt_counter, maximum_attempts, random_word = game_screen(player_name)
            # if user wins
            if game_input == 'congratulations':
                congrats_input = congrats_screen(player_name, attempt_counter, maximum_attempts)
                if congrats_input == '1':
                    do_not_exit = True
                    option = '1'
                elif congrats_input == '2':
                    do_not_exit = False
                    option = '2'
        if option == '2':
            break
    if option == '2':
        goodbye_screen(player_name)
    return '\nThank you for playing this game\n\n'

main()