# PP3 Python Project -Word Guessing Game

# Table of Content
1. [Introduction](#introduction)
   1. [Site Goals](#site-goals)
   2. [For new visitors](#for-new-visitor)
   3. [For Returning visitors](#for-returning-visitors)
2. [Structure](#structure)
   1. [Features](#features)
   2. [Future features to be implemented](#future-features-to-be-implemented)
   3. [Screens](#screens)
      1. [Welcome Screen](#welcome-screen)
      2. [Player Name Screen](#player-name-screen)
      3. [Option Screen](#option-screen)
         1. [Option Screen - menu "1. Play Game"](#option-screen---menu-1-play-game)
         2. [Option Screen - menu "2. Exit Game"](#option-screen---menu-2-exit-game)
      4. [Game Screen](#game-screen)
         1. [Main Game Screen](#main-game-screen)
         2. [Correct guessed](#correct-guessed)
         3. [Incorrect guessed](#incorrect-guessed)
         4. [Failed screen](#failed-screen)
         5. [Success screen](#success-screen)
         6. [Goodbye screen](#goodbye-screen)
         7. [End screen](#end-screen)
3. [Flowcharts](#flowcharts)
   1. [Initial idea](#initial-idea)
   2. [Basic game flow ](#basic-game-flow)
   3. [Control flow of the main()](#control-flow-of-the-main)
   4. [Function call flow](#function-call-flow)
4. [Testing](#testing)
   1. [Functional Testing (Table)](#functional-testing)
5. [Code Validation](#code-validation)
   1. [PEP8](#pep8)
      1. [PEP8 pycodestyle - result](#pep8-pycodestyle---result)
      2. [Code Institute: CI Python Linter - result](#code-institute-ci-python-linter---result)
6. [Bugs](#bugs)
   1. [Fixed Bugs](#fixed-bugs)
   2. [Unfixed Bugs](#unfixed-bugs)
7. [Technologies used](#technologies-used)
   1. [Language](#language)
8. [Environment used](#environment-used)
9. [Deployment](#deployment)
   1. [Version Control](#version-control)
   2. [Heroku Deployment](#version-control)
   3. [Clone Locally](#clone-locally)
10. [Credits](#credits)

# Introduction
This project is a Python terminal game,  created for people to play the classic word guessing game.
- The deployed game can be found [here](https://pp3-python-word-game.herokuapp.com/).
- The repository can be found [here](https://github.com/pzompa/pp3-python-word-game).

## Site Goals
- To offer entertainment to the user who wants to get away from their daily activities and pass their time.
- Provide the user with simple instruction to play the game.
- Give options to play or exit the game.

## For new visitor
- To play the word guessing game and recharge their brain.
- To easily understand how to play the game.
- To easily quit whenever they wish to.

## For Returning visitors
- To practice their guessing skills.
- To play guessing game any number of times and improve their guessing skills further.

# Structure
<img src="asset/images/initial%20gameflow%20idea.png" height="500">

## Features
- A random word will be generated.
- The user is given a hint and the total number of letters in the word.
- The word is encrypted with a '-' for each letters.
- The computer accepts the user input and gives responsive feedback.
- If the user guessed the correct letter, the letter will be displayed.
- If the user guessed a wrong letter, the attempt counter will increase by one.
- If the user exhaust all the 10 attempts allowed, then the user loses the game and correct word will be revealed.
- If the user guessed a correct letter or guessed all the letters in the word, then the user wins the game.
- User is always given the option to quit the game at any point of the game.

## Future features to be implemented
- To store and update user specific data on google sheets.
- Return the top 10 highest scores.
- To generate random word from external dictionary.
- To give word specific hints to make the guessing game more interesting.

## Screens
### Welcome Screen
- This screen greets the user with a beautiful Ascii logo of the game. It gives the user option to press enter to play the game .
- The Ascii graffiti was generated using Patorjk.com.
		
![initial game screeen](/asset/images/initial_screen.png)

### Player Name Screen
- This screen displays the welcome message.
- asks the user to enter their name to personalise the game.
- informs the user with the rules of the game.


![](/asset/images/welcome_rules_name_screen.png)

### Option Screen
- This screen addresses the user by name.
- Gives the user options to play or the exit the game.

![](/asset/images/options_screen.png)
		
#### Option Screen - menu "1. Play Game"
	
- This screen shows the information about the maximum attempts allowed for the game and the number of attempts made by the user.
- This screen gives the user a hint of the random word.
- And prints blank spaces for each of the letters in the word
- After guessing a correct letter, the guessed letter replaces the blank space.
- If user guessed all the letters correctly, then he wins the game.
- If the user guesses a letter that isn't in the word, the "attempts counter" increases
- The user will be informed that the guessed letter is not in the word.
- If the user uses up 10 allowed attempts, and still not guessed all the letters in the word, then the user looses the game and the word is shown.

#### Option Screen - menu "2. Exit Game"
- This screen displays a beautiful goodbye screen with a message thanking the user for playing the game.
- This screen goes blank after 3 seconds and the game is over.

### Game Screen

#### Main Game Screen
![](/asset/images/game_screen.png)

#### Correct guessed
![](/asset/images/game_screen_right_guess.png)

#### Incorrect guessed
![](/asset/images/game_screen_wrong_guess.png)

#### Failed screen
![](/asset/images/failed_screen.png)

#### Success screen
![](/asset/images/congrats_screen.png)

#### Goodbye screen
![](/asset/images/goodbye_screen.png)

#### End screen
- application stops
- screen is cleared
![](/asset/images/end_game_black_screen.png)

# Flowcharts
- These flowchart were created using [Lucid Charts](https://lucid.app/documents#/dashboard).

## Initial idea 
- This was my initial plan for the game.
![](/asset/images/initial%20gameflow%20idea.png)

## Basic game flow 
![](/asset/images/Game%20Flow.png)

## Control flow of the main()
![](/asset/images/main%20function%20control%20flow.png)

## Function call flow 
![](/asset/images/Code%20Function%20flow.png)

 
# Testing
## Functional Testing
	
| Test | Action | Result | Notes |
| --- | --- | --- | --- | 
| https://pp3-python-word-game.herokuapp.com/ | Application can be reached via heroku URL | Application can be reached via heroku URL | Pass
| enter key | pressed the enter key | Enter key takes you to the name screen | Pass |
|  |  | Welcome message and rules are displayed as intented | Pass |
|  |  | Colorama is rendered properly | Pass |
|  |  | Prompt accepting user input  | Pass |
| player name | enter valid input | valid inputs are accepted | Pass |
|  | enter invalid input | invalid input is rejected | Pass |
| Option screen |  | Colorama is rendered properly | Pass |
|  |  | Player name is displayed properly | Pass |
| Option screen, option 1 | type 1 | Option 1 takes you properly to the game screen | Pass |
| Option screen, option 2 | type 2 | Option 2 takes you properly to the goodbye screen | Pass |
| Game screen |  | Colorama is rendered properly | Pass |
|  |  | Playername is displayed properly | Pass |
|  |  | Both Counters are displayed and functions properly | Pass |
|  |  | Option to quit game is displayed properly | Pass |
| Game screen, User Input | valid input - correct letter | Message is shown properly | Pass |
|  |  | Valid input is accepted as intented | Pass |
|  |  | letter is revealed to the user | Pass |
| Game screen, User Input | valid input - incorrect letter | Message is show properly | Pass |
|  |  | Attempt counter is incremented properly | Pass |
| Game screen, User Input  | Invalid Input | Invalid message is displayed and requests for valid entry , as intended. | Pass |
| Game screen, User Input | Option "2" Exit game | Goodbye screen is displayed as intended | Pass |
| Congratulation Screen |  | Appropriate message is displayed properly | Pass |
|  |  | Colorama is rendered properly | Pass |
|  |  | Playername is displayed properly | Pass |
|  |  | Both Counters are displayed and functions as intended | Pass |
|  |  | Options to play and quit game is displayed properly | Pass |
| Congratulation screen, User Input | Option 1 : Play again | Takes you to the Game screen to play the game | Pass |
| Congratulation screen, User Input | Option 2 : Exit game | Takes you to the Goodbye screen | Pass |
| Failed screen |  | Appropriate message is displayed properly | Pass |
|  |  | Colorama is rendered properly | Pass |
|  |  | Playername is displayed properly | Pass |
|  |  | Both Counters are displayed and functions as intended | Pass |
|  |  | Options to play and quit game is displayed properly | Pass |
|  |  | Attempt counter is incrementd properly | Pass |
| Failed screen, User Input | Option 1 : Play again | Takes you to the Game screen to play the game | Pass |
| Failed screen, User Input | Option 2 : Exit game | Takes you to the Goodbye screen | Pass |
| Goodbye screen |  | Screen is rendered properly | Pass |
|  |  | The screen is cleared after 3 seconds as intended | Pass |

# Code Validation
## PEP8
- pep8 error E501:
  - One cosmetic error: "run.py:396:80: E501 line too long (95 > 79 characters)" PEP8 issue still exists.
  - I decided against condensing the line for code readability reasons.

### PEP8 pycodestyle - result
![](/asset/images/PEP8-pycodestyle%20result.png)

### Code Institute: CI Python Linter - result
![](/asset/images/CI%20Python%20Linter.png)

# Bugs
## Fixed Bugs
- [PEP 8 pycodestlye](https://pycodestyle.pycqa.org/en/latest/intro.html) found issues  with the Ascii art especially with `\`. I fixed them by replacing them with `\\`.
- It also found white spaces in the code which was fixed.
- It also found issues with the length of some lines which was fixed by using (character * n) expression.


## Unfixed Bugs
- One cosmetic error: "run.py:396:80: E501 line too long (95 > 79 characters)" PEP8 issue still exists.
  - I decided against condensing the line for code readability reasons.

# Technologies used
## Language:
- [Python](https://www.python.org/): Python was the main language used  to build the whole application.
- Markdown: Markdown was used to write the README.md
- [colorama](https://pypi.org/project/colorama/) was used to colorize the text.

# Environment used
- [GitHub](https://github.com/pzompa/pp3-python-word-game): GitHub was used for source control
- [Gitpod](https://gitpod.io/workspaces): Project started with GitPod IDE to write the application
- [Codeanywhere](https://app.codeanywhere.com/): later migrated to Codeanywhere IDE, and finished and tested the application 
- [Heroku](https://pp3-python-word-game.herokuapp.com/): Heroku was used to deploy the project

# Deployment
## Version Control
The site was first created using Gitpod IDE, and later was migrate to Codeanywhere IDE and pushed to github to the remote repository "[pp3-python-word-game](https://github.com/pzompa/pp3-python-word-game)".
	
The following git commands were used throughout to push code to the remote repo:
	
- `Git add <file>` : This command was used to add the file to the staging area before they are committed.
- `Git commit-m "commit message"`: This command was used to commit changes to the local repository.
- `Git push`: This command was used to push all committed code to the remote repository on github.
		
## Heroku Deployment
These steps were followed to deploy this project to Heroku:
	
- Go to Heroku and click "New" to create a new app.
- Choose an app name and region, then click "Create app".
- Go to "Settings" and navigate to Config Vars. 
  - Add the following config variable: PORT : 8000
- Navigate to Buildpacks and add buildpacks for Python and NodeJS (in that order).
- Navigate to "Deploy". Set the deployment method to Github and enter repository name and connect.
- Scroll down to Manual Deploy, select "main" branch and click "Deploy Branch".
- The app will now be deployed to heroku.
		
## Clone Locally
- Open IDE of choice and type the following into the terminal:
- `git clone https://github.com/pzompa/pp3-python-word-game`		
- Project will now be cloned locally.

# Credits
- Lessons from the Code Institute and the love Sandwiches in learning and understanding python program.
- Watched many YouTube tutorials to learn and understand python programming and took some inspiration from these videos but was created from my own understanding.
   - (YouTube) [Build a Word Guessing Game in Python | Python Tutorials For Beginners](https://youtu.be/M1t4RJ5XRHE)
   - (YouTube) [Building a Guessing Game | Python | Tutorial 21](https://youtu.be/B9ORjeQlPOA)
- Used google extensively to understand and clear doubts throughout this project.
- [W3 Schools](https://www.w3schools.com/), [Educative.io](https://www.educative.io/) and [Stack overflow](https://stackoverflow.com/) was extensively used throughout this project.
- Ascii Art was made with [Patorjk Website](http://patorjk.com/software/taag/#p=about&f=Graffiti&t=Type%20Something%20).
- Code Institute Mentor Gareth McGiir: Grateful for his useful Tips and advices.
- My family for their support and patience