#!/usr/bin/env python3
import random
import time

def print_intro():
    """Print a nice introduction to the game"""
    print("=" * 60)
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 60)
    print("I'll think of a number, and you try to guess it.")
    print("I'll tell you if your guess is too high or too low.")
    print("=" * 60)

def get_player_name():
    """Get the player's name with validation"""
    while True:
        name = input("What is your name? ")
        if name.strip():  # Check that name isn't empty
            return name
        print("Please enter a valid name.")

def get_difficulty():
    """Let the player choose a difficulty level"""
    print("\nDifficulty levels:")
    print("1. Easy   - Numbers between 1-10, 6 guesses")
    print("2. Medium - Numbers between 1-20, 6 guesses")
    print("3. Hard   - Numbers between 1-50, 6 guesses")
    print("4. Expert - Numbers between 1-100, 5 guesses")
    
    while True:
        try:
            choice = int(input("Choose a difficulty (1-4): "))
            if 1 <= choice <= 4:
                if choice == 1:
                    return 1, 10, 6
                elif choice == 2:
                    return 1, 20, 6
                elif choice == 3:
                    return 1, 50, 6
                else:
                    return 1, 100, 5
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def get_guess(min_val, max_val):
    """Get the player's guess with validation"""
    while True:
        try:
            guess = input("Take a guess: ")
            guess = int(guess)
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    """Main game function"""
    print_intro()
    
    # Get player information
    player_name = get_player_name()
    min_val, max_val, max_guesses = get_difficulty()
    
    # Generate the random number
    secret_number = random.randint(min_val, max_val)
    
    print(f"\nWell, {player_name}, I am thinking of a number between {min_val} and {max_val}.")
    print(f"You have {max_guesses} guesses to find it.")
    
    # For debugging: 
    # print(f"(The secret number is {secret_number})")
    
    # Game loop
    guesses_taken = 0
    
    while guesses_taken < max_guesses:
        guesses_taken += 1
        
        # Get the player's guess
        print(f"\nGuess #{guesses_taken} of {max_guesses}")
        guess = get_guess(min_val, max_val)
        
        # Check the guess
        if guess < secret_number:
            print("Your guess is too LOW.")
        elif guess > secret_number:
            print("Your guess is too HIGH.")
        else:
            # Correct guess!
            break
    
    # Game result
    if guess == secret_number:
        print("\n" + "=" * 60)
        print(f"CONGRATULATIONS, {player_name.upper()}!")
        print(f"You guessed my number ({secret_number}) in {guesses_taken} guesses!")
        
        if guesses_taken == 1:
            print("Amazing! You got it on your first try!")
        elif guesses_taken <= max_guesses // 2:
            print("That's impressive!")
        else:
            print("Good job!")
    else:
        print("\n" + "=" * 60)
        print(f"Sorry, {player_name}. You've used all your guesses.")
        print(f"The number I was thinking of was {secret_number}.")

def play_again():
    """Ask if the player wants to play again"""
    while True:
        answer = input("\nWould you like to play again? (yes/no): ").lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Please answer 'yes' or 'no'.")

def main():
    """Main program function"""
    while True:
        play_game()
        if not play_again():
            break
    
    print("\nThank you for playing the Number Guessing Game!")
    print("Goodbye!")

# Run the game if this script is executed
if __name__ == "__main__":
    main() 