#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    for r in range(row):
        if (
            board[r][col] == 1
            or (col - (row - r) >= 0 and board[r][col - (row - r)] == 1)
            or (col + (row - r) < n and board[r][col + (row - r)] == 1)
        ):
            return False
    return True


def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append([list(row) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def solve_nqueens(n):
    solutions = []
    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
    else:
        solutions = solve_nqueens(n)
        for solution in solutions:
            for row in solution:
                print(" ".join("Q" if cell == 1 else "." for cell in row))
            print()
