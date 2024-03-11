from modules.game_logic import get_computer_choice, determine_winner

def get_user_choice():
    while True:
        try:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Exiting...")
            exit()

def display_result(winner):
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        if user_score == rounds_to_win or computer_score == rounds_to_win:
            break

    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Sorry, the computer wins the game!")
    else:
        print("The game ends in a tie!")

def play_again():
    return input("Do you want to play again? (y/n): ").lower() == 'y'
