# Adversarial Search with Alpha Beta Pruning Part A

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


def winner(board):
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def alpha_beta(board, maximizing, alpha, beta):
    result = winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    if " " not in board:
        return 0

    if maximizing:
        value = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                value = max(value, alpha_beta(board, False, alpha, beta))
                board[i] = " "
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return value
    value = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            value = min(value, alpha_beta(board, True, alpha, beta))
            board[i] = " "
            beta = min(beta, value)
            if alpha >= beta:
                break
    return value


def best_move(board):
    move, best_value = None, -float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            value = alpha_beta(board, False, -float("inf"), float("inf"))
            board[i] = " "
            if value > best_value:
                move, best_value = i, value
    return move


def main():
    board = [" "] * 9
    print("You are O. The computer is X.")
    while True:
        move = best_move(board)
        if move is not None:
            board[move] = "X"
            print("\nComputer move:")
            print_board(board)
        if winner(board) or " " not in board:
            break
        while True:
            try:
                user_move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= user_move < 9 and board[user_move] == " ":
                    board[user_move] = "O"
                    break
                print("That position is unavailable.")
            except ValueError:
                print("Enter a number from 1 to 9.")
        print_board(board)
        if winner(board) or " " not in board:
            break
    result = winner(board)
    print("Computer wins." if result == "X" else "You win." if result == "O" else "Draw.")


if __name__ == "__main__":
    main()
