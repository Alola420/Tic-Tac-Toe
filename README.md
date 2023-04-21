# Tic-Tac-Toe
User Interactable Tic Tac Toe game

This project aims to develop a Tic Tac Toe game using python. It mainly consists of designing a computer program that pits you in a game 
of Tic Tac Toe against another player.

Rules of Tic Tac Tac Toe:

Tic Tac Toe is a game between two players. The players choose between inputs 'X' and 'O'.
The two players take turns placing their respective markers on a 3x3 board and the game continues until either the board is full, or one of the players
has managed to place 3 of their markers in a row: either horizontally, vertically or diagonally.

Given below are the components used to code the program:

Board Representation: Designing a data structure to represent the game board, in this case an array was used, and using print statements 
it served as a 2-D array, to keep track of the current state of the game.

Checking for Space: Checking the board before each turn to see if there is a position available on the board for the player to insert their marker.

Player Input: Mechanism for players to input their moves, through the command line, and validating their input to ensure it is a 
valid move within the rules of Tic Tac Toe, otherwise they are asked to re-enter their values

Game Logic: Determining the state of the game, such as checking for win conditions, identifying draws, and updating the board accordingly after each move.

Game Loop: The game continues until a win or draw stage is reeached by continually checking for a win or draw at the end of every turn.

User Interface: A user-friendly interface for players to interact with, displaying the game board and prompting for player input.

Error Handling: Checking for invalid inputs and illegal moves from the player.


