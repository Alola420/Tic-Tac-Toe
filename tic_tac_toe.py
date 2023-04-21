
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])



#player 1 makes the choice of input before starting
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose between X or O player 1: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



#to see if any player has won the game
def check_win(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 



#placing the player's marker on desired position
def place_mark(marker, position, board):
    board[position] = marker

def space_check(board, position):
    if board[position] == " ":
        return True
    else: return False

#to check if there is no empty space left on the board
def full_check(board):
    for i in range(1, 10):
        if space_check(board, i) == True: 
            return False
    return True



# randomly deciding which player goes first in the game
import random
def first_player():
    if random.randint(0, 1) == 0:
        return 'Player2'
    else: return 'Player1'

#asks player for next position and returns it for later use
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position): #position must be valid
        position = int(input("choose your position from 1-9: "))
    return position

#choice to replay
def replay():
    choice = input("do you want to play again? (Y/N) : ").lower()
    if choice == 'y':
        return True
    else:
        return False

#main function
print("Welcome to tic tac toe")
while True:
    play_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    curr = first_player()
    print(curr + ' will move first')

    start_play = input('Start tic tac toe? (Y/N): ').lower()
    if (start_play == 'y'):
        start_game = True
    else:
        start_game = False
    
    while (start_game == True):
        #check if it is player1's turn to start the game
        if curr == 'Player1':
            display_board(play_board)
            spot = player_choice(play_board)
            place_mark(player1_marker, spot, play_board)

            if check_win(play_board, player1_marker):
                display_board(play_board)
                print("Player1 has won the game")
                start_game = False
            else:
                if full_check(play_board):
                    display_board(play_board)
                    print("It's a draw")
                    break
                else:
                    curr = "player2"
        else:
            display_board(play_board)
            spot = player_choice(play_board)
            place_mark(player2_marker, spot, play_board)

            if check_win(play_board, player2_marker):
                display_board(play_board)
                print("Player2 has won the game")
                start_game = False
            
            else:
                if full_check(play_board):
                    display_board(play_board)
                    print("It's a draw")
                    break
                else:
                    curr = 'Player1'
    if not replay():
        print('game over')
        break












    

