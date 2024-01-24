Import random

# Function to create the game board

def print_board(board, show_ships=False):
    print("01234")
    for i, row in enumerate(board):
        display_row = ["S" if cell == "S" and show_ships else cell for cell in row]
        print(f"{i} |{' '.join(display_row)}|")
        print("")
        
# Function for genereate ships
def generate_ships(board):

# Function for players turn

# Function for guess for the row and col

# Function to see if the guess contains a ship

# Function for computers turn

# Function to display the rules of the game

# Main logic
