# Local Beam Search for the Traveling Salesman Problem

import random


class LocalBeamSearch:
    def __init__(self, cities, distances, beam_width=3):
        self.cities = cities
        self.distances = distances
        self.beam_width = beam_width

    def calculate_cost(self, path):
        cost = 0
        for i in range(len(path)):
            cost += self.distances[path[i]][path[(i + 1) % len(path)]]
        return cost

    def generate_neighbors(self, path):
        neighbors = []

        for i in range(1, len(path) - 1):
            for j in range(i + 1, len(path)):
                new_path = path[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                neighbors.append(new_path)

        return neighbors

    def run(self):
        beam = []

        for _ in range(self.beam_width):
            path = self.cities[:]
            random.shuffle(path)
            beam.append(path)

        best_path = None
        best_cost = float('inf')

        for _ in range(100):
            neighbors = []

            for path in beam:
                neighbors.extend(self.generate_neighbors(path))

            if not neighbors:
                break

            neighbors.sort(key=self.calculate_cost)
            beam = neighbors[:self.beam_width]

            cost = self.calculate_cost(beam[0])

            if cost < best_cost:
                best_cost = cost
                best_path = beam[0][:]

        return best_path, best_cost


if __name__ == "__main__":
    cities = ['A', 'B', 'C', 'D']

    distances = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }

    agent = LocalBeamSearch(cities, distances)
    path, cost = agent.run()

    print("Best path:", " -> ".join(path + [path[0]]))
    print("Minimum distance:", cost)