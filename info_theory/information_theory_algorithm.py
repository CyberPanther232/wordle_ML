import random
from collections import defaultdict
import math

def load_wordlist(filename):
    with open(filename, 'r') as f:
        wordlist = [line.strip().lower() for line in f]
    return wordlist

def calculate_feedback(guess, secret_word):
    correct_positions = sum(1 for g, s in zip(guess, secret_word) if g == s)
    common_letters = sum(min(guess.count(letter), secret_word.count(letter)) for letter in set(guess))
    correct_letters = common_letters - correct_positions
    return correct_positions, correct_letters

def calculate_entropy(wordlist, guess):
    if len(wordlist) == 0:
        return float('inf')  # Maximize entropy when no words left
    
    letter_counts = defaultdict(int)
    total_words = len(wordlist)
    
    for word in wordlist:
        letter_counts[word[0]] += 1
    
    entropy = 0.0
    for count in letter_counts.values():
        probability = count / total_words
        entropy -= probability * math.log2(probability)
    
    return entropy

def select_next_guess(wordlist, guesses):
    min_entropy = float('inf')
    best_guess = None
    
    for word in wordlist:
        entropy = calculate_entropy(wordlist, word)
        if entropy < min_entropy and word not in guesses:
            min_entropy = entropy
            best_guess = word
    
    return best_guess

def update_wordlist(wordlist, guess, feedback):
    updated_wordlist = []
    for word in wordlist:
        if calculate_feedback(guess, word) == feedback:
            updated_wordlist.append(word)
    return updated_wordlist

def wordle_algorithm(wordlist):
    secret_word = 'smart'
    possible_words = [word for word in wordlist if len(word) == len(secret_word)]
    guesses = []
    max_guesses = 6
    
    while len(guesses) < max_guesses:
        guess = select_next_guess(possible_words, guesses)
        guesses.append(guess)
        print(f"Guess #{len(guesses)}: {guess}")
        
        feedback = calculate_feedback(guess, secret_word)
        possible_words = update_wordlist(possible_words, guess, feedback)
        
        if guess == secret_word:
            print("Congratulations! You've guessed the secret word:", secret_word)
            break
    
    if guess != secret_word:
        print("Sorry, you didn't guess the secret word. The secret word was:", secret_word)

# Example usage:
wordlist = load_wordlist('smaller_wordlist.txt')  # Replace with your own wordlist file
wordle_algorithm(wordlist)
