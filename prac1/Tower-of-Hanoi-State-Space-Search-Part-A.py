# Tower of Hanoi by State Space Search Part A

from collections import deque


def solve(disks):
    start = tuple([0] * disks)
    goal = tuple([2] * disks)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        tops = {}
        for disk, peg in enumerate(state):
            tops.setdefault(peg, disk)
        for source in range(3):
            if source not in tops:
                continue
            disk = tops[source]
            for target in range(3):
                if target == source:
                    continue
                if target not in tops or tops[target] > disk:
                    new_state = list(state)
                    new_state[disk] = target
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [(disk + 1, source + 1, target + 1)]))
    return None


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a whole number.")


def main():
    disks = read_int("Enter number of disks (1-8): ")
    if not 1 <= disks <= 8:
        print("Enter a number from 1 to 8.")
        return
    path = solve(disks)
    print(f"Minimum moves: {len(path)}")
    for step, (disk, source, target) in enumerate(path, 1):
        print(f"Move {step}: Disk {disk} from peg {source} to peg {target}")


if __name__ == "__main__":
    main()
