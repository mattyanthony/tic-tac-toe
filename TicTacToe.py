#Impossible to beat TicTacToe game
#Author: Matthew Anthony

'''This is a classic game of tictac toe where the user (player X) will play against the computer (player O)
To play, you can simply download this .py file and open up your command prompt on windows. Assuming you have python
downloaded from the Microsoft store, simply type "cd Downloads" followed by "python TicTacToe.py".
This game uses the minimax algorithm which essentially renders the AI player as impossible to beat.
Do you think you can do it?'''

import random
import math

print("Welcome to Tic Tac Toe!")
print("You will be playing as player X against the computer, player O.")
print("The rules are simple: get 3 X's in a row to win!")
print("Play your move by typing a number 0-8. The number correlates with the position on the board like this:\n")
print("| 0 | 1 | 2 |")
print("-------------")
print("| 3 | 4 | 5 |")
print("-------------")
print("| 6 | 7 | 8 |\n")
print("Good luck!\n")
print("---------------------------------------\n")

PLAYER_X = 'X'
PLAYER_O = 'O'

def draw_board(board):
    #The playing board
    #9 indexes belonging to "board" with various dashes and 
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def is_winner(board, player):
    #All possible win combos done using and/or statements and board indexes
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def is_board_full(board):
    #Checks if the board is full/tie game
    for i in range(9):
        if board[i] == ' ': #if any index on the board is empty, the board is not full therefore false
            return False
    return True #if every index has a value, board is full

def get_empty_cells(board):
    #So we can see all the empty indexes
    #enumerate and list comprehension research helped greatly here
    return [i for i, cell in enumerate(board) if cell == ' '] #use enumerate to get a list of empty indexes

    
def computer_move(board, computer_player):
    if computer_player == PLAYER_O: #AI plays as O
        best_score = float('-inf') #negative infinity is best possible score 
        best_move = None
        for cell in get_empty_cells(board): #loop goes over each index, using previous empty_cell function to return a list
            board[cell] = computer_player #temp O in all cells to use for calculations 
            score = minimax(board, 0, False, -math.inf, math.inf) #uses minimax to calculate score based on current board
            board[cell] = ' ' #take the O off from 2 lines prior 
            if score > best_score: #if the calculated score is better than the previous best score, update it new best score
                best_score = score
                best_move = cell
        return best_move #returns best score after calculating every possiblity in minimaxWher


def minimax(board, recur, maximizing_player, alpha, beta): #state of the board currently, recursion level, player who needs the help
    if is_winner(board, PLAYER_O): #AI winner returns 1
        return 1
    elif is_winner(board, PLAYER_X): #-1 is if the human wins (unlikely)
        return -1
    elif is_board_full(board): #a tie is 0
        return 0

    if maximizing_player: #all very similar to computer_move however minimax is recursively called here
        max_eval = float('-inf') #negative infinity to represent highest minimax score
        for cell in get_empty_cells(board): #similar to computer_move, iterates over each empty cell
            board[cell] = PLAYER_O #temp 0 is stored for simulation purposes
            eval = minimax(board, recur + 1, False, alpha, beta) #recursively calls minimax for the next move
            board[cell] = ' ' #remove temp 0 
            max_eval = max(max_eval, eval) #update new highest score
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval #return highest score
    else:
        min_eval = float('inf')
        for cell in get_empty_cells(board):
            board[cell] = PLAYER_X
            eval = minimax(board, recur + 1, True, alpha, beta)
            board[cell] = ' '
            min_eval = min(min_eval, eval) #opposite of above statement, they want the highest for AI and lowest for human
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def play_game():
    while True: #allows the play_again input to work/loops this function
        board = [' '] * 9  #adds 9 blank spots for indexes 
        current_player = 'X' #sets the starting plays, human is X AI is O
        
        while True: #turn loop
            draw_board(board) #prints the current game board
            
            if current_player == 'X':
                #Human player's turn
                move = int(input('Enter your move (0-8): '))
                
                if board[move] != ' ': #making sure you are not selecting an occupied index, asks to try again if it is
                    print('That space has already been played. Choose another position')
                    continue
                
                board[move] = current_player #updates board with the move
                print('You played move:', move)
            else:
                #Computer player's turn
                move = computer_move(board, current_player) #calls computer_move funtion to get AI move
                board[move] = current_player #updates board with the move
                print('Computer played move:', move)
            
            if is_winner(board, current_player): #checks if current player is a winner using is_winner function
                draw_board(board)
                print('Player', current_player, 'wins!')  #last person to move/current player will always be the winner
                break
            elif is_board_full(board): #if the board is full, it is a tie game
                draw_board(board)
                print("It's a tie!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X' #switches player's turns for the next turn iteration
        
        play_again = input('Do you want to play again? (y/n): \n') #user input, y = play again, n = quit out
        if play_again.lower() != 'y':
            break


play_game()

print("---------------------------------------")
print("Thanks for playing!")
