#Legend
# X for placing ship and hit battleship
# " " for available space
# "-" for missed shot 

from random import randint

OUR_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F':5, 'G':6, 'H': 7 }

def board(board):
    result = '  A B C D E F G H\n'
    result += '  ---------------\n'
    row_number = 1
    for row in board:
        result += "%d|%s|\n" % (row_number, "|".join(row))
        row_number += 1
    return result
def create_ships(board):
    for ship in range(5):
        ship_row = randint(0,7)
        ship_column = randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row = randint(0,7)
            ship_column = randint(0,7)
        board[ship_row][ship_column] = 'X'


def attack_ship():
    row = input("Enter a ship row 1-8")
    while row not in "12345678":
        print("Please enter a ship row 1-8")
        row = input("Please enter a ship row 1-8")
    column = input("Please enter a ship column A-H").upper()
    while column not in "ABCDEFGH":
        print("Please enter a valir column")
        column = input("Please enter a ship column A-H").upper()
    return int(row) -1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count +=1
    return count

def play_game():
    create_ships(OUR_BOARD)
    create_ships(COMPUTER_BOARD)
    turns = 10
    while turns > 0:
        print("Welcome to Battleship!")
        
        print(board(OUR_BOARD))
        print(board(COMPUTER_BOARD))
        row, column = attack_ship()
        if COMPUTER_BOARD[row][column] == "-":
            print('You already have guessed that, try somewhere else')
        elif OUR_BOARD[row][column] == 'X':
            print("ITS A HIT!!! GOODJOB!!!")
            COMPUTER_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("Sorry, you missed!")
            COMPUTER_BOARD[row][column] = '-'
            turns -= 1
        if count_hit_ships(COMPUTER_BOARD)==5:
            print("Congratulations all the ships are sunk! You won!")
            break
        print(f"You have {turns} turns left")
        if turns == 0:
            print("Sorry, No more turns, Game Over")
            break


playgame()
