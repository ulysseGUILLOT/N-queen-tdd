def create_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def display_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print (board[i][j],end=' ')
        print()


def is_safe(board, row, col, n):
    # Vérifie la ligne à gauche
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Vérifie la diagonale supérieure gauche
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Vérifie la diagonale inférieure gauche
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0

def solve_nqueens(n):
    if n == 1:
        return [[1]]
    return []