

#displays board
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

#takes player choice for marker
def player_input():
    marker = ''

    while  not (marker == 'X' or marker == 'O'):
        marker = input('Do you want to be X or O: ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

import random

#places marker at given posistion
def place_marker(board, marker, position):

    board[position] = marker 

#checks for win condition
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#picks who goes first
def choose_first():
    x =  random.randint(0, 9)
    who = ''
    if x % 2 == 0:
        who = 'Player 1'
    else:
        who = 'Player 2'
    return who

#Checks to see if space is free
def space_check(board, position):
    if board[position] == 'O' or board[position]  == 'X':
        return False
    else:
        return True

#checks weather board is full or not
def full_board_check(board):
    x = ' '
    if x not in board:
        return True
    else:
        return False
    
#ask for players next posistion and checks if free
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Pick a posistion on the board (1-9): '))

    return position

#ask if player wants to play again
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = ['#'] + [" "]*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')
  
    play_game = input('Are you ready to play? (Y/N)')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congrats you won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congrats you won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break