import random
from words import word_list


# Function that returns word to game
def get_word():
    word = random.choice(word_list)
    return word.upper()


# Interactive game function
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # List that holds the letters that player guessed
    guessed_words = []  # List that holds the words that player guessed 
    attempt = 8  # Number of attempts
