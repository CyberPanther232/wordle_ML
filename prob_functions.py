"""
Program: prob_functions
Date Created: 24-Jun-2024
Last Modified: 28-Jun-2024
Purpose: To provide probability results for increasing wordle bot guessing algorithms
Developer: Hunter Kinney
"""
from wordle_funcs import load_words
import math

# wordle_list = load_words("smaller_wordlist.txt")

def probability_of_letter(Letter, word_list) -> float:
    
    words_with_letter = []
    
    for word in word_list:
        for letter in word:
            if letter == Letter:
                words_with_letter.append(word)
    
    return len(words_with_letter) / len(word_list)
           
def information_content(Prob, Letter) -> float:
    if Prob <= 0 or Prob >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive).")
    
    return -math.log2(Prob)

def information_content_w_prob(I, word_list) -> float:
    
    if I <= 0:
        raise ValueError("Information content (I) must be positive.")
    
    # Calculate MA using the equation MA = 1 / (2^I) * M
    num_of_words = len(word_list)
    
    num_of_occurrences = round((1 / (2 ** I)) * num_of_words,0)
    
    return num_of_occurrences
                    
def probability_of_word(wordlist_path):
    
    word_list = load_words(wordlist_path)
    
    words = {}
    
    for word in word_list:
        
        if word not in words:
            words.update({word : 1})
        
        elif word in words:
            words[word] += 1
            
    return words

from collections import Counter

def calculate_entropy_for_word(guess, potential_words):
    """
    Calculate the entropy for a given guess based on the list of potential words.
    
    Parameters:
    guess (str): The word to guess.
    potential_words (list of str): The list of possible target words.
    
    Returns:
    float: The entropy value for the guess.
    """
    # Simulate feedback for the guess
    feedback_patterns = [get_feedback(guess, target) for target in potential_words]
    
    # Count the frequency of each feedback pattern
    pattern_counts = Counter(feedback_patterns)
    
    # Calculate probabilities of each pattern
    total_patterns = len(feedback_patterns)
    probabilities = [count / total_patterns for count in pattern_counts.values()]
    
    # Calculate entropy
    return entropy(probabilities)

def get_feedback(guess, target):
    """
    Simulate feedback for a guess given a target word.
    Returns a tuple representing the pattern (green, yellow, gray).
    
    Parameters:
    guess (str): The guessed word.
    target (str): The target word.
    
    Returns:
    tuple: The feedback pattern.
    """
    feedback = []
    for g, t in zip(guess, target):
        if g == t:
            feedback.append('green')
        elif g in target:
            feedback.append('yellow')
        else:
            feedback.append('gray')
    return tuple(feedback)

# Example usage
potential_words = ["apple", "banjo", "carol", "dogma", "eagle"]
guess = "apple"
entropy_value = calculate_entropy_for_word(guess, potential_words)
print(f"Entropy for guess '{guess}': {entropy_value}")

  
    
        
