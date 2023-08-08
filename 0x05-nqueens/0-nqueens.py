#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def is_safe(placed_queens, row, col):
    for r, c in placed_queens:
        if col == c or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n):
    solutions = []

    def backtrack(row, placed_queens):
        if row == n:
            solutions.append(placed_queens[:])
            return

        for col in range(n):
            if is_safe(placed_queens, row, col):
                placed_queens.append((row, col))
                backtrack(row + 1, placed_queens)
                placed_queens.pop()

    backtrack(0, [])
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)
