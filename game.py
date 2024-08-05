import random

def game():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
        while user_choice not in ["rock", "paper", "scissor"]:
            user_choice = input("Invalid input. Please enter rock, paper, or scissor: ").lower()

        possible_choices = ["rock", "paper", "scissor"]
        computer_choice = random.choice(possible_choices)
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissor":
                print("Rock smashes scissor! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissor cuts paper! You lose.")
        elif user_choice == "scissor":
            if computer_choice == "paper":
                print("Scissor cuts paper! You win!")
            else:
                print("Rock smashes scissor! You lose.")

        play_again = input("Play again? (y/n): ").lower()
        while play_again not in ["y", "n"]:
            play_again = input("Invalid input. Please enter y or n: ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    game()