# Model-Based Grid Navigation Agent Part A

from collections import deque


class ModelBasedAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.internal_map = [row[:] for row in grid]

    def find_path(self):
        rows, cols = len(self.internal_map), len(self.internal_map[0])
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            (r, c), path = queue.popleft()
            if (r, c) == self.goal:
                return path
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and self.internal_map[nr][nc] != "#" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
        return None


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a whole number.")


def read_point(prompt):
    try:
        values = tuple(x - 1 for x in map(int, input(prompt).split()))
    except ValueError:
        return None
    return values if len(values) == 2 else None


def main():
    rows = read_int("Enter grid rows: ")
    cols = read_int("Enter grid columns: ")
    if rows < 1 or cols < 1:
        print("Rows and columns must be at least 1.")
        return
    grid = []
    print("Enter each row using . for free cell and # for obstacle.")
    for i in range(rows):
        while True:
            line = input(f"Row {i + 1}: ").strip().replace(" ", "")
            if len(line) == cols and all(ch in ".#" for ch in line):
                grid.append(list(line))
                break
            print(f"Enter exactly {cols} characters using only . and #.")
    start = read_point("Enter start row and column (1-based): ")
    goal = read_point("Enter goal row and column (1-based): ")
    if start is None or goal is None:
        print("Enter two numbers for the start and for the goal.")
        return

    for point in (start, goal):
        if not (0 <= point[0] < rows and 0 <= point[1] < cols) or grid[point[0]][point[1]] == "#":
            print("Start and goal must be valid free cells.")
            return

    agent = ModelBasedAgent(grid, start, goal)
    path = agent.find_path()
    if path:
        print("Path found:", " -> ".join(str((r + 1, c + 1)) for r, c in path))
        print("Number of moves:", len(path) - 1)
    else:
        print("No path exists.")


if __name__ == "__main__":
    main()
