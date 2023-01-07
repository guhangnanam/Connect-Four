def initialize_board(num_rows, num_cols):
    return [["-" for i in range(num_cols)] for j in range(num_rows)]

def print_board(board):
    for row in reversed(board):
        for col in row:
            print(col, end = " ")
        print()

def available_square(board, row, col):
    return board[row][col] == "-"


def insert_chip(board, col, chip_type):
    for i in range(0, num_rows):
        if board[i][col] == "-":
            board[i][col] = chip_type
            row = i
            return row
def board_is_full(board):
    for row in board:
        for chip in row:
            if chip == "-":
                return False
    return True
def check_if_winner(board, col, row, chip_type):
    count = 0
    # check horizontal
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    # check vertical
    count_2 = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count_2 += 1
            if count_2 == 4:
                return True
        else:
            count_2 = 0



    return False


if __name__ == "__main__":
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows, num_cols)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o")

    player = 1
    chip_type = "x"
    row = 0

    game_continue = True
    while game_continue:

        col = int(input(f"Player {player}: Which column would you like to choose? "))

        row_val = insert_chip(board, col, chip_type)
        print_board(board)

        # check if someone has won
        if check_if_winner(board, col, row_val, chip_type) == True:
            print(f"\nPlayer {player} won the game!")
            game_continue = False
            break

        if board_is_full(board) == True:
            print("Draw. Nobody wins.")
            game_continue = False
            break


        # alternate player
        if player == 1:
            player = 2
        else:
            player = 1

        chip_type = 'o' if chip_type == 'x' else "x"









