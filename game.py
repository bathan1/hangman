import random

# Open hangman.txt and set the word for the game
with open('hangman.txt', 'r') as file:
    lines = file.readlines()
    gameword = random.choice(lines).strip() #.strip() to remove \n from string

