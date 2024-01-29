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
        while board[row][col] == "S":
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        board[row][col] = "S"

# Function for players turn


def player_turn(board):
    print("Its Your Turn!")
    try:
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))
        except ValueError:
            print("Wrong Input. Please Enter A Number.")
            return player_turn(board)


# Function for guess for the row and col
if 0 <= guess_row < 5 and 0 <= guess_col < 5:
    if board[guess_row][guess_col] == "S":
        print("You hit the computer's Battleship!")
        board[guess_row][guess_col] = "*"
        return True
        else:
        print("You Missed!")
        board[guess_row][guess_col] = "X"
            return False
else:
    print("Yout missed the ocean. Please try again.")
    return player_turn(board)

# Function for computers turn
print("Computer's Turn!")
comp_guess_row = random.randint(0, 4)
comp_guess_col = random.randint(0, 4)

if board[comp_guess_row][comp_guess_col] == "S":
    print("The computer hit your battleship!")
    board[comp_guess_row][comp_guess_col] = "*"
    return True
else:
    print("The computer missed!")
    return False

# Function to display the rules of the game


def display_rules()


print("\n\nPlay Battleship 2024")
input("Press Enter to start game...")
print("Welcome to Battleship 2024!")
print("\nRules:")
print("1. The game board is a 5x5 grid")
print("2. Your battleships are hidden on your board, marked as S")
print("3. Hits are marked with * and misses with X")
print("4. You take turns guessing the coordinates to hit the computer's battleships")
print("5. The game continues until either you or the computer sink all the battleships")
print("6. You and the computer each have 3 battleships")
print("7. Top left corner is row: 0, col: 0\n")

print("Have fun and good luck!")

# Main logic


def main():


display_rules()
player_name = input("Enter your name: ")
player_score = 0
computer_score = 0
