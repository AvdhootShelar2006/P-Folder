# Goal Stack Planning for Blocks World Part B

def valid_configuration(configuration):
    blocks = set(configuration)
    supports = [support for support in configuration.values() if support != "table"]
    if len(supports) != len(set(supports)):
        return False
    for block, support in configuration.items():
        if support != "table" and (support not in blocks or support == block):
            return False
    for block in blocks:
        seen = set()
        current = block
        while current != "table":
            if current in seen:
                return False
            seen.add(current)
            current = configuration[current]
    return True


def goal_stack_plan(initial, goal):
    state = dict(initial)
    actions = []

    def move(block, destination):
        old = state[block]
        state[block] = destination
        actions.append((block, old, destination))

    def clear(block):
        for top in [x for x in state if state[x] == block]:
            clear(top)
            move(top, "table")

    def place(block, destination):
        if state[block] == destination:
            return
        clear(block)
        if destination != "table":
            clear(destination)
        move(block, destination)

    for _ in range(len(state) * len(state) + len(state)):
        pending = [b for b in goal if state[b] != goal[b]]
        if not pending:
            return actions, state
        ready = [b for b in pending if goal[b] == "table" or state[goal[b]] == goal[goal[b]]]
        if not ready:
            return None
        place(ready[0], goal[ready[0]])
    return None


def read_configuration(label, blocks):
    configuration = {}
    print(f"Enter support for each block in {label}. Use table or another block.")
    for block in blocks:
        configuration[block] = input(f"What is {block} on? ").strip()
    return configuration


def main():
    blocks = input("Enter block names separated by spaces (e.g. A B C): ").split()
    if not blocks or len(set(blocks)) != len(blocks):
        print("Enter unique block names.")
        return
    initial = read_configuration("initial state", blocks)
    goal = read_configuration("goal state", blocks)
    if not valid_configuration(initial) or not valid_configuration(goal):
        print("Invalid configuration. Check supports and avoid cycles.")
        return
    result = goal_stack_plan(initial, goal)
    if result is None:
        print("This planner could not construct a valid plan.")
    else:
        actions, final_state = result
        print("Plan:")
        for i, (block, old, new) in enumerate(actions, 1):
            print(f"{i}. Move {block} from {old} to {new}")
        print("Final state:", final_state)


if __name__ == "__main__":
    main()
