import random
import time
import os

def clear_screen():
    """Clear the console screen for better readability."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

def type_text(text, delay=0.03):
    """Print text with a typewriter effect for better immersion."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_intro():
    """Display the game introduction with improved storytelling."""
    clear_screen()
    print("\n" + "=" * 60)
    print("\033[1m" + " " * 20 + "DRAGON REALM" + " " * 20 + "\033[0m")
    print("=" * 60 + "\n")
    
    type_text('''You find yourself standing at the edge of a vast mountain range.
Ancient legends speak of dragons that guard immense treasures in these caves.
Some dragons are friendly guardians who reward the brave, while others are 
fierce beasts who devour any who disturb their slumber.''')
    time.sleep(1)
    
    type_text('''\nAfter days of searching, you've found a hidden valley with three caves.
Each cave might hold unimaginable riches... or unspeakable danger.''')
    print()

def choose_cave(num_caves=3):
    """Let player choose a cave with input validation.
    
    Args:
        num_caves: Number of caves to choose from (default: 3)
        
    Returns:
        The chosen cave as a string.
    """
    valid_choices = [str(i) for i in range(1, num_caves+1)]
    cave_descriptions = [
        "A cave with ancient runes carved around its entrance.",
        "A cave with smoke gently rising from its depths.",
        "A cave with strange glowing crystals surrounding it."
    ]
    
    print("\nThe caves before you:")
    for i, desc in enumerate(cave_descriptions[:num_caves], 1):
        print(f"  Cave {i}: {desc}")
    
    cave = ''
    while cave not in valid_choices:
        print(f"\nWhich cave will you enter? (1-{num_caves})")
        cave = input("> ")
        if cave not in valid_choices:
            type_text("Please enter a valid cave number.", 0.02)
    
    return cave

def build_suspense(cave_num):
    """Create dramatic tension as player enters the cave."""
    clear_screen()
    type_text(f"\nYou approach cave {cave_num}...", 0.05)
    time.sleep(1)
    
    type_text("\nThe darkness envelops you as you step inside...", 0.05)
    time.sleep(1.5)
    
    type_text("\nThe air is damp and cold, ancient stalactites hang from above...", 0.05)
    time.sleep(1.5)
    
    type_text("\nYou hear a deep rumbling sound...", 0.05)
    time.sleep(1)
    
    type_text("\nSuddenly, torches along the walls ignite by themselves!", 0.05)
    time.sleep(1.5)
    
    type_text("\nA massive dragon appears before you, its scales reflecting the firelight!", 0.05)
    time.sleep(2)
    
    print("\n" + "-" * 60)
    type_text("The dragon regards you with ancient eyes and then...", 0.05)
    time.sleep(2)

def check_cave(chosen_cave, difficulty="normal"):
    """Determine and display the player's fate.
    
    Args:
        chosen_cave: The cave number player selected
        difficulty: Game difficulty affecting chance of success
        
    Returns:
        True if player found treasure, False if eaten
    """
    build_suspense(chosen_cave)
    
    # Adjust friendly cave chance based on difficulty
    if difficulty == "easy":
        friendly_chance = 0.6
    elif difficulty == "hard":
        friendly_chance = 0.3
    else:  # normal
        friendly_chance = 0.4
    
    # Determine if dragon is friendly
    if random.random() < friendly_chance:
        type_text('''\n\033[32mThe dragon bows its head and steps aside, revealing an ancient treasure hoard!
Gold coins, gemstones, and magical artifacts beyond your wildest dreams.\033[0m''', 0.03)
        
        treasures = [
            "a crown of pure starlight",
            "the sword of ancient heroes",
            "a chest of rare gemstones",
            "an orb of mystical power",
            "a pouch of endless gold coins"
        ]
        special_treasure = random.choice(treasures)
        
        type_text(f"\nAmong the treasures, you discover {special_treasure}!", 0.03)
        return True
    else:
        type_text('''\n\033[31mThe dragon's eyes narrow as it lets out a terrifying roar!
With lightning speed, it lunges forward and consumes you in a single bite.\033[0m''', 0.03)
        
        type_text("\nYour adventure comes to an unfortunate end...", 0.05)
        return False

def display_score(score):
    """Display the player's current score."""
    print("\n" + "-" * 60)
    print(f"Your current treasure count: {score}")
    print("-" * 60)

def main():
    """Main game loop with enhanced features."""
    score = 0
    survived = 0
    attempts = 0
    
    # Set initial difficulty
    difficulty = "normal"
    
    display_intro()
    
    play_again = 'yes'
    while play_again.lower() in ['yes', 'y']:
        if attempts > 0:
            display_score(score)
            
            # Offer difficulty change every few attempts
            if attempts % 3 == 0:
                print("\nSelect difficulty for next round:")
                print("  1: Easy   (better chance of finding treasure)")
                print("  2: Normal (balanced gameplay)")
                print("  3: Hard   (greater risk, but we believe in you!)")
                
                choice = ''
                while choice not in ['1', '2', '3']:
                    choice = input("> ")
                
                if choice == '1':
                    difficulty = "easy"
                    type_text("\nThe dragons seem sleepy today. Good for you!")
                elif choice == '2':
                    difficulty = "normal"
                    type_text("\nA standard adventure awaits!")
                else:
                    difficulty = "hard"
                    type_text("\nThe dragons are particularly alert today. Be careful!")
            
            # Clear screen and remind player of the setting
            time.sleep(1)
            clear_screen()
            type_text("You return to the valley, determined to try again...")
        
        # Choose cave
        cave_number = choose_cave(3)  # Now with 3 caves
        
        # Determine outcome
        result = check_cave(cave_number, difficulty)
        attempts += 1
        
        if result:
            score += 1
            survived += 1
            type_text(f"\nYou've successfully claimed treasure {survived} time(s)!")
        
        # Calculate and display survival rate
        if attempts > 0:
            survival_rate = (survived / attempts) * 100
            type_text(f"\nYour survival rate: {survival_rate:.1f}%")
        
        # Ask to play again
        print("\n" + "-" * 60)
        print("Do you want to brave the dragon caves again? (yes or no)")
        play_again = input("> ")
    
    # Game over sequence
    clear_screen()
    print("\n" + "=" * 60)
    print(" " * 22 + "GAME OVER" + " " * 22)
    print("=" * 60)
    
    type_text(f"\nYou faced the dragons {attempts} times and collected {score} treasures.")
    
    if score == 0:
        type_text("\nBetter luck next time, brave adventurer!")
    elif score < 3:
        type_text("\nA respectable effort! The bards will sing of your deeds.")
    else:
        type_text("\nA legendary performance! Your name will be remembered for ages to come!")
    
    print("\nThanks for playing DRAGON REALM!")

# Start the game if this script is run directly
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Sorry about that! Please try again.") 