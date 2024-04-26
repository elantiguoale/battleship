#Legend
# X for placing ship and hit battleship
# " " for available space
# "-" for missed shot 

import random

OUR_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F':5, 'G':6, 'H': 7 }

def board(board):
    print('     A B C D E F G H')
    print("     ---------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship range(5):
        ship_row = randint(0,7)
        ship_column = randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row = randint(0,7)
            ship_column = randint(0,7)
        board[ship_column][ship_column] = 'X'


def get_ship_location():
    row = input("Enter a ship row 1-8")
    while row not in "12345678":
        print("Please enter a ship row 1-8")
        row = input("Please enter a ship row 1-8")
    column = input("Please enter a ship column A-H").upper()
    while column not in "ABCDEFGH":
        print("Please enter a valir column")
        column = input("Please enter a ship column A-H").upper()
    return int(row) -1, letters_to_numbersp[column]


def count_hit_ships():
    pass
