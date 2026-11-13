# Adversarial Search with Alpha-Beta Pruning

class AlphaBeta:
    def __init__(self):
        self.nodes_visited = 0
        self.nodes_pruned = 0

    def minimax(self, depth, node, maximizing, alpha, beta):
        self.nodes_visited += 1

        if depth == 0 or node not in self.tree:
            return self.values[node]

        if maximizing:
            best = float('-inf')

            for child in self.tree[node]:
                value = self.minimax(depth - 1, child, False, alpha, beta)
                best = max(best, value)
                alpha = max(alpha, best)

                if beta <= alpha:
                    self.nodes_pruned += 1
                    break

            return best

        else:
            best = float('inf')

            for child in self.tree[node]:
                value = self.minimax(depth - 1, child, True, alpha, beta)
                best = min(best, value)
                beta = min(beta, best)

                if beta <= alpha:
                    self.nodes_pruned += 1
                    break

            return best

    def run(self):
        result = self.minimax(3, 'A', True, float('-inf'), float('inf'))
        print("Optimal value:", result)
        print("Nodes visited:", self.nodes_visited)
        print("Pruned nodes:", self.nodes_pruned)


if __name__ == "__main__":
    agent = AlphaBeta()

    agent.tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G']
    }

    agent.values = {
        'D': 3,
        'E': 5,
        'F': 2,
        'G': 9
    }

    agent.run()