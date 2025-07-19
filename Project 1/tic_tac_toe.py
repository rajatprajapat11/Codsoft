import math

# Create a blank board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

# Get available positions
def get_available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

# Check if a player has won
def is_winner(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Check if board is full
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if is_winner("O"):
        return 1
    if is_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score

# Let AI choose the best move
def get_best_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The AI is O.")
    print("Board positions:")
    print(" 0 | 1 | 2 ")
    print(" 3 | 4 | 5 ")
    print(" 6 | 7 | 8 ")

    print_board()

    while True:
        # Human move
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if move in get_available_moves():
                    board[move] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except:
                print("Please enter a number from 0 to 8.")

        print_board()

        if is_winner("X"):
            print("Congratulations! You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = get_best_move()
        board[ai_move] = "O"

        print_board()

        if is_winner("O"):
            print("AI wins! Better luck next time.")
            break
        if is_draw():
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
