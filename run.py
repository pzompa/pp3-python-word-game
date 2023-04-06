# Project 3: Python Project - Word Game 

# for os.system clear: clears screen
import os

def random_word_function():
    """
    Generate a random Word
    """
    # Generate randomd Word
    # create a list of random words
    # choose a word form the list

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

def options_screen():
    """
    Options Menu
    """
    # Play or Exit

def game_screen():
    """
    Main Game Code
    """
    # Main Game Code
    # accept user input
    # check input validity

def congrats_screen():
    """
    Display Contratulation Screen
    """
    # draw Contratulation Screen

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

main()