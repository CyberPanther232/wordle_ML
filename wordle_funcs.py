"""
Program: prob_functions
Date Created: 24-Jun-2024
Last Modified: 28-Jun-2024
Purpose: To provide probability results for increasing wordle bot guessing algorithms
Developer: Hunter Kinney
"""

import random

# Score each word based on letter frequencies
def score_word(word, frequencies) -> list:
    return sum(frequencies.get(letter, 0) for letter in word)

def display_word(word) -> list:
    display_word = []
    for letter in word:
        if letter == " ":
            display_word.append(" ")
        else:
            display_word.append("_")
    return display_word

def load_words(wordlist_filepath) -> list:
    
    wordlist = []
    
    with open(wordlist_filepath, 'r') as wordfile:
        for line in wordfile:
            fields = line.strip('\n').split(' ')
            
            word = fields[0].lower()
            
            wordlist.append(word)
            
    return wordlist

# Automated wordle feedback for automated testing
def wordle_feedback(guess, target) -> str:
    feedback = ['b'] * len(guess)  # Initialize feedback with 'b' for grey
    target_chars = list(target)  # List of target characters to help with yellow feedback
    
    # First pass: Check for greens
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback[i] = 'g'
            target_chars[i] = None  # Remove the matched character

    # Second pass: Check for yellows
    for i in range(len(guess)):
        if feedback[i] == 'b' and guess[i] in target_chars:
            feedback[i] = 'y'
            target_chars[target_chars.index(guess[i])] = None  # Remove the matched character
    
    return ''.join(feedback)

def main():
    
    words = load_words('valid-wordle-words.txt')
    
    wordle = random.choice(words)
    print(wordle)
    
    display_char_list = display_word(wordle)
    
    print(display_char_list)
    
if __name__ == "__main__":
    main()
            