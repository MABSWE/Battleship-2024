import random

# Function to create the game board
def print_board(board, show_ships=False):
    print("   0 1 2 3 4")
    for i, row in enumerate(board):
        display_row = [
            "S" if cell == "S" and show_ships else cell
            for cell in row]
        print(f"{i} |{' '.join(display_row)}|")
        print("")

# Function for genereate ships
def generate_ships(board):
    for _ in range(3):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        while board[row][col] == "S"
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        board[row][col] = "S"

# Function for players turn

# Function for guess for the row and col

# Function to see if the guess contains a ship

# Function for computers turn

# Function to display the rules of the game

# Main logic
