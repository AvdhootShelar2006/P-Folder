# Local Beam Search for Traveling Salesman Problem Part A

import random


def tour_length(route, distances):
    return sum(distances[route[i]][route[(i + 1) % len(route)]] for i in range(len(route)))


def local_beam_search(distances, beam_width, iterations):
    n = len(distances)
    beam = []
    for _ in range(beam_width):
        route = list(range(n))
        random.shuffle(route)
        beam.append(route)
    beam = sorted(beam, key=lambda route: tour_length(route, distances))

    for _ in range(iterations):
        candidates = {}
        for route in beam:
            for i in range(1, n):
                for j in range(i + 1, n):
                    neighbor = route[:]
                    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                    candidates[tuple(neighbor)] = neighbor
        if not candidates:
            break
        beam = sorted(candidates.values(), key=lambda route: tour_length(route, distances))[:beam_width]
    return min(beam, key=lambda route: tour_length(route, distances))


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a whole number.")


def read_distances(prompt, n):
    try:
        row = list(map(float, input(prompt).split()))
    except ValueError:
        return None
    if len(row) == n and all(x >= 0 for x in row):
        return row
    return None


def main():
    n = read_int("Enter number of cities: ")
    if n < 2:
        print("Enter at least 2 cities.")
        return
    names = [input(f"Enter name of city {i + 1}: ").strip() or f"City{i + 1}" for i in range(n)]
    distances = []
    print("Enter the distance matrix row by row.")
    for i in range(n):
        row = read_distances(f"Distances from {names[i]}: ", n)
        if row is None:
            print("Each row must contain", n, "non-negative numbers.")
            return
        distances.append(row)
    width = read_int("Enter beam width: ")
    iterations = read_int("Enter number of iterations: ")
    if width < 1 or iterations < 1:
        print("Beam width and iterations must be positive.")
        return
    route = local_beam_search(distances, width, iterations)
    print("Best route:", " -> ".join(names[i] for i in route + [route[0]]))
    print("Total distance:", tour_length(route, distances))


if __name__ == "__main__":
    main()
