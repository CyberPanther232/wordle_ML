"""
Program: prob_functions
Date Created: 24-Jun-2024
Last Modified: 28-Jun-2024
Purpose: To provide probability results for increasing wordle bot guessing algorithms
Developer: Hunter Kinney
"""
from wordle_funcs import load_words
from collections import Counter
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

import math
from collections import Counter

def entropy(probabilities):
    """
    Calculate the entropy of a distribution for given probabilities.
    
    Parameters:
    probabilities (list of float): A list of probabilities.
    
    Returns:
    float: The entropy value.
    """
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def calculate_entropy_from_feedback(feedback_data, potential_words):
    """
    Calculate the entropy for all possible words based on manual feedback.
    
    Parameters:
    feedback_data (list of tuples): A list of tuples where each tuple contains
                                    (guess, feedback) with feedback being a string of 'g', 'y', 'b'.
    potential_words (list of str): The list of possible target words.
    
    Returns:
    dict: A dictionary with words as keys and their entropy values as values.
    """
    pattern_counts = Counter()
    
    for guess, feedback in feedback_data:
        for word in potential_words:
            if matches_feedback(guess, feedback, word):
                pattern_counts[word] += 1

    total_patterns = len(potential_words)
    probabilities = {word: pattern_counts[word] / total_patterns for word in potential_words}
    
    # Ensure all words have an entry in the probabilities dictionary
    entropies = {word: entropy([probabilities[word]]) for word in potential_words}
    return entropies

def matches_feedback(guess, feedback, target):
    """
    Check if a target word matches the given feedback for a guess.
    
    Parameters:
    guess (str): The guessed word.
    feedback (str): The feedback string ('g', 'y', 'b').
    target (str): The target word.
    
    Returns:
    bool: True if the target matches the feedback, False otherwise.
    """
    for g, f, t in zip(guess, feedback, target):
        if f == 'g' and g != t:
            return False
        if f == 'y' and (g == t or g not in target):
            return False
        if f == 'b' and g in target:
            return False
    return True

def find_best_guess_from_feedback(feedback_data, potential_words):
    """
    Find the best guess based on entropy calculated from manual feedback.
    
    Parameters:
    feedback_data (list of tuples): A list of tuples where each tuple contains
                                    (guess, feedback) with feedback being a string of 'g', 'y', 'b'.
    potential_words (list of str): The list of possible target words.
    
    Returns:
    str: The best guess based on entropy.
    """
    entropies = calculate_entropy_from_feedback(feedback_data, potential_words)
    
    max_entropies = max(entropies, key=entropies.get)
    print(max_entropies)
    return max_entropies

# Example usage
potential_words = ["order", "knead", "savor", "sword"]
feedback_data = [
    ("apple", "bbbyb"),  # 'a' is not in the word, 'p' is correct and in the right position
    ("banjo", "bbbby"),  # 'a' is not in the word, 'n' is in the word but not in the correct position
]

best_guess = find_best_guess_from_feedback(feedback_data, potential_words)
print(f"Best guess based on entropy: {best_guess}")


  
    
        
