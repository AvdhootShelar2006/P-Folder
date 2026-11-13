# Game Playing Agent Using Minimax Part B

def minimax(stones, maximizing, memo):
    if stones == 0:
        return -1 if maximizing else 1
    key = (stones, maximizing)
    if key in memo:
        return memo[key]
    choices = []
    for take in (1, 2, 3):
        if stones >= take:
            choices.append(minimax(stones - take, not maximizing, memo))
    result = max(choices) if maximizing else min(choices)
    memo[key] = result
    return result


def best_move(stones):
    memo = {}
    options = []
    for take in (1, 2, 3):
        if stones >= take:
            options.append((minimax(stones - take, False, memo), take))
    return max(options)[1]


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid integer.")


def main():
    stones = read_int("Enter starting number of stones: ")
    if stones < 1:
        print("Enter a positive number.")
        return
    print("Take turns removing 1, 2, or 3 stones. The player taking the last stone wins.")
    turn = input("Who starts? (user/computer): ").strip().lower()
    while turn not in ("user", "computer"):
        turn = input("Please type 'user' or 'computer': ").strip().lower()
    while stones > 0:
        if turn == "computer":
            take = best_move(stones)
            print(f"Computer takes {take} stone(s).")
        else:
            while True:
                take = read_int("Your move (1, 2, or 3): ")
                if 1 <= take <= min(3, stones):
                    break
                print("Invalid number of stones.")
        stones -= take
        print("Stones remaining:", stones)
        if stones == 0:
            print("Computer wins!" if turn == "computer" else "You win!")
            break
        turn = "user" if turn == "computer" else "computer"


if __name__ == "__main__":
    main()
