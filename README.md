# Rock Paper Scissors

This is a simple command-line implementation of the classic game "Rock Paper Scissors" written in Python.

## Features

- Allows the user to play multiple rounds against the computer.
- Keeps track of the score and declares the winner at the end of the game.
- User-friendly interface with input validation.

## How to Play

1. Clone the repository:

   ```bash
   git clone https://github.com/BranLeeDev/rock-paper-scissors.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rock-paper-scissors
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to choose rock, paper, or scissors for each round.

5. After each round, you will be prompted to play again. Enter 'y' to continue or 'n' to exit.

## Project Structure

- `main.py`: The entry point of the program. Starts the game loop.
- `modules/`: Directory containing the modular components of the game.
  - `game_logic.py`: Module for the game logic, including functions to determine the winner and generate the computer's choice.
  - `user_interface.py`: Module for user interaction, including functions to get user input and display game results.

## Contributing

Contributions are welcome! If you find any bugs or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
