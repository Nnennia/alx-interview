#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    def solve(board, col):
        if col >= N:
            solutions.append(board.copy())
            return
        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(board, col + 1)
                board[row][col] = 0

    solutions = []
    initial_board = [[0] * N for _ in range(N)]
    solve(initial_board, 0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        for row in solution:
            print(' '.join(map(str, row)))
        print()


if __name__ == "__main__":
    main()
