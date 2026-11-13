# Depth-First Search for the Water Jug Problem

class WaterJug:
    def __init__(self, jug1, jug2, target):
        self.jug1 = jug1
        self.jug2 = jug2
        self.target = target
        self.visited = set()
        self.path = []

    def dfs(self, x, y):
        if (x, y) in self.visited:
            return False

        self.visited.add((x, y))
        self.path.append((x, y))

        if x == self.target or y == self.target:
            return True

        states = [
            (self.jug1, y),
            (x, self.jug2),
            (0, y),
            (x, 0),
            (x - min(x, self.jug2 - y), y + min(x, self.jug2 - y)),
            (x + min(y, self.jug1 - x), y - min(y, self.jug1 - x))
        ]

        for nx, ny in states:
            if self.dfs(nx, ny):
                return True

        self.path.pop()
        return False

    def solve(self):
        if self.dfs(0, 0):
            return self.path
        return None


if __name__ == "__main__":
    agent = WaterJug(4, 3, 2)
    solution = agent.solve()

    if solution:
        print("Solution found!")
        for step, state in enumerate(solution):
            print(f"Step {step}: Jug 1 = {state[0]}L, Jug 2 = {state[1]}L")
    else:
        print("No solution exists.")