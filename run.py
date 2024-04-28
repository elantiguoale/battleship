# Legend
# S for ship locations
# X for battleships hit
# " " for available space
# "-" for missed shot

from random import randint
from random import choice

global attacked_positions


OUR_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
HIDDEN_BOARD = [[" "] * 8 for i in range(8)]

letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
}


def board(board):
    result = '  A B C D E F G H\n'
    result += '  ---------------\n'
    row_number = 1
    for row in board:
        result += "%d|%s|\n" % (row_number, "|".join(row))
        row_number += 1
    return result


def create_ships(board):
    for ship in range(10):
        ship_row = randint(0, 7)
        ship_column = randint(0, 7)
        while board[ship_row][ship_column] == "S":
            ship_row = randint(0, 7)
            ship_column = randint(0, 7)
        board[ship_row][ship_column] = 'S'


def attack_ship():
    while True:
        row = input("Enter a ship row 1-8: ").strip()
        if row and row in "12345678":
            break
        print("Please enter a valid ship row 1-8")
    while True:
        column = input("Enter a ship column A-H: ").strip().upper()
        if column and column in "ABCDEFGH":
            break
        print("Please enter a valid column (A-H)")
    return int(row) - 1, letters_to_numbers[column]


def computer_attack(attacked_positions):
    while True:
        row = randint(0, 7)
        column = randint(0, 7)
        if (row, column) not in attacked_positions:
            attacked_positions.append((row, column))
            return row, column


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def play_game():
    attacked_positions = []
    print("==================================================")
    print("           Welcome to Battleship!")
    print("To win you need to sink all the computers ships")
    print("both you and the computer have 10 ships")
    print("                 GOODLUCK!!!")
    print("==================================================")
    while True:
        print("This is your Board")
        print(board(OUR_BOARD))
        print("This is the Computers Board")
        print(board(HIDDEN_BOARD))
        row, column = attack_ship()
        # YOUR TURN
        while COMPUTER_BOARD[row][column] == "-":
            print('You already have guessed that, try somewhere else')
            row, column = attack_ship()
        if COMPUTER_BOARD[row][column] == 'S':
            print("ITS A HIT!!! GOODJOB!!!")
            COMPUTER_BOARD[row][column] = "X"
            HIDDEN_BOARD[row][column] = "X"
        else:
            print("Sorry, you missed!")
            COMPUTER_BOARD[row][column] = '-'
            HIDDEN_BOARD[row][column] = "-"
        if count_hit_ships(COMPUTER_BOARD) == 10:
            print("Congratulations all the ships are sunk! You won!")
            break
        # COMPUTERS TURN
        row, column = computer_attack(attacked_positions)
        if OUR_BOARD[row][column] == "S":
            print("The computer hits your ship!")
            OUR_BOARD[row][column] = "X"
        else:
            print("The computer misses your ship!")
            OUR_BOARD[row][column] = "-"

        if count_hit_ships(OUR_BOARD) == 10:
            print("Oh no! The computer sank all your ships! You lost!")
            break


create_ships(OUR_BOARD)
create_ships(COMPUTER_BOARD)
turns = 10
play_game()
