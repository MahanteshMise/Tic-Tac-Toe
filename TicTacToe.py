# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 23:37:12 2018

@author: Mahantesh Mise
"""

from IPython.display import clear_output
import random

#code for displaying the block
def display_board(board):
    print('\n' * 100)
    print('{:^40}'.format(board[7] + ' |' + board[8] + ' |' + board[9]))
    print('{:^40}'.format("__|__|__"))
    print('{:^40}'.format(board[4] + ' |' + board[5] + ' |' + board[6]))
    print('{:^40}'.format("__|__|__"))
    print('{:^40}'.format(board[1] + ' |' + board[2] + ' |' + board[3]))
    print('{:^40}'.format(" |  | "))

#code for initial numpad demo.
def num_pad(board):
    print('{:^40}'.format(board[7] + ' |' + board[8] + ' |' + board[9]))
    print('{:^40}'.format("__|__|__"))
    print('{:^40}'.format(board[4] + ' |' + board[5] + ' |' + board[6]))
    print('{:^40}'.format("__|__|__"))
    print('{:^40}'.format(board[1] + ' |' + board[2] + ' |' + board[3]))
    print('{:^40}'.format(" |  | "))

#assigning players as 1 and 2 and corresponding marker values
def player_input(player):
    marker = ''
    while (marker != 'X' and marker != '0'):
        marker = input('{},choose X or 0:'.format(player))

    if (player == 'Player1' and marker == 'X'):
        temp_player1 = 'Player1'
        player1_marker = 'X'
        temp_player2 = 'Player2'
        player2_marker = '0'
    elif (player == 'Player1' and marker == '0'):
        temp_player1 = 'Player1'
        player1_marker = '0'
        temp_player2 = 'Player2'
        player2_marker = 'X'
    elif (player == 'Player2' and marker == 'X'):
        temp_player1 = 'Player1'
        player1_marker = '0'
        temp_player2 = 'Player2'
        player2_marker = 'X'
    elif (player == 'Player2' and marker == '0'):
        temp_player1 = 'Player1'
        player1_marker = 'X'
        temp_player2 = 'Player2'
        player2_marker = '0'
    else:
        pass

    return (temp_player1, player1_marker, temp_player2, player2_marker)

#Checking winning conditions
def win_check(board):

    if ((board[9] == 'X' and board[6] == 'X' and board[3] == 'X') or
        (board[8] == 'X' and board[5] == 'X' and board[2] == 'X') or
        (board[7] == 'X' and board[4] == 'X' and board[1] == 'X') or
        (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or
        (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or
        (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or
        (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or
        (board[7] == 'X' and board[5] == 'X' and board[1] == 'X')):
         return ('X_Win')

    elif ((board[9] == '0' and board[6] == '0' and board[3] == '0') or
          (board[8] == '0' and board[5] == '0' and board[2] == '0') or
          (board[7] == '0' and board[4] == '0' and board[1] == '0') or
          (board[7] == '0' and board[8] == '0' and board[9] == '0') or
          (board[4] == '0' and board[5] == '0' and board[6] == '0') or
          (board[1] == '0' and board[2] == '0' and board[3] == '0') or
          (board[1] == '0' and board[5] == '0' and board[9] == '0') or
          (board[7] == '0' and board[5] == '0' and board[1] == '0')):
          return ('0_Win')

    else:
        pass
#Randomly choosing which player goes first
def choose_first():
    x = random.randint(1, 3)
    if (x == 1):
        return ("Player1")
    else:
        return ("Player2")


#Do confirm whether the players want to play the game again
def replay():
    x = input("Do you want to play again Y/N?")
    if (x == 'y' or x == 'Y'):
        return (True)
    elif (x == 'N' or x == 'n'):
        return (False)
    else:
        print("Invalid Input")


#Main code begins here
print('{:-^40}'.format("Welcome to TicTacToe"))
while(True):
    print('\n')
    print("Please choose your positions based on the numpad values as shown in the board below.")
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_pad(board)
    player = choose_first()
    print('\n' * 2)
    print('{} starts the game!!!'.format(player))
    Player1, Player1_marker, Player2, Player2_marker = player_input(player)

    while(win_check(board) != 'X_Win' and win_check(board) != '0_Win'):
        player_choice = int(input('{} Please select your option from numpad(1-9)'.format(player)))
        #        flag = 0
        while(True):
            if(board[player_choice] == 'X' or board[player_choice] == '0'):
                print("{} option is already taken.Please select another".format(player_choice))
                player_choice = int(input('{} Please select your option from numpad(1-9)'.format(player)))
                continue
            else:
                # if (board[player_choice] == 'X' or board[player_choice] == '0'):
                #     flag = 0
                # else:
                #     flag = 1
                break

        if(player == Player1):
            board[player_choice] = Player1_marker
        else:
            board[player_choice] = Player2_marker

        display_board(board)

        if (player == Player1):
            player = Player2
        else:
            player = Player1

    if((win_check(board)) == 'X_Win'):
        if(Player1_marker == 'X'):
            print("Player1 Wins!!!")
        else:
            print("Player2 Wins!!!")
    elif((win_check(board)) == '0_Win'):
        if (Player1_marker == 'X'):
            print("Player1 Wins!!!")
        else:
            print("Player2 Wins!!!")


    if(replay()==True):
        continue
    else:
        break
