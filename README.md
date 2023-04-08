PP3 Python Word Game Project

# Introduction
This project is a Python terminal game,  created for people to play the classic word guessing game.
- The game can be found [here](https://pp3-python-word-game.herokuapp.com/).
- The repository can be found [here](https://github.com/pzompa/pp3-python-word-game).

## Site Goals
- To offer entertainment to the user who wants to get away from their daily activities and pass their time..
- Provide the user with simple instruction to play the game
- Give options to play or exit the game


## Target Audience
(to be done)

## For new users
- To play the word guessing game and charge their brain.
- To easily understand how to play the game
- To easily navigate and quit whenever they wish to.

## For Returning visitors
- To practice their guessing skills
- To play guessing game any number of times and improve their guessing skills

# Structure
(to be done)
# Features
- A random word will be generated.
- The user is given a hint and the total number of letters in the word.
- The word is encrypted with a '-' for each letters.
- The computer accepts the user input and gives responsive feedback.
- If the user guessed the correct letter, the letter will be displayed.
- If the user guessed a wrong letter or an invalid entry, the attempt counter will increase by one.
- If the user exhaust all the 10 attempts allowed, then the user loses the game and correct word will be revealed.

## Future features to be implemented
- To store and update user specific data on google sheets.
- Return the top 10 highest scores.
- To generate random word from external dictionary.
- To give word specific hints to make the guessing game more interesting.

# Game Screens
## Welcome Screen
- This screen greets the user with a beautiful Ascii logo of the game. It gives the user option to press enter to play the game 
- The Ascii graffiti was generated using Patorjk.com
		
Screen shot----

## Player Name Screen
This screen asks the user to enter their name to personalise the game.

Screen shot----

## Option Screen
- This screen addresses the user by name 
- Gives the user options to play or the exit the game
		
### Option Screen - menu "1. Play Game"
	
- This screen shows the information about the maximum attempts allowed for the game and the number of attempts made by the user.
- This screen gives the user a hint of the random word.
- And prints blank spaces for each of the letters in the word
- After guessing a correct letter, the guessed letter replaces the blank space.
- If the user guesses a letter that isn't in the word, the "attempts counter" increases
- The user will be informed that the guessed letter is not in the word.
- If the user uses up 10 allowed attempts, and still not guessed all the letters in the word, then the user looses the game and the word is shown.

### Option Screen - menu "2. Exit Game"
- This screen displays a beautiful goodbye screen with a message thanking the user for playing the game
- This screen goes blank after 3 seconds and the game is over.

Screen shot...

## Game Screen
Initial game screen

Correct guessed

Incorrect guessed

Failed screen

Success screen

# Flowchart
- This was my initial plan for the game. this flowchart was created using [Lucid Charts](https://lucid.app/documents#/dashboard).


# Testing
Functional Testing
	
(Testing table to be done)

# Code Validation
- PEP8 pycodestyle

Screen shot------

- Code Institute Linter

Screen shot------

## Fixed Bugs
- [PEP 8 pycodestlye](https://pycodestyle.pycqa.org/en/latest/intro.html) found issues  with the Ascii art especially with "\". I fixed them by replacing them with "\\".
- It also found white spaces in the code which was fixed.
- It also found issues with the length of some lines which was fixed by using (character * n) expression.


## Unfixed Bugs
- One cosmetic error: "run.py:396:80: E501 line too long (95 > 79 characters)" PEP8 issue still exists.
  - I decided against condensing the line for code readability reasons.

# Technologies used
Language:
- [Python](https://www.python.org/): Python was the main language used  to build the whole application.
- Markdown: Markdown was used to write the README.md

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
		
Clone Locally
- Open IDE of choice and type the following into the terminal:
- `git clone https://github.com/pzompa/pp3-python-word-game`		
- Project will now be cloned locally.

# Credits
- Lessons from the Code Institute and the love Sandwiches in learning and understanding python program.
- Watched many YouTube tutorials to learn and understand python programming and took some inspiration from these videos but was created from my own understanding.
- (YouTube) [Build a Word Guessing Game in Python | Python Tutorials For Beginners](https://youtu.be/M1t4RJ5XRHE)
- (YouTube) [Building a Guessing Game | Python | Tutorial 21](https://youtu.be/B9ORjeQlPOA)
- Used google extensively to understand and clear doubts throughout this project.
- Stack overflow, W3 Schools, Educative.io was extensively used throughout this project.
- Ascii Art was made with [Patorjk Website](http://patorjk.com/software/taag/#p=about&f=Graffiti&t=Type%20Something%20).
- Code Institute Mentor Gareth McGiir: Grateful for his useful Tips and advices.
- My family for their support and patience