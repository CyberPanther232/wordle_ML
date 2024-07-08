"""
Program: wordle_bot
Date Created: 24-Jun-2024
Last Modified: 28-Jun-2024
Purpose: To filter out words in wordlist to improve bot guessing success
Developer: Hunter Kinney
"""

import random
from prob_functions import probability_of_letter

# def filter_unobscured_words(word_list, unobscured_list) -> list:
#     for word in word_list:
#         if word not in unobscured_list:
#             word_list.remove(word)
            
#     return word_list

# Algorithm used to guess the first word in the guessing system
def first_guess_filter(wordlist, num_of_letters) -> list:
    alphabet = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z'
    ]

    letter_probabilities = {}

    for letter in alphabet:
        prob = probability_of_letter(letter, wordlist)
        letter_probabilities[letter] = prob
        
    sorted_letter_probabilities = sorted(letter_probabilities)

    sorted_dict = dict(sorted(letter_probabilities.items(), key=lambda x: x[1])[:num_of_letters])

    first_word_wordlist = []

    for word in wordlist:
        for letter in word:
            if letter in sorted_dict.keys() and word not in first_word_wordlist:
                first_word_wordlist.append(word)

    return random.choice(first_word_wordlist)

# Filters recent solution words from previous wordle games
def filter_recent_words(word_list, recent_list, days_passed) -> list:
    
    print(len(word_list))
    
    recent_list = recent_list # [:days_passed]
    
    for word in word_list:
        if word in recent_list:
            word_list.remove(word)
        else:
            pass
        
    print(len(word_list))
        
    return word_list

# Function to update the list of possible words based on feedback
def filter_words(words, guess, feedback) -> list:
    new_words = []
    for word in words:
        match = True
        yellow_letters = [guess[i] for i in range(len(feedback)) if feedback[i] == 'y']
        green_letters = [guess[i] for i in range(len(feedback)) if feedback[i] == 'g']
        black_letters = [guess[i] for i in range(len(feedback)) if feedback[i] == 'b']

        for i, (g_letter, f) in enumerate(zip(guess, feedback)):
            if f == 'g':  # Green: letter is correct and in the correct position
                if word[i] != g_letter:
                    match = False
                    break
            elif f == 'y':  # Yellow: letter is correct but in the wrong position
                if g_letter not in word or word[i] == g_letter:
                    match = False
                    break

        if match:
            for i, (g_letter, f) in enumerate(zip(guess, feedback)):
                if f == 'b':  # Black/Gray: letter is not in the word at all
                    if g_letter in word and g_letter not in yellow_letters and g_letter not in green_letters and g_letter in black_letters or word[i] == g_letter:
                        match = False
                        break
                
        if match:
            new_words.append(word)
        else:
            pass
        
        try:
            new_words.remove(guess)
        except ValueError:
            pass
        
    return new_words
