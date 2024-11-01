from random import randint

# Defining a function to get the computer's move
def get_computer_move():
    """
    Retrieves the computer's move by randomly generating a number.

    Returns:
        str: The computer's move, which can be "rock", "paper", or "scissors".
    """
    num = 0  # Declare num variable
    computer_move = ""  # Declare local computer move variable
    
    num = randint(1, 3)
    if num == 1:
        computer_move = "rock"
    elif num == 2:
        computer_move = "paper"
    else:
        computer_move = "scissors"
    
    return computer_move

# Defining a function to check the winner of a round of rock, paper, scissors
def check_winner(player_move, computer_move):
    """
    Determines the winner of the rock, paper, scissors game.

    Args:
        player_move (str): The move the player made.
        computer_move (str): The move the computer made.
    
    Returns:
        str: "Player wins", "Computer wins", or "It's a tie. Play again!"
    """
    game_result = ""  # Declare local game result variable

    if player_move == computer_move:
        game_result = "It's a tie. Play again!"
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        game_result = "Player wins"
    else:
        game_result = "Computer wins"
    
    return game_result

# Defining the main function
def main():
    """
    The main function that controls the game of rock, paper, scissors.
    """
    player_move = ""  # Declare local player move variable
    computer_move = ""  # Declare local computer move variable
    game_result = ""  # Declare local game result variable

    # Game loop to play until there is a winner (no tie)
    while True:
        # Prompt player for a move
        while (player_move := input("Pick one - 'rock', 'paper', or 'scissors': ").lower()) \
              not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

        computer_move = get_computer_move()

        # Display computer's move
        print(f"Computer chose: {computer_move}")

        # Check the winner and display the result
        game_result = check_winner(player_move, computer_move)
        print(game_result)

        # Break if it's not a tie
        if game_result != "It's a tie. Play again!":
            break

# Calling the main function
if __name__ == "__main__":
    main()