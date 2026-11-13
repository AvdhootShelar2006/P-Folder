# Sudoku Solver Using Backtracking and Constraint Propagation Part A

def candidates(board, row, col):
    used = set(board[row])
    used.update(board[r][col] for r in range(9))
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    used.update(board[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3))
    return set(range(1, 10)) - used


def valid_givens(board):
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value:
                board[r][c] = 0
                allowed = value in candidates(board, r, c)
                board[r][c] = value
                if not allowed:
                    return False
    return True


def find_empty_mrv(board):
    best = None
    best_values = None
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = candidates(board, r, c)
                if best is None or len(options) < len(best_values):
                    best, best_values = (r, c), options
                if not options:
                    return (r, c), options
    return best, best_values


def solve(board):
    cell, options = find_empty_mrv(board)
    if cell is None:
        return True
    if not options:
        return False
    r, c = cell
    for value in sorted(options):
        board[r][c] = value
        if solve(board):
            return True
        board[r][c] = 0
    return False


def read_row(prompt):
    try:
        row = list(map(int, input(prompt).split()))
    except ValueError:
        return None
    if len(row) == 9 and all(0 <= x <= 9 for x in row):
        return row
    return None


def main():
    print("Enter 9 rows of Sudoku. Use 0 for empty cells.")
    board = []
    for i in range(9):
        row = read_row(f"Row {i + 1}: ")
        while row is None:
            print("Enter exactly 9 numbers between 0 and 9.")
            row = read_row(f"Row {i + 1}: ")
        board.append(row)
    original = [row[:] for row in board]
    if valid_givens(board) and solve(board):
        print("Solved Sudoku:")
        for row in board:
            print(*row)
    else:
        print("No solution exists for the entered Sudoku.")
        print("Original puzzle:")
        for row in original:
            print(*row)


if __name__ == "__main__":
    main()
