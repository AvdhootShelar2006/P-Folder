# Breadth-First Search for the 8-Puzzle Problem

from collections import deque


class EightPuzzle:
    def __init__(self, start, goal):
        self.start = tuple(start)
        self.goal = tuple(goal)

    def get_neighbors(self, state):
        neighbors = []
        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
                neighbors.append(tuple(new_state))

        return neighbors

    def solve(self):
        queue = deque([(self.start, [self.start])])
        visited = {self.start}

        while queue:
            state, path = queue.popleft()

            if state == self.goal:
                return path

            for neighbor in self.get_neighbors(state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None


if __name__ == "__main__":
    start = [1, 2, 3,
             4, 0, 6,
             7, 5, 8]

    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    puzzle = EightPuzzle(start, goal)
    solution = puzzle.solve()

    if solution:
        print("Solution found!")
        print("Number of moves:", len(solution) - 1)

        for step, state in enumerate(solution):
            print(f"\nStep {step}:")
            for i in range(0, 9, 3):
                print(state[i:i + 3])
    else:
        print("No solution exists.")