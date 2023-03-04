import random

print("=" * 35)
print(" Welcome to a game of Battleships!")
print(" Guess a row and column between\n 1 and 5.")
print("=" * 35)

"""
Creates a board in a square, with dims. 
"""


def make_board(dims):
    return [["*" for count in range(dims)] for count in range(dims)]


def generate_board(board):
    for i in board:
        print(*i)


board = make_board(5)
generate_board(board)

"""
Creates and returns ship coordinates
by using length of the ship with a random number
between 2 and the length of the board.

Orientation == 0: ship is horizontal,
Orientation == 1: ship is vertical.
"""


def build_ship(dims):
    ship_len = random.randint(2, dims)
    orientation = random.randint(0, 1)

    if orientation == 0:
        ship_row = [random.randint(0, dims - 1)] * ship_len
        col = random.randint(0, dims - ship_len)
        ship_col = list(range(col, col + ship_len))
        coords = tuple(zip(ship_row, ship_col))
    else:
        ship_col = [random.randint(0, dims - 1)] * ship_len
        row = random.randint(0, dims - ship_len)
        ship_row = list(range(row, row + ship_len))
        coords = tuple(zip(ship_row, ship_col))
    return list(coords)


ship = build_ship(5); ship


"""
Function for player guesses
"""


def player_guess():
    row = int(input("Guess row:\n")) - 1
    col = int(input("Guess column:\n")) - 1
    print("=" * 38)
    return (row, col)


x = player_guess(); x


def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print("You've already guessed that!")
        print("=" * 38)
        return board
    guesses.append(guess)
    if guess in ship:
        print("It's a hit!")
        print("=" * 38)
        """
        'X' = hit
        """
        board[guess[0]][guess[1]] = "X"
        """
        ship.remove = for while loop in main()
        """
        ship.remove(guess)
        return board
    print("You missed!")
    print("=" * 38)
    return board


guesses = []
our_guess = player_guess()
board = update_board(our_guess, board, ship, guesses)
    

generate_board(board)


"""
Main function to call all code.
"""


def main():
    board = make_board(5)
    ship = build_ship(5)
    guesses = []
    while len(ship) > 0:
        board = update_board(player_guess(), board, ship, guesses)
        generate_board(board)
    print("You sunk my ship!")
    print("=" * 38)
    return


main()
