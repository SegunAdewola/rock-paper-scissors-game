# Rock, Paper, Scissors Game

## Description
This Python program lets the user play a game of Rock, Paper, Scissors against the computer. The computer's move is randomly selected, and the winner is determined based on standard rules. The game continues until either the player or the computer wins (in case of a tie, the game is replayed).

## Features
- **Computer Move Generation**: The computer randomly selects "rock", "paper", or "scissors".
- **Player Input Validation**: Ensures the user enters a valid move.
- **Winner Determination**: The program compares moves and declares a winner or prompts a rematch in case of a tie.

## Usage

1. Clone or download the script.
2. Run the script from the terminal or command line:

   ```bash
   python rock_paper_scissors.py
   ```
3. Follow the prompt to play the game.

### Example
```plaintext
Pick one - 'rock', 'paper', or 'scissors': rock
Computer chose: scissors
Player wins
```

## Functions

- **`get_computer_move()`**: Randomly generates the computer's move.
    - **Returns**: "rock", "paper", or "scissors"
- **`check_winner(player_move, computer_move)`**: Determines the winner based on the player's and computer's moves.
    - **Arguments**: 
        - **`player_move (str)`**: The player's move
        - **`computer_move (str)`**: The computer's move
    - **Returns**: "Player wins", "Computer wins", or "It's a tie. Play again!"

- **`main()`**: Manages game flow, prompting the player for input and handling game logic.

## Requirements
- **Python 3.x**

## License
This project is licensed under the MIT License.