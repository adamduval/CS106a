"""
File: lecture_13_tictactoe.py
-----------------
This file is a self coded version of the lecture 13 tictactoe code.

From lecture code:
"This program allows to players to play tic-tac-toe.  The board in
the game is SIZE x SIZE, set using the constant SIZE.  Each element
on the board will contain either 'X', 'O', or None to indicate that
either a particular player occupies a particular space in the grid
or the space is empty (contains None)."

Complete - Make empty board from SIZE, rows and columns as list in list
Complete - Draw empty board adn updated board
Complete - Check for vertical row winner
Complete - Check for horizontal row winner
Complete - Check for diagonal row winner
Complete - X turn entry
Complete - Y turn entry
Complete - check all win conditions
Complete - check for invalid move
Complete - win to end the game
Complete - set draw condition
Complete - check conditions using bigger boards 4x4 and up, wins and draws
Complete - how can i make game ask and execute would you like to play again?
Complete - check for invalid move if row/column is greater than game board
"""

# game board size (number of rows and columns)
SIZE = 3


# makes a list of lists (columns x rows) of SIZE
def make_empty_board(size):
    board = []
    # make rows
    for i in range(size):
        # make columns, need to append none to account for number of columns
        columns = []
        for j in range(size):
            columns.append(None)
        board.append(columns)
    return board


# places X at specific row and column
def x_turn(board):
    print('Player X it is your turn')
    row = input('Choose row: ')
    column = input('Choose column: ')
    while row >= str(len(board)) or column >= str(len(board)) or board[int(row)][int(column)] is not None:
        print('Invalid Move')
        row = input('Choose row: ')
        column = input('Choose column: ')
    remove_value(row, column, board)
    board[int(row)].insert(int(column), 'X')
    return board


# places O at specific row and column
def o_turn(board):
    print('Player O it is your turn')
    row = input('Choose row: ')
    column = input('Choose column: ')
    while row >= str(len(board)) or column >= str(len(board)) or board[int(row)][int(column)] is not None:
        print('Invalid Move')
        row = input('Choose row: ')
        column = input('Choose column: ')
    remove_value(row, column, board)
    board[int(row)].insert(int(column), 'O')
    return board


# removes none entry at specified column and row
def remove_value(row, column, board):
    board[int(row)].pop(int(column))


# checks all possible winning conditions
def check_for_winner(board):
    if check_horizontal_winner(board):
        return True
    if check_vertical_winner(board):
        return True
    if check_diagonal_winner_from_left(board):
        return True
    if check_diagonal_winner_from_right(board):
        return True
    return False


# checks to see if all spaces are filled but not winning condition
def check_for_draw(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is None:
                return False
    return True


# check for vertical winner
def check_horizontal_winner(board):
    for i in range(len(board)):
        check = []
        for j in range(len(board)):
            check.append(board[i][j])
        if check.count('X') == len(board) or check.count('O') == len(board):
            return True
    return False


# check for vertical row winner (len(board) in a row), player is x or O
def check_vertical_winner(board):
    for i in range(len(board)):
        # values in column are added to list and compared to number of X's or O's to win
        check = []
        for j in range(len(board)):
            # need to flip j/i to check down column instead of row
            check.append(board[j][i])
        if check.count('X') == len(board) or check.count('O') == len(board):
            return True
    return False


# check from top left to bottom right for winning condition, returns True if there is a winner
def check_diagonal_winner_from_left(board):
    winner = board[0][0]
    if winner is None:
        return False
    for i in range(len(board)):
        if board[i][i] != winner:
            return False
    return True


# check from top right to bottom left for winning condition, returns True if there is a winner
def check_diagonal_winner_from_right(board):
    winner = board[0][len(board)-1]
    if winner is None:
        return False
    for i in range(len(board)):
        if board[i][len(board)-i-1] != winner:
            return False
    return True


# draw game board of SIZE x SIZE
def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'X':
                if j < (len(board)-1):
                    print(' X |', end='')
                else:
                    print(' X ', end='')
            elif board[i][j] == 'O':
                if j < (len(board)-1):
                    print(' O |', end='')
                else:
                    print(' O ', end='')
            # to account for last column
            elif j == (len(board)-1):
                print('   ', end='')
            else:
                print('   |', end='')
        # line separator will print all rows but last
        if i < (len(board)-1):
            print('')
            print_line_sep(board)
    print('')


# print lines between squares
def print_line_sep(board):
    for i in range(len(board)-1):
        print('---+', end='')
    print('---')


def main():
    play = 'yes'
    while play == 'yes':
        game_board = make_empty_board(SIZE)
        draw_board(game_board)
        winner = False
        draw = False
        while winner is False:
            if winner is False:
                player = 'X'
                x_turn(game_board)
                draw_board(game_board)
                winner = check_for_winner(game_board)
                draw = check_for_draw(game_board)
                if draw is True:
                    winner = check_for_draw(game_board)
            if winner is False:
                player = 'O'
                o_turn(game_board)
                draw_board(game_board)
                winner = check_for_winner(game_board)
                draw = check_for_draw(game_board)
                if draw is True:
                    winner = check_for_draw(game_board)
        if draw is True:
            print('Draw, nobody wins!')
        else:
            print('Player ', player, ' wins!')
        play = input('Do you want to play again? Yes or No: ')
    print('Goodbye')


if __name__ == '__main__':
    main()
