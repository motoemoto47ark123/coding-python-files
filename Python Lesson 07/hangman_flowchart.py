import random

def display_hangman(wrong_guesses):
    """Display the hangman ASCII art based on number of wrong guesses"""
    stages = [
        """
        +----+
        |    |
        |
        |
        |
        |
        ===
        """,
        """
        +----+
        |    |
        |    O
        |
        |
        |
        ===
        """,
        """
        +----+
        |    |
        |    O
        |    |
        |
        |
        ===
        """,
        """
        +----+
        |    |
        |    O
        |   /|
        |
        |
        ===
        """,
        """
        +----+
        |    |
        |    O
        |   /|\\
        |
        |
        ===
        """,
        """
        +----+
        |    |
        |    O
        |   /|\\
        |   /
        |
        ===
        """,
        """
        +----+
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        ===
        """
    ]
    return stages[wrong_guesses]

def display_word(word, guessed_letters):
    """Show the word with blanks for unguessed letters"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    # List of words to choose from
    words = ['cat', 'dog', 'python', 'computer', 'hangman', 'programming', 'code']
    
    play_again = 'yes'
    
    while play_again.lower() == 'yes':
        # START - Come up with a secret word
        secret_word = random.choice(words)
        guessed_letters = []
        wrong_guesses = 0
        max_wrong_guesses = 6  # Maximum wrong guesses before losing
        
        print("H A N G M A N")
        print(display_hangman(wrong_guesses))
        
        # Game loop
        while wrong_guesses < max_wrong_guesses:
            # Show drawing and blanks to player
            print(display_word(secret_word, guessed_letters))
            print("Missed letters:", " ".join(sorted([l for l in guessed_letters if l not in secret_word])))
            
            # Ask player to guess a letter
            guess = input("Guess a letter: ").lower()
            
            # Check if letter was already guessed
            if guess in guessed_letters:
                print("You have already guessed that letter. Choose again.")
                continue
            
            # Add the guess to guessed letters
            guessed_letters.append(guess)
            
            # Check if letter is in the secret word
            if guess in secret_word:
                # Check if player guessed all letters and wins
                all_letters_guessed = all(letter in guessed_letters for letter in secret_word)
                if all_letters_guessed:
                    print(display_word(secret_word, guessed_letters))
                    print(f"Yes! The secret word is \"{secret_word}\"!")
                    print("You have won!")
                    break
            else:
                # Letter is not in the secret word
                wrong_guesses += 1
                print(display_hangman(wrong_guesses))
                
                # Check if player ran out of guesses and loses
                if wrong_guesses >= max_wrong_guesses:
                    print(display_word(secret_word, guessed_letters))
                    print(f"Sorry! The secret word was \"{secret_word}\".")
                    print("You have lost!")
                    break
        
        # Ask player to play again
        play_again = input("Do you want to play again? (yes or no): ")
    
    # END
    print("Thanks for playing!")

if __name__ == "__main__":
    main() 