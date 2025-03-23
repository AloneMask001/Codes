count = 0  # Move counter
location = [[0, 0], [0, 1], [1, 0], [2, 1], [2, 2]]  # Predefined locations for the computer to choose from

if __name__ == "__main__":
    print("Welcome to XOX game :)")

winner = None  # Variable to store the winner

# Initialize the 3x3 game board with empty spaces
area = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

while True:  # Main game loop
    answer_sign = "X"  # User's sign
    computer_sign_choice = "O"  # Computer's sign

    # User's turn
    while True:
        i, j = map(int, input(f"Enter your {count + 1}. location move: ").split())  # Get user input
        if area[i][j] == " ":  # Check if the chosen position is empty
            area[i][j] = answer_sign  # Place the user's move
            break  # Exit user input loop

    # Computer's turn
    while True:
        computer_location_choice = random.choice(location)  # Rastgele bir koordinat seç # Randomly select a position from predefined list
        if area[computer_location_choice[0]][computer_location_choice[1]] == " ":  # Check if position is empty
            area[computer_location_choice[0]][computer_location_choice[1]] = computer_sign_choice  # Place move
            break  # Exit computer move loop
    
    print([computer_location_choice[0]], [computer_location_choice[1]], computer_sign_choice)  # Debugging: Print computer's move info
    print()

    # Print the current game board
    for row in area:
        print(row)

    # Check for a winner
    for s in ["X", "O"]:
        # Check rows for a win
        for r in range(3):
            if area[r][0] == s and area[r][1] == s and area[r][2] == s:
                winner = s
                break
        
        # Check columns for a win
        for c in range(3):
            if area[0][c] == s and area[1][c] == s and area[2][c] == s:
                winner = s
                break
        
        # Check diagonals for a win
        if area[0][0] == s and area[1][1] == s and area[2][2] == s:  # Top-left to bottom-right diagonal
            winner = s
            break
        if area[0][2] == s and area[1][1] == s and area[2][0] == s:  # Top-right to bottom-left diagonal
            winner = s
            break
    
    # If a winner is found, display the result and break the loop
    if winner:
        if winner == "X":
            winner = "User"
        else:
            winner = "Computer"
        print(f"Game ended. {winner} won!")
        break  # End the game
