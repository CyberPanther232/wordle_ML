"""
Program: prob_functions
Date Created: 24-Jun-2024
Purpose: To have letter selection probability
Developer: Hunter Kinney
"""
from wordle_funcs import load_words
import math

# wordle_list = load_words("smaller_wordlist.txt")

def probability_of_letter(Letter, word_list):
    
    words_with_letter = []
    
    for word in word_list:
        for letter in word:
            if letter == Letter:
                words_with_letter.append(word)
    
    return len(words_with_letter) / len(word_list)
           
def information_content(Prob, Letter):
    if Prob <= 0 or Prob >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive).")
    
    return -math.log2(Prob)

def information_content_w_prob(I, word_list):
    
    if I <= 0:
        raise ValueError("Information content (I) must be positive.")
    
    # Calculate MA using the equation MA = 1 / (2^I) * M
    num_of_words = len(word_list)
    
    num_of_occurrences = round((1 / (2 ** I)) * num_of_words,0)
    
    return num_of_occurrences
                    

# prob_a = probability_of_letter('x', wordle_list)
# information = information_content(prob_a, 'x')

# print(prob_a)
# print(information)
# print(information_content_w_prob(information, wordle_list))