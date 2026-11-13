# Eight Queens Backtracking Constraint Satisfaction Part B

def solve_queens(n):
    solutions = []
    positions = []

    def backtrack(row, columns, diag1, diag2):
        if row == n:
            solutions.append(positions[:])
            return
        for col in range(n):
            if col not in columns and row - col not in diag1 and row + col not in diag2:
                positions.append(col)
                backtrack(row + 1, columns | {col}, diag1 | {row - col}, diag2 | {row + col})
                positions.pop()

    backtrack(0, set(), set(), set())
    return solutions


def read_int(prompt, default):
    while True:
        text = input(prompt).strip()
        if not text:
            return default
        try:
            return int(text)
        except ValueError:
            print("Enter a whole number.")


def main():
    n = read_int("Enter board size (default 8, press Enter): ", 8)
    if not 1 <= n <= 12:
        print("Enter a board size from 1 to 12.")
        return
    solutions = solve_queens(n)
    print(f"Total solutions for {n}-Queens: {len(solutions)}")
    if solutions:
        choice = read_int(f"Choose solution number (1-{len(solutions)}, default 1): ", 1)
        if not 1 <= choice <= len(solutions):
            print("Invalid solution number.")
            return
        solution = solutions[choice - 1]
        for row in range(n):
            print(" ".join("Q" if solution[row] == col else "." for col in range(n)))


if __name__ == "__main__":
    main()
