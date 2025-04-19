import random
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                            QGraphicsOpacityEffect, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QSize, pyqtProperty, QRect
from PyQt5.QtGui import QColor, QPainter, QPen, QBrush, QFont, QFontDatabase, QIcon, QPalette

# Define color scheme constants for consistent theming across the application
DARK_BG = "#1e1e2e"        # Main background color for the application
DARK_ACCENT = "#313244"    # Secondary background color for controls and panels
TEXT_COLOR = "#cdd6f4"     # Primary text color for readability against dark backgrounds
PRIMARY_COLOR = "#89b4fa"  # Accent color for interactive elements and highlights
RED_COLOR = "#f38ba8"      # Error/negative feedback color (wrong guesses, game over)
GREEN_COLOR = "#a6e3a1"    # Success/positive feedback color (correct guesses, win state)
YELLOW_COLOR = "#f9e2af"   # Warning/caution color (medium difficulty)

class AnimatedHangman(QWidget):
    """Widget that renders the hangman figure with smooth animations between stages"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_stage = 0        # Current game stage (0-6, where 6 is game over)
        self.max_stages = 6           # Maximum number of wrong guesses allowed
        self.setMinimumSize(300, 350) # Minimum size to ensure proper drawing of the figure
        self.animation_progress = 0   # Animation interpolation value (0.0 to max_stage+0.9)
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_active = False # Flag to track if animation is currently running
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Configure painter with white stroked lines for the hangman figure
        pen = QPen(QColor(TEXT_COLOR))
        pen.setWidth(4)
        painter.setPen(pen)
        
        # Draw scaffold (base components always visible regardless of game state)
        painter.drawLine(50, 320, 250, 320)  # Base horizontal beam
        painter.drawLine(100, 320, 100, 50)  # Vertical support pole
        painter.drawLine(100, 50, 200, 50)   # Top horizontal beam
        painter.drawLine(200, 50, 200, 80)   # Noose rope
        
        # Draw body parts according to current game stage with smooth animation
        if self.current_stage >= 1 or (self.animation_active and self.animation_progress >= 1):
            # Draw head with circular animation if animating
            progress = min(1, max(0, self.animation_progress - 0)) if self.animation_active else 1
            if progress > 0:
                painter.save()
                painter.setBrush(Qt.NoBrush)
                painter.drawEllipse(185, 80, int(30 * progress), int(30 * progress))
                painter.restore()
        
        if self.current_stage >= 2 or (self.animation_active and self.animation_progress >= 2):
            # Draw body (torso) with vertical line animation
            progress = min(1, max(0, self.animation_progress - 1)) if self.animation_active else 1
            if progress > 0:
                painter.drawLine(200, 110, 200, int(110 + 60 * progress))
        
        if self.current_stage >= 3 or (self.animation_active and self.animation_progress >= 3):
            # Draw left arm extending outward animation
            progress = min(1, max(0, self.animation_progress - 2)) if self.animation_active else 1
            if progress > 0:
                painter.drawLine(200, 130, int(200 - 40 * progress), 150)
        
        if self.current_stage >= 4 or (self.animation_active and self.animation_progress >= 4):
            # Draw right arm extending outward animation
            progress = min(1, max(0, self.animation_progress - 3)) if self.animation_active else 1
            if progress > 0:
                painter.drawLine(200, 130, int(200 + 40 * progress), 150)
        
        if self.current_stage >= 5 or (self.animation_active and self.animation_progress >= 5):
            # Draw left leg extending outward animation
            progress = min(1, max(0, self.animation_progress - 4)) if self.animation_active else 1
            if progress > 0:
                painter.drawLine(200, 170, int(200 - 40 * progress), 220)
        
        if self.current_stage >= 6 or (self.animation_active and self.animation_progress >= 6):
            # Draw right leg extending outward animation
            progress = min(1, max(0, self.animation_progress - 5)) if self.animation_active else 1
            if progress > 0:
                painter.drawLine(200, 170, int(200 + 40 * progress), 220)
                
                # Add X's for eyes and sad mouth when game is lost and animation completes
                if self.current_stage >= 6 and progress >= 0.9:
                    painter.setPen(QPen(QColor(RED_COLOR), 3))
                    # Left eye X
                    painter.drawLine(190, 85, 195, 90)
                    painter.drawLine(195, 85, 190, 90)
                    # Right eye X
                    painter.drawLine(205, 85, 210, 90)
                    painter.drawLine(210, 85, 205, 90)
                    
                    # Draw sad mouth
                    painter.drawArc(190, 95, 20, 10, 0, -180 * 16)
    
    def set_stage(self, stage, animate=True):
        """Sets the hangman drawing stage with optional smooth animation transition"""
        if animate and stage > self.current_stage:
            self.animation_active = True
            self.animation_progress = self.current_stage
            self.animation_timer.start(50)  # 20 FPS animation speed
            
        self.current_stage = stage
        self.update()
        
    def update_animation(self):
        """Updates animation interpolation value for smooth transitions between stages"""
        if self.animation_active:
            self.animation_progress += 0.1  # Increment by 0.1 for smooth animation steps
            if self.animation_progress >= self.current_stage + 0.9:
                # Stop animation when we reach slightly beyond target stage (for smoothness)
                self.animation_active = False
                self.animation_timer.stop()
            self.update()  # Trigger repaint with new animation value
            
    def reset(self):
        """Resets the hangman drawing to initial state"""
        self.current_stage = 0
        self.animation_active = False
        self.animation_progress = 0
        self.update()

class AnimatedPushButton(QPushButton):
    """Custom push button with hover and press animations for a more interactive UI experience"""
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(45)  # Ensure buttons have sufficient touch/click area
        self.setCursor(Qt.PointingHandCursor)  # Change cursor on hover for better UX
        self._color_factor = 0.0  # Animation interpolation value (0.0-1.0)
        
        # Create property animation for smooth color transitions
        self._animation = QPropertyAnimation(self, b"color_factor")
        self._animation.setDuration(100)  # 100ms animation for responsiveness
        self._animation.setStartValue(0.0)
        self._animation.setEndValue(1.0)
        self._animation.setEasingCurve(QEasingCurve.OutCubic)  # Easing for natural feel
        
        # Add drop shadow for depth and visual hierarchy
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 80))  # Semi-transparent shadow
        shadow.setOffset(0, 2)  # Slight vertical offset for natural light direction
        self.setGraphicsEffect(shadow)
        
    def get_color_factor(self):
        """Getter for the color_factor property used in animations"""
        return self._color_factor
        
    def set_color_factor(self, value):
        """Setter for the color_factor property that triggers repaint on change"""
        self._color_factor = value
        self.update()
        
    # PyQt property for animation system to target
    color_factor = pyqtProperty(float, get_color_factor, set_color_factor)
    
    def enterEvent(self, event):
        """Handle mouse enter event by playing forward animation"""
        self._animation.setDirection(QPropertyAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        """Handle mouse leave event by playing backward animation"""
        self._animation.setDirection(QPropertyAnimation.Backward)
        self._animation.start()
        super().leaveEvent(event)
        
    def mousePressEvent(self, event):
        """Handle mouse press with animation for visual feedback"""
        self._animation.setDirection(QPropertyAnimation.Forward)
        self._animation.start()
        super().mousePressEvent(event)
        
    def mouseReleaseEvent(self, event):
        """Handle mouse release with animation for visual feedback"""
        self._animation.setDirection(QPropertyAnimation.Backward)
        self._animation.start()
        super().mouseReleaseEvent(event)

class LetterButton(AnimatedPushButton):
    """Specialized button for alphabet letters with game state visualization (correct/wrong)"""
    def __init__(self, letter, parent=None):
        super().__init__(letter.upper(), parent)
        self.letter = letter  # Store the associated letter
        self.state = "default"  # Track button state: default, correct, or wrong
        self.setFixedSize(65, 65)  # Square button shape for keyboard aesthetic
        
        # Initial styling for unused letters
        self.setStyleSheet(f"""
            background-color: {DARK_ACCENT};
            color: {TEXT_COLOR};
            border: none;
            border-radius: 12px;
            font-size: 24px;
            font-weight: bold;
            margin: 4px;
        """)
    
    def set_state(self, state):
        """Update button appearance based on guess result (correct/wrong/default)"""
        self.state = state
        if state == "correct":
            # Green styling for correct guesses
            self.setStyleSheet(f"""
                background-color: {GREEN_COLOR};
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 24px;
                font-weight: bold;
                margin: 4px;
            """)
        elif state == "wrong":
            # Red styling for incorrect guesses
            self.setStyleSheet(f"""
                background-color: {RED_COLOR};
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 24px;
                font-weight: bold;
                margin: 4px;
            """)
        else:
            # Default styling for unused letters
            self.setStyleSheet(f"""
                background-color: {DARK_ACCENT};
                color: {TEXT_COLOR};
                border: none;
                border-radius: 12px;
                font-size: 24px;
                font-weight: bold;
                margin: 4px;
            """)
        # Only enable interaction for buttons in default state
        self.setEnabled(state == "default")

class WordDisplay(QWidget):
    """Widget that displays the secret word with animated letter reveals as they are guessed correctly"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.word = ""                # The secret word to be guessed
        self.revealed_letters = set() # Set of letters that have been correctly guessed
        self.layout = QHBoxLayout()
        self.layout.setSpacing(15)    # Increased spacing for better readability of word
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)
        self.letter_labels = []       # List to track and manage letter label widgets
        
    def set_word(self, word):
        """Sets a new secret word and resets the display to show all letters as hidden"""
        self.word = word
        self.revealed_letters = set()
        self.update_display()
        
    def reveal_letter(self, letter):
        """Reveals all instances of the guessed letter in the word with visual update
        
        Returns:
            bool: True if letter was found in word, False otherwise
        """
        if letter in self.word:
            self.revealed_letters.add(letter)
            self.update_display()
            return True
        return False
            
    def update_display(self):
        """Rebuilds the visual word display showing revealed and hidden letters with styling"""
        # Clear existing letter labels to rebuild display
        for label in self.letter_labels:
            if label is not None:
                self.layout.removeWidget(label)
                label.deleteLater()
        self.letter_labels.clear()
        
        # Create new letter labels for each character in the word
        for char in self.word:
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            
            if char in self.revealed_letters:
                # Display and style revealed letters - clean modern look without background
                label.setText(char.upper())
                label.setStyleSheet(f"""
                    color: {PRIMARY_COLOR};
                    font-size: 48px;
                    font-weight: bold;
                    min-width: 60px;
                    min-height: 70px;
                    margin: 5px;
                    text-align: center;
                """)
                
                # Add subtle glow effect to emphasize revealed letters
                glow = QGraphicsDropShadowEffect()
                glow.setBlurRadius(12)
                glow.setColor(QColor(PRIMARY_COLOR))
                glow.setOffset(0, 0)
                label.setGraphicsEffect(glow)
            else:
                # Display and style unrevealed letters - shown as underlines
                label.setText("")
                label.setStyleSheet(f"""
                    color: {TEXT_COLOR};
                    font-size: 48px;
                    font-weight: bold;
                    min-width: 60px;
                    min-height: 70px;
                    margin: 5px;
                    border-bottom: 4px solid {TEXT_COLOR}AA;
                """)
            
            self.layout.addWidget(label)
            self.letter_labels.append(label)
        
        # Force immediate update and process events to ensure animations are visible
        self.update()
        QApplication.processEvents()
            
    def is_word_complete(self):
        """Checks if all letters in the word have been revealed
        
        Returns:
            bool: True if the entire word has been revealed, False otherwise
        """
        return all(char in self.revealed_letters for char in self.word)

class HangmanGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Hangman")
        self.setWindowIcon(QIcon("icon.png"))  # Add icon for window title bar
        self.setMinimumSize(1000, 800)  # Set appropriate window size for all elements
        
        # Apply dark theme to entire application
        self.setup_theme()
        
        # Dictionary of word categories with different difficulty levels
        self.categories = {
            'animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
            'fruits': 'apple banana cherry grape grapefruit kiwi lemon lime mango orange papaya peach pear pineapple plum pomegranate raspberry strawberry watermelon'.split(),
            'countries': 'australia brazil canada china egypt france germany india italy japan mexico russia spain thailand turkey ukraine vietnam'.split()
        }

        # Initialize game state variables
        self.secret_word = ""          # Word player needs to guess
        self.guessed_letters = set()   # All letters guessed so far
        self.correct_letters = set()   # Letters correctly guessed
        self.wrong_letters = set()     # Letters incorrectly guessed
        self.guesses_left = 6          # Number of wrong guesses allowed
        self.game_over = False         # Flag to track game completion state
        self.current_category = ""     # Current word category being played
        
        # Set up main application layout structure
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # Add padding around all content
        
        # Create widgets for game screens
        self.welcome_widget = QWidget()  # Category selection screen
        self.game_widget = QWidget()     # Main game play screen
        
        # Initialize both screens
        self.setup_welcome_screen()
        self.setup_game_screen()
        
        # Start by showing the welcome/category selection screen
        self.main_layout.addWidget(self.welcome_widget)
        
    def setup_theme(self):
        """Applies consistent dark theme styling to all application widgets"""
        self.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background-color: {DARK_BG};
                color: {TEXT_COLOR};
            }}
            QPushButton {{
                background-color: {PRIMARY_COLOR};
                color: {DARK_BG};
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {PRIMARY_COLOR}CC;
            }}
            QPushButton:pressed {{
                background-color: {PRIMARY_COLOR}99;
            }}
            QLabel {{
                color: {TEXT_COLOR};
            }}
        """)
        
    def setup_welcome_screen(self):
        """Creates the category selection screen with animated title and difficulty buttons"""
        welcome_layout = QVBoxLayout(self.welcome_widget)
        welcome_layout.setAlignment(Qt.AlignCenter)
        welcome_layout.setSpacing(30)
        welcome_layout.setContentsMargins(50, 50, 50, 50)
        
        # Create large glowing title
        title = QLabel("HANGMAN")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(f"""
            font-size: 72px;
            font-weight: bold;
            color: {PRIMARY_COLOR};
            margin-bottom: 40px;
        """)
        welcome_layout.addWidget(title)
        
        # Add glowing effect to make title stand out
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(15)
        glow.setColor(QColor(PRIMARY_COLOR))
        glow.setOffset(0, 0)
        title.setGraphicsEffect(glow)
        
        # Add subtitle for category selection
        subtitle = QLabel("Select Difficulty")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 24px; margin-bottom: 30px;")
        welcome_layout.addWidget(subtitle)
        
        # Define difficulty options and associated word categories
        difficulties = [
            ("EASY - ANIMALS", 'animals'),     # Easy difficulty with animal words
            ("MEDIUM - FRUITS", 'fruits'),     # Medium difficulty with fruit words
            ("HARD - COUNTRIES", 'countries'), # Hard difficulty with country names
            ("RANDOM - MIX", 'random')         # Random difficulty mixing all categories
        ]
        
        # Create container for difficulty selection buttons
        btn_container = QWidget()
        btn_layout = QVBoxLayout(btn_container)
        btn_layout.setSpacing(15)
        
        # Create button for each difficulty option with distinct styling
        for text, value in difficulties:
            btn = AnimatedPushButton(text)
            btn.setMinimumWidth(300)
            btn.clicked.connect(lambda checked, v=value: self.start_game(v))
            
            # Apply different color for each difficulty level
            if value == 'animals':
                btn.setStyleSheet(f"""
                    background-color: {GREEN_COLOR};
                    color: {DARK_BG};
                    border: none;
                    border-radius: 5px;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: bold;
                """)
            elif value == 'fruits':
                btn.setStyleSheet(f"""
                    background-color: {YELLOW_COLOR};
                    color: {DARK_BG};
                    border: none;
                    border-radius: 5px;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: bold;
                """)
            elif value == 'countries':
                btn.setStyleSheet(f"""
                    background-color: {RED_COLOR};
                    color: {DARK_BG};
                    border: none;
                    border-radius: 5px;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: bold;
                """)
            else:
                btn.setStyleSheet(f"""
                    background-color: {PRIMARY_COLOR};
                    color: {DARK_BG};
                    border: none;
                    border-radius: 5px;
                    padding: 15px;
                    font-size: 18px;
                    font-weight: bold;
                """)
                
            btn_layout.addWidget(btn)
        
        welcome_layout.addWidget(btn_container)
        
    def setup_game_screen(self):
        """Creates the main gameplay screen with hangman drawing, word display, and virtual keyboard"""
        game_layout = QVBoxLayout(self.game_widget)
        game_layout.setContentsMargins(30, 30, 30, 30)
        game_layout.setSpacing(25)  # Ensure good spacing between UI sections
        
        # Create top bar with game title and stats information
        top_bar = QWidget()
        top_bar_layout = QHBoxLayout(top_bar)
        
        # Game title in top-left
        game_title = QLabel("HANGMAN")
        game_title.setStyleSheet(f"font-size: 36px; font-weight: bold; color: {PRIMARY_COLOR};")
        top_bar_layout.addWidget(game_title)
        
        # Game stats in top-right
        stats_widget = QWidget()
        stats_layout = QHBoxLayout(stats_widget)
        stats_layout.setSpacing(30)
        
        # Create labels for displaying game information (category, word length, guesses)
        self.category_label = QLabel()
        self.category_label.setStyleSheet("font-size: 18px;")
        stats_layout.addWidget(self.category_label)
        
        self.word_length_label = QLabel()
        self.word_length_label.setStyleSheet("font-size: 18px;")
        stats_layout.addWidget(self.word_length_label)
        
        self.guesses_left_label = QLabel()
        self.guesses_left_label.setStyleSheet("font-size: 18px;")
        stats_layout.addWidget(self.guesses_left_label)
        
        top_bar_layout.addWidget(stats_widget, alignment=Qt.AlignRight)
        game_layout.addWidget(top_bar)
        
        # Main game area split between hangman drawing and word display
        main_game_area = QWidget()
        main_game_layout = QHBoxLayout(main_game_area)
        main_game_layout.setContentsMargins(15, 15, 15, 15)  # Add padding for visual space
        
        # Left side: Animated hangman visualization 
        self.hangman_drawing = AnimatedHangman()
        main_game_layout.addWidget(self.hangman_drawing, 1)
        
        # Right side: Word display and wrong guesses
        word_area = QWidget()
        word_area_layout = QVBoxLayout(word_area)
        word_area_layout.setAlignment(Qt.AlignCenter)
        word_area_layout.setContentsMargins(20, 20, 20, 20)  # Add padding for visual space
        
        # Display for the word being guessed
        self.word_display = WordDisplay()
        word_area_layout.addWidget(self.word_display)
        
        # Display for tracking wrong guesses
        self.wrong_guesses_label = QLabel("Wrong Guesses:")
        self.wrong_guesses_label.setStyleSheet("font-size: 18px; margin-top: 25px;")
        self.wrong_guesses_label.setAlignment(Qt.AlignCenter)
        word_area_layout.addWidget(self.wrong_guesses_label)
        
        main_game_layout.addWidget(word_area, 2)
        game_layout.addWidget(main_game_area)
        
        # Virtual keyboard for letter selection
        keyboard_widget = QWidget()
        keyboard_layout = QVBoxLayout(keyboard_widget)
        keyboard_layout.setSpacing(18)  # Space between keyboard rows
        
        # Standard QWERTY keyboard layout
        rows = [
            'qwertyuiop',  # Top row
            'asdfghjkl',   # Middle row
            'zxcvbnm'      # Bottom row
        ]
        
        self.letter_buttons = {}  # Dictionary to track letter buttons by character
        
        # Create each row of the keyboard
        for row in rows:
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setSpacing(10)  # Space between keys
            row_layout.setContentsMargins(0, 0, 0, 0)  # No internal padding
            
            # Add extra space at beginning for alignment of shorter rows
            if len(row) < 10:
                row_layout.addStretch(1)
                
            # Create button for each letter in this row
            for letter in row:
                btn = LetterButton(letter)
                btn.clicked.connect(self.create_letter_callback(letter))
                row_layout.addWidget(btn)
                self.letter_buttons[letter] = btn
                
            # Add extra space at end for alignment of shorter rows
            if len(row) < 10:
                row_layout.addStretch(1)
                
            keyboard_layout.addWidget(row_widget)
        
        # Style the keyboard container
        keyboard_widget.setContentsMargins(25, 25, 25, 25)  # Add padding around keyboard
        keyboard_widget.setStyleSheet(f"""
            background-color: {DARK_BG};
            border-radius: 15px;
            border: 1px solid {DARK_ACCENT};
        """)
        
        game_layout.addWidget(keyboard_widget)
        
        # Bottom action buttons (new game, quit)
        button_bar = QWidget()
        button_layout = QHBoxLayout(button_bar)
        button_layout.setSpacing(30)  # Space between buttons
        
        # New game button to return to menu
        new_game_btn = AnimatedPushButton("NEW GAME")
        new_game_btn.setMinimumSize(180, 50)  # Larger size for better touch target
        new_game_btn.setStyleSheet(f"""
            background-color: {PRIMARY_COLOR};
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        """)
        new_game_btn.clicked.connect(self.show_welcome_screen)
        button_layout.addWidget(new_game_btn)
        
        # Quit button to exit the game
        quit_btn = AnimatedPushButton("QUIT")
        quit_btn.setMinimumSize(180, 50)  # Larger size for better touch target
        quit_btn.setStyleSheet(f"""
            background-color: {RED_COLOR};
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        """)
        quit_btn.clicked.connect(self.close)
        button_layout.addWidget(quit_btn)
        
        game_layout.addWidget(button_bar)
        
    def start_game(self, category):
        """Initializes a new game session with the selected word category
        
        Args:
            category (str): The word category to use ('animals', 'fruits', 'countries', or 'random')
        """
        # Select a random word based on chosen category
        if category == 'random':
            all_words = []
            for words in self.categories.values():
                all_words.extend(words)
            self.secret_word = random.choice(all_words)
            self.current_category = "Mix"
        else:
            self.secret_word = random.choice(self.categories[category])
            self.current_category = category.capitalize()
        
        # Reset all game state variables to starting values
        self.guessed_letters = set()
        self.correct_letters = set()
        self.wrong_letters = set()
        self.guesses_left = 6
        self.game_over = False
        
        # Update UI elements with initial game information
        self.category_label.setText(f"Category: {self.current_category}")
        self.word_length_label.setText(f"Word Length: {len(self.secret_word)}")
        self.guesses_left_label.setText(f"Guesses Left: {self.guesses_left}")
        self.wrong_guesses_label.setText("Wrong Guesses:")
        
        # Reset all letter buttons to default state
        for letter, button in self.letter_buttons.items():
            button.set_state("default")
        
        # Reset hangman drawing to empty state
        self.hangman_drawing.reset()
        
        # Initialize word display with the selected secret word
        self.word_display.set_word(self.secret_word)
        
        # Switch from welcome screen to game screen
        self.main_layout.removeWidget(self.welcome_widget)
        self.welcome_widget.hide()
        self.main_layout.addWidget(self.game_widget)
        self.game_widget.show()
        
    def create_letter_callback(self, letter):
        """Creates a callback function for a specific letter button
        
        Args:
            letter (str): The letter associated with the button
            
        Returns:
            function: A callback function that makes a guess with this letter
        """
        return lambda: self.make_guess(letter)
    
    def make_guess(self, letter):
        """Processes a player's letter guess, updating game state and UI accordingly
        
        Args:
            letter (str): The letter that was guessed
        """
        # Ignore guesses if game is over or letter was already guessed
        if self.game_over or letter in self.guessed_letters:
            return
            
        # Mark letter as guessed
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            # Process correct guess
            self.correct_letters.add(letter)
            self.letter_buttons[letter].set_state("correct")
            
            # Update word display to reveal this letter
            self.word_display.reveal_letter(letter)
            
            # Ensure word display is fully updated
            self.word_display.update_display()
            
            # Check if player has won by guessing all letters
            if self.word_display.is_word_complete():
                self.handle_win()
        else:
            # Process incorrect guess
            self.wrong_letters.add(letter)
            self.letter_buttons[letter].set_state("wrong")
            self.guesses_left -= 1
            
            # Update hangman drawing to show next body part
            self.hangman_drawing.set_stage(6 - self.guesses_left)
            
            # Update wrong guesses display with newly guessed letter
            wrong_letters_text = ", ".join(sorted(self.wrong_letters)).upper()
            self.wrong_guesses_label.setText(f"Wrong Guesses: {wrong_letters_text}")
            
            # Update guesses left counter
            self.guesses_left_label.setText(f"Guesses Left: {self.guesses_left}")
            
            # Check if player has lost by using all guesses
            if self.guesses_left <= 0:
                self.handle_loss()
    
    def handle_win(self):
        """Processes the win state when player has correctly guessed all letters"""
        self.game_over = True
        
        # Ensure all letters are visibly revealed in the word display
        for letter in self.secret_word:
            self.word_display.reveal_letter(letter)
        
        # Show win message after a short delay to allow animations to complete
        QTimer.singleShot(1000, lambda: self.show_game_over_message(True))
    
    def handle_loss(self):
        """Processes the loss state when player has used all available guesses"""
        self.game_over = True
        
        # Reveal the full word to show player what they missed
        for letter in self.secret_word:
            self.word_display.reveal_letter(letter)
        
        # Show loss message after a short delay to allow animations to complete
        QTimer.singleShot(1000, lambda: self.show_game_over_message(False))
    
    def show_game_over_message(self, win):
        """Displays a modal overlay with game result and options to play again or quit
        
        Args:
            win (bool): True if player won, False if player lost
        """
        # Create a semi-transparent overlay for the game over message
        message_widget = QWidget(self)
        message_widget.setFixedSize(self.width(), self.height())
        message_widget.move(0, 0)
        message_widget.setStyleSheet("background-color: rgba(20, 20, 30, 0.85);")
        
        # Set up layout for game over content
        message_layout = QVBoxLayout(message_widget)
        message_layout.setAlignment(Qt.AlignCenter)
        message_layout.setSpacing(30)  # Space between elements
        message_layout.setContentsMargins(50, 50, 50, 120)  # Extra bottom space for buttons
        
        # Create result message with appropriate win/loss styling
        result_label = QLabel("YOU WON!" if win else "GAME OVER")
        result_label.setAlignment(Qt.AlignCenter)
        result_label.setStyleSheet(f"""
            font-size: 64px;
            font-weight: bold;
            color: {GREEN_COLOR if win else RED_COLOR};
            padding: 20px;
        """)
        
        # Add glow effect to result text
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(30)
        glow.setColor(QColor(GREEN_COLOR if win else RED_COLOR))
        glow.setOffset(0, 0)
        result_label.setGraphicsEffect(glow)
        
        message_layout.addWidget(result_label)
        
        # Word panel with cleaner styling
        word_panel = QWidget()
        word_panel.setStyleSheet(f"""
            background-color: transparent;
            padding: 20px;
        """)
        word_layout = QVBoxLayout(word_panel)
        
        # "The word was" label
        word_label = QLabel(f"The word was:")
        word_label.setAlignment(Qt.AlignCenter)
        word_label.setStyleSheet("font-size: 24px; color: #cdd6f4; margin-bottom: 10px;")
        word_layout.addWidget(word_label)
        
        # Display the actual secret word
        word_value = QLabel(f"{self.secret_word.upper()}")
        word_value.setAlignment(Qt.AlignCenter)
        word_value.setStyleSheet(f"""
            font-size: 64px;
            font-weight: bold;
            color: {PRIMARY_COLOR};
            letter-spacing: 5px;
        """)
        
        # Add glow effect to word
        word_glow = QGraphicsDropShadowEffect()
        word_glow.setBlurRadius(15)
        word_glow.setColor(QColor(PRIMARY_COLOR))
        word_glow.setOffset(0, 0)
        word_value.setGraphicsEffect(word_glow)
        
        word_layout.addWidget(word_value)
        
        message_layout.addWidget(word_panel)
        
        # Action buttons for play again or quit
        btn_widget = QWidget()
        btn_layout = QHBoxLayout(btn_widget)
        btn_layout.setSpacing(30)
        btn_layout.setContentsMargins(100, 30, 100, 30)  # Add horizontal spacing
        
        # Play again button
        play_again_btn = AnimatedPushButton("PLAY AGAIN")
        play_again_btn.setMinimumSize(200, 60)  # Larger touch target
        play_again_btn.setStyleSheet(f"""
            background-color: {GREEN_COLOR};
            color: #1e1e2e;
            border: none;
            border-radius: 10px;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
        """)
        play_again_btn.clicked.connect(lambda: self.close_message(message_widget))
        btn_layout.addWidget(play_again_btn)
        
        # Quit button
        quit_btn = AnimatedPushButton("QUIT")
        quit_btn.setMinimumSize(200, 60)  # Larger touch target
        quit_btn.setStyleSheet(f"""
            background-color: {RED_COLOR};
            color: #1e1e2e;
            border: none;
            border-radius: 10px;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
        """)
        quit_btn.clicked.connect(self.close)
        btn_layout.addWidget(quit_btn)
        
        message_layout.addWidget(btn_widget)
        
        # Animate the message overlay appearance with fade in
        message_widget.setWindowOpacity(0)
        message_widget.show()
        
        fade_in = QPropertyAnimation(message_widget, b"windowOpacity")
        fade_in.setStartValue(0)
        fade_in.setEndValue(1)
        fade_in.setDuration(500)
        fade_in.start()
    
    def close_message(self, widget):
        """Closes the game over message and returns to welcome screen
        
        Args:
            widget (QWidget): The message overlay widget to close
        """
        widget.deleteLater()
        self.show_welcome_screen()
    
    def show_welcome_screen(self):
        """Returns to the welcome screen to start a new game"""
        self.main_layout.removeWidget(self.game_widget)
        self.game_widget.hide()
        self.main_layout.addWidget(self.welcome_widget)
        self.welcome_widget.show()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Use system fonts instead of trying to load a custom one that might not exist
    app.setFont(QFont("Arial", 10))  # Use a standard system font that's almost always available
    
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())