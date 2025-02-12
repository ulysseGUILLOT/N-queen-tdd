def create_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def display_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print (board[i][j],end=' ')
        print()


def solve_nqueens(n):
    if n == 1:
        return [[1]]
    return []

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

