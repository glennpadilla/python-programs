import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_board(board):
    print("Let's play Tic-Tac-Toe!")
    print()
    for row_number, row in enumerate(board):
        print(" " + " | ".join(row) + " ")
        if row_number + 1 != len(board):
            separator = "---+" * 3
            print(separator[0:-1])
    print()


def has_winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][0]


def is_tie(board):
    return all([value == "X" or value == "O" for row in board for value in row])


def play_o(board):
    positions = [[1, 1], [0, 1], [1, 0], [1, 2], [2, 1], [0, 0], [0, 2], [2, 0], [2, 2]]
    for row, column in positions:
        if board[row][column] not in ["X", "O"]:
            board[row][column] = "O"
            return


def play_game():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    while not has_winner(board) and not is_tie(board):
        response = None
        clear()
        print_board(board)
        while response is None:
            try:
                response = int(input("Choose a number to play X in: ")) - 1
                if response < 0 or response > 8:
                    raise ValueError("Not a good value")

                row = response // 3
                column = response % 3
                space = board[row][column]
                if space == "X" or space == "O":
                    raise ValueError("Not an empty space")
                else:
                    board[row][column] = "X"
                play_o(board)
            except ValueError:
                response = None
                print("That is not a valid value")
    clear()
    print_board(board)
    if has_winner(board):
        print(f"The winner is {has_winner(board)}!")
    else:
        print(f"It's a tie!")


if __name__ == "__main__":
    play_game()
