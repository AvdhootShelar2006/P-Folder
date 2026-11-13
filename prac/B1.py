# BFS Planning Problem Part B

from collections import deque


def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        position, path = queue.popleft()
        if position == goal:
            return path
        r, c = position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
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
    rows = read_int("Enter number of rows: ")
    cols = read_int("Enter number of columns: ")
    if rows < 1 or cols < 1:
        print("Rows and columns must be at least 1.")
        return
    grid = []
    print("Enter grid rows using . for open cells and # for obstacles.")
    for i in range(rows):
        line = input(f"Row {i + 1}: ").strip().replace(" ", "")
        if len(line) != cols or any(ch not in ".#" for ch in line):
            print("Invalid row.")
            return
        grid.append(list(line))
    start = read_point("Start row column (1-based): ")
    goal = read_point("Goal row column (1-based): ")
    if start is None or goal is None:
        print("Invalid start or goal.")
        return
    for point in (start, goal):
        if not (0 <= point[0] < rows and 0 <= point[1] < cols) or grid[point[0]][point[1]] == "#":
            print("Invalid start or goal.")
            return
    path = bfs(grid, start, goal)
    if path:
        print("Shortest path:", " -> ".join(str((r + 1, c + 1)) for r, c in path))
        print("Steps:", len(path) - 1)
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
