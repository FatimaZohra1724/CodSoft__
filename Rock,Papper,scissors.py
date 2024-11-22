import random

print("Welcome to the Rock, Paper, Scissor Game...! Try Your Luck.")

while True:
    # User Input
    user_choice = int(input("Choose Rock, Paper, Scissor. Type 0 for Rock, 1 for Paper, 2 for Scissor: "))
    
    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice! Please choose 0 for Rock, 1 for Paper, or 2 for Scissor.")
        continue

    # Computer's Random Choice
    comp_choice = random.randint(0, 2)
    print(f"Your choice: {user_choice}, Computer's choice: {comp_choice}")

    # Game Logic
    if user_choice == comp_choice:
        print("It's a draw!")
    elif comp_choice == 0 and user_choice == 2:
        print("Computer wins!")
    elif comp_choice == 2 and user_choice == 0:
        print("You win!")
    elif comp_choice == 1 and user_choice == 0:
        print("Computer wins!")
    elif comp_choice == 0 and user_choice == 1:
        print("You win!")
    elif comp_choice == 1 and user_choice == 2:
        print("You win!")
    elif comp_choice == 2 and user_choice == 1:
        print("Computer wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
