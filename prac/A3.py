# A Star Search 8 Puzzle Part A

import heapq


def heuristic(state, goal):
    return sum(abs(i // 3 - goal.index(value) // 3) + abs(i % 3 - goal.index(value) % 3)
               for i, value in enumerate(state) if value != 0)


def solve(start, goal):
    frontier = [(heuristic(start, goal), 0, start, [])]
    best_cost = {start: 0}
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

    while frontier:
        _, cost, state, path = heapq.heappop(frontier)
        if state == goal:
            return path
        if cost != best_cost[state]:
            continue
        zero = state.index(0)
        r, c = divmod(zero, 3)
        for dr, dc, name in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                new_state = tuple(new_state)
                new_cost = cost + 1
                if new_cost < best_cost.get(new_state, float("inf")):
                    best_cost[new_state] = new_cost
                    heapq.heappush(frontier, (new_cost + heuristic(new_state, goal), new_cost, new_state, path + [name]))
    return None


def solvable(state, goal):
    values = [x for x in state if x != 0]
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    goal_values = [x for x in goal if x != 0]
    goal_inversions = sum(
        goal_values[i] > goal_values[j]
        for i in range(len(goal_values))
        for j in range(i + 1, len(goal_values))
    )
    return inversions % 2 == goal_inversions % 2


def read_state(prompt, default=None):
    text = input(prompt).strip()
    if not text and default is not None:
        return default
    try:
        return tuple(map(int, text.split()))
    except ValueError:
        return None


def main():
    print("Enter the 8-puzzle values row-wise, using 0 for the blank.")
    start = read_state("Start state (9 numbers): ")
    goal = read_state("Goal state (9 numbers, default: 1 2 3 4 5 6 7 8 0): ", (1, 2, 3, 4, 5, 6, 7, 8, 0))
    if start is None or goal is None or len(start) != 9 or len(goal) != 9 or set(start) != set(range(9)) or set(goal) != set(range(9)):
        print("Each state must contain every number from 0 to 8 exactly once.")
        return
    if not solvable(start, goal):
        print("The entered puzzle cannot be solved.")
        return
    path = solve(start, goal)
    if path is None:
        print("No solution found.")
    else:
        print("Moves:", path)
        print("Total moves:", len(path))


if __name__ == "__main__":
    main()
