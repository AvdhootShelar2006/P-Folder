# DFS Problem Solving Water Jug Part B

def dfs(capacity_a, capacity_b, target):
    stack = [((0, 0), [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        a, b = state
        path = path + [state]
        if a == target or b == target:
            return path
        amount = min(a, capacity_b - b)
        pour_a_b = (a - amount, b + amount)
        amount = min(b, capacity_a - a)
        pour_b_a = (a + amount, b - amount)
        next_states = [
            (capacity_a, b), (a, capacity_b), (0, b), (a, 0),
            pour_a_b, pour_b_a
        ]
        for next_state in next_states:
            if next_state not in visited:
                stack.append((next_state, path))
    return None


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a whole number.")


def main():
    a = read_int("Enter capacity of jug A: ")
    b = read_int("Enter capacity of jug B: ")
    target = read_int("Enter target amount: ")
    if min(a, b, target) < 0 or target > max(a, b):
        print("Invalid capacities or target.")
        return
    path = dfs(a, b, target)
    if path:
        for step, state in enumerate(path):
            print(f"Step {step}: Jug A = {state[0]}, Jug B = {state[1]}")
    else:
        print("Target cannot be reached.")


if __name__ == "__main__":
    main()
