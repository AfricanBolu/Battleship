from random import randint

# board set up
hidden_board = []
guess_board = []
# count = 0

letter_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

for x in range(1, 8):
    hidden_board.append([" "] * 8)
    guess_board.append(["O"] * 8)


# prints the board to screen.
def print_board(ship_board):
    print('  A B C D E F G H')
    # print('  ---------------')
    row_num = 1
    for ship_row in ship_board:
        print("%d|%s|" % (row_num, "|".join(ship_row)))
        row_num += 1


def create_ship(ship_board):
    for ship in range(5):
        ship_row, ship_col = randint(0, 5), randint(0, 5)
        while ship_board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0, 5), randint(0, 5)
        ship_board[ship_row][ship_col] = 'X'


def get_ship_location():
    chosen_row = input("Enter a row 1-8: ")
    try:
        while chosen_row not in '12345678':
            print('Please enter a valid row: ')
            chosen_row = input("Enter a row 1-8")
        chosen_col = input("Enter a column 1-8: ").upper()
        while chosen_col not in 'ABCDEFGH':
            print('Please enter a valid column: ')
            chosen_col = input("Enter a column 1-8: ").upper()
        return int(chosen_row) - 1, letter_to_number[chosen_col]
    except TimeoutError:
        print('Error occurred.')


def count_hit_ships(board):
    count = 0
    for ship_row in board:
        for ship_col in ship_row:
            if ship_col == 'X':
                count += 1
    return count


create_ship(hidden_board)
print('Hidden board: ')
print_board(hidden_board)
print('\n\n Guess board: ')
print_board(guess_board)
for turn in range(5):
    row, col = get_ship_location()
    if guess_board[row][col] == "-":
        print("You guessed that one already.")
    elif hidden_board[row][col] == "X":
        print("Congratulations! You sunk my battleship!")
        guess_board[row][col] = "X"
    else:
        print("You missed my battleship!")
        guess_board[row][col] = "-"
    if turn == 5:
        print("Game Over")
    # Print (turn + 1) here!
    print_board(guess_board)
    print("Turn", turn + 1)
