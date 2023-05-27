import random

# Open hangman.txt and set the word for the game
with open('hangman.txt', 'r') as file:
    lines = file.readlines()
    gameword = random.choice(lines).strip() #.strip() to remove \n from string

# Preliminary game setup

# Set up list of underscores
underscores = ["_" for char in gameword]
# Set up list of guessed letters
guessed_chars = []
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

win = False
print("Welcome to Hangman!")
# Set up Game Loop

while lives > 0 and not win:
    #Print gallows + blanks
    print(hangman_dict[lives])
    blanks = " ".join(underscores)
    print(blanks)
    print("Not in the word:", ",".join(guessed_chars))

    user_guess = input("Guess a letter: ")

    while len(user_guess) != 1: # Ensures the guess is just a letter
        user_guess = input("Guess a letter: ")

    # Control flow for after user inputs a letter to guess
    if gameword.count(user_guess) > 0:
        start_index = gameword.find(user_guess)
        while start_index != -1:
            underscores[start_index] = user_guess
            start_index = gameword.find(user_guess, start_index + 1)
    else:
        guessed_chars.append(user_guess)
        print(user_guess, "is not in the word!")
        lives = lives - 1
    
    # win/lose conditions
    check_word = "".join(underscores)
    if check_word == gameword:
        blanks = " ".join(underscores)
        print(hangman_dict[lives])
        print(blanks)
        print("You correctly guessed the word " + gameword + "!")
        win = True
    if lives == 0:
        print(hangman_dict[0])
        print("You lost :( The word was:", gameword)