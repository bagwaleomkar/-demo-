
def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check diagonals
    for i in range(row):
        for j in range(n):
            if board[i][j] == "Q" and abs(row-i) == abs(col-j):
                return False

    return True


def solve(board, row, n):

    if row == n:
        for r in board:
            print(" ".join(r))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            solve(board, row+1, n)

            board[row][col] = "0"


n = int(input("Enter board size: "))
board = [["0"] * n for i in range(n)]

solve(board, 0, n)

