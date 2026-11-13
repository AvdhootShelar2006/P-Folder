# Game-Playing Agent Using Minimax

class MinimaxAgent:
    def __init__(self):
        self.board = [' '] * 9
        self.human = 'O'
        self.ai = 'X'

    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("--+---+--")

    def check_winner(self, player):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(all(self.board[i] == player for i in line) for line in wins)

    def minimax(self, is_maximizing):
        if self.check_winner(self.ai):
            return 1
        if self.check_winner(self.human):
            return -1
        if ' ' not in self.board:
            return 0

        if is_maximizing:
            best = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.ai
                    best = max(best, self.minimax(False))
                    self.board[i] = ' '
            return best

        else:
            best = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.human
                    best = min(best, self.minimax(True))
                    self.board[i] = ' '
            return best

    def ai_move(self):
        best_score = float('-inf')
        best_move = None

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.ai
                score = self.minimax(False)
                self.board[i] = ' '

                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.board[best_move] = self.ai

    def play(self):
        print("Tic-Tac-Toe: You are O, AI is X")

        while True:
            self.display_board()

            try:
                move = int(input("Enter position (1-9): ")) - 1
                if move < 0 or move >= 9 or self.board[move] != ' ':
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Enter a valid number.")
                continue

            self.board[move] = self.human

            if self.check_winner(self.human):
                self.display_board()
                print("You win!")
                break

            if ' ' not in self.board:
                self.display_board()
                print("It's a draw!")
                break

            self.ai_move()

            if self.check_winner(self.ai):
                self.display_board()
                print("AI wins!")
                break

            if ' ' not in self.board:
                self.display_board()
                print("It's a draw!")
                break


if __name__ == "__main__":
    agent = MinimaxAgent()
    agent.play()