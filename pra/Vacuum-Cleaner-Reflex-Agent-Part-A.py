# Vacuum Cleaner Reflex Agent Part A

class VacuumAgent:
    def __init__(self, rooms):
        self.rooms = rooms
        self.position = 0

    def act(self):
        if self.rooms[self.position] == "dirty":
            self.rooms[self.position] = "clean"
            return "Suck"
        if self.position < len(self.rooms) - 1:
            self.position += 1
            return "Move Right"
        if self.position > 0:
            self.position -= 1
            return "Move Left"
        return "No Operation"

    def run(self):
        steps = 0
        while "dirty" in self.rooms:
            action = self.act()
            steps += 1
            print(f"Step {steps}: {action} | Position: {self.position + 1} | Rooms: {self.rooms}")
        print(f"All rooms are clean in {steps} actions.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a whole number.")


def main():
    count = read_int("Enter number of rooms: ")
    if count < 1:
        print("Enter at least 1 room.")
        return
    rooms = []
    for i in range(count):
        status = input(f"Room {i + 1} status (clean/dirty): ").strip().lower()
        while status not in ("clean", "dirty"):
            status = input("Enter clean or dirty: ").strip().lower()
        rooms.append(status)
    start = read_int(f"Enter starting room (1-{count}): ")
    while not 1 <= start <= count:
        start = read_int(f"Enter a room from 1 to {count}: ")
    agent = VacuumAgent(rooms)
    agent.position = start - 1
    agent.run()


if __name__ == "__main__":
    main()
