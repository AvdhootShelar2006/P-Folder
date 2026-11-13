# Number Guessing Intelligent Agent Using Higher Lower Feedback Part B

class NumberGuessingAgent:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def play(self):
        print(f"Think of a number between {self.low} and {self.high}.")
        print("Respond with h if your number is higher, l if lower, and c if correct.")
        while self.low <= self.high:
            guess = (self.low + self.high) // 2
            feedback = input(f"Is your number {guess}? (h/l/c): ").strip().lower()
            if feedback == "c":
                print("I guessed your number!")
                return
            if feedback == "h":
                self.low = guess + 1
            elif feedback == "l":
                self.high = guess - 1
            else:
                print("Please enter h, l, or c.")
        print("Your feedback was inconsistent. No possible number remains.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a whole number.")


def main():
    low = read_int("Enter minimum number: ")
    high = read_int("Enter maximum number: ")
    if low > high:
        print("Minimum must not exceed maximum.")
        return
    NumberGuessingAgent(low, high).play()


if __name__ == "__main__":
    main()
