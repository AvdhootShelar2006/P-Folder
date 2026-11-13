# Simple Reflex Agent for Vacuum Cleaner World

def reflex_vacuum_agent(percept):
    location, status = percept
    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Right"
    return "Left"


def run_simulation(environment, start_location, steps=10):
    location = start_location
    total_score = 0
    history = []
    for step in range(1, steps + 1):
        status = environment[location]
        action = reflex_vacuum_agent((location, status))
        history.append((step, location, status, action))
        if action == "Suck":
            environment[location] = "Clean"
            total_score += 10
        elif action == "Right":
            location = "B"
            total_score -= 1
        else:
            location = "A"
            total_score -= 1
    return history, total_score, environment


if __name__ == "__main__":
    environment = {"A": "Dirty", "B": "Dirty"}
    history, score, final_env = run_simulation(environment, "A", steps=6)
    print(f"{'Step':<6}{'Location':<10}{'Status':<10}{'Action':<8}")
    for step, location, status, action in history:
        print(f"{step:<6}{location:<10}{status:<10}{action:<8}")
    print(f"\nFinal environment: {final_env}")
    print(f"Performance score: {score}")