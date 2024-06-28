"""
Program: prob_functions
Date Created: 24-Jun-2024
Last Modified: 28-Jun-2024
Purpose: To provide probability results for increasing wordle bot guessing algorithms
Developer: Hunter Kinney
"""

import random

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

def find_best_guess(potential_words):
    """
    Find the best guess based on maximum entropy.
    
    Parameters:
    potential_words (list of str): The list of possible target words.
    
    Returns:
    str: The best guess.
    """
    entropy_values = {word: calculate_entropy_for_word(word, potential_words) for word in potential_words}
    return max(entropy_values, key=entropy_values.get)

# Example usage
best_guess = find_best_guess(potential_words)
print(f"Best guess based on entropy: {best_guess}")

def main():
    
    words = load_words('valid-wordle-words.txt')
    
    wordle = random.choice(words)
    print(wordle)
    
    display_char_list = display_word(wordle)
    
    print(display_char_list)
    
if __name__ == "__main__":
    main()
            