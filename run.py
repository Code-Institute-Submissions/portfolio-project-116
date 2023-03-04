import random

print("=" * 39)
print(" Welcome to a game of Battleships!")
print(" Guess a row and column between 0 & 4.")
print("=" * 39)

"""
Creates a board in a square, with dims. 
"""


def make_board(dims):
    return [["O" for count in range(dims)] for count in range(dims)]


def generate_board(board):
    for i in board:
        print(*i)


board = make_board(5)
generate_board(board)

