import random

# Open hangman.txt and set the word for the game
with open('hangman.txt', 'r') as file:
    lines = file.readlines()
    gameword = random.choice(lines).strip() #.strip() to remove \n from string

# Preliminary game setup

# Set up blank character strings
blanks = "_ " * len(gameword)
# The total amount of lives
lives = 6

# ASCII art of hangman gallows
hangman_gallows_0 = '''
    _______
   |/      |
   |      (_)
   |      \|/
   |       |
   |      / \\
   |
  _|___
'''
hangman_gallows_1 = '''
    _______
   |/      |
   |      (_)
   |      \|
   |       |
   |      / \\
   |
  _|___
'''
hangman_gallows_2 = '''
    _______
   |/      |
   |      (_)
   |       |
   |       |
   |      / \\
   |
  _|___
'''
hangman_gallows_3 = '''
    _______
   |/      |
   |      (_)
   |       |
   |       |
   |      / 
   |
  _|___
'''
hangman_gallows_4 = '''
    _______
   |/      |
   |      (_)
   |       |
   |       |
   |       
   |
  _|___
'''
hangman_gallows_5 = '''
    _______
   |/      |
   |      (_)
   |       
   |       
   |       
   |
  _|___
'''
hangman_gallows_6 = '''
    _______
   |/      |
   |      
   |       
   |       
   |       
   |
  _|___
'''

# Create dict of hangman gallow art to display based on lives
hangman_dict = {
    6: hangman_gallows_6,
    5: hangman_gallows_5,
    4: hangman_gallows_4,
    3: hangman_gallows_3,
    2: hangman_gallows_2,
    1: hangman_gallows_1,
    0: hangman_gallows_0,
}


print("Welcome to Hangman!")
print(hangman_dict[6])
print(blanks)
# Set up Game Loop