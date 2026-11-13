# Model-Based Agent for Grid Navigation with Obstacles
# The agent builds an internal model of obstacles from its local sensing, then plans a path to the goal using that model.

from collections import deque


class ModelBasedAgent:
    def __init__(self, rows, cols, start, goal):
        self.rows = rows
        self.cols = cols
        self.position = start
        self.goal = goal
        self.known_obstacles = set()

    def perceive(self, environment):
        r, c = self.position
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if environment[nr][nc] == "#":
                    self.known_obstacles.add((nr, nc))
                else:
                    self.known_obstacles.discard((nr, nc))

    def plan_path(self):
        queue = deque([(self.position, [self.position])])
        seen = {self.position}
        while queue:
            (r, c), path = queue.popleft()
            if (r, c) == self.goal:
                return path
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nxt = (r + dr, c + dc)
                nr, nc = nxt
                if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                    continue
                if nxt in seen or nxt in self.known_obstacles:
                    continue
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
        return None

    def run(self, environment, max_steps=100):
        path_taken = [self.position]
        self.perceive(environment)
        steps = 0
        while self.position != self.goal and steps < max_steps:
            path = self.plan_path()
            if path is None or len(path) < 2:
                break
            self.position = path[1]
            path_taken.append(self.position)
            self.perceive(environment)
            steps += 1
        return path_taken, self.position == self.goal


if __name__ == "__main__":
    grid = [
        "....#...",
        ".##.#.#.",
        "....#.#.",
        "##.....#",
        "...##...",
        ".#....#.",
    ]
    grid = [list(row) for row in grid]
    start, goal = (0, 0), (5, 7)
    agent = ModelBasedAgent(len(grid), len(grid[0]), start, goal)
    path, reached = agent.run(grid)
    display = [row[:] for row in grid]
    for r, c in path[1:-1]:
        display[r][c] = "*"
    display[start[0]][start[1]] = "S"
    display[goal[0]][goal[1]] = "G"
    for row in display:
        print("".join(row))
    print(f"\nGoal reached: {reached}")
    print(f"Steps taken: {len(path) - 1}")
    print(f"Known obstacles: {len(agent.known_obstacles)}")