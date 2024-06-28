"""
Program: wordle_bot
Date Created: 24-Jun-2024
Last Modified: 28-Jun-2024
Purpose: To provide an accurate model to help those who want to play wordle but want to take it easy
Developer: Hunter Kinney
"""

from collections import Counter
from wordle_funcs import load_words
from wordle_bot_filters import *
from prob_functions import *
import time
from datetime import datetime

# # Load the word list
# word_list = load_words('smaller_wordlist.txt')
# recent_word_list = load_words('prior_wordle_list_chrono.txt')
# unobscured_list = load_words('prior_wordle_list_alpha.txt')

# Model Parameters
DAYS = 150
NUM_OF_LETTERS = 7
POSS_SOLUTIONS_LIST = r'wordlists/smaller_wordlist.txt'
RECENT_WORDS_LIST = r'wordlists/prior_wordle_list_chrono.txt'

# Score each word based on letter frequencies
def score_word(word, frequencies) -> list:
    return sum(frequencies.get(letter, 0) for letter in word)

def main():
    print("Welcome to Hunter's Wordle bot!\nI will guess a word and you provide the feedback!")
    count = 1
    
    word_list = load_words(POSS_SOLUTIONS_LIST)
    
    recent_word_list = load_words(RECENT_WORDS_LIST)

    word_list = filter_recent_words(word_list, recent_word_list, DAYS)

    guess = first_guess_filter(word_list, NUM_OF_LETTERS)
    
    feedback_data = []

    while count < 7:
        print(guess)
        feedback = input("Enter feedback in format (gybgy): ").strip().lower()
        
        if feedback == "ggggg":
            print("YES!!!")
            print(f"I guessed it in {count} guesses!")
            
            print("Thank you for using Hunter's Wordle bot!")
            exit(0)
            
        else:
            pass

        # Update the word list based on the feedback
        filtered_word_list = filter_words(word_list, guess, feedback)

        if not filtered_word_list:
            print("No matching words found based on the feedback.")
            break

        # Calculate letter frequencies from the filtered word list
        letter_counts = Counter()
        for word in filtered_word_list:
            letter_counts.update(word)

        # Calculate the frequency of each letter
        total_letters = sum(letter_counts.values())
        letter_frequencies = {letter: count / total_letters for letter, count in letter_counts.items()}

        word_scores = {word: score_word(word, letter_frequencies) for word in filtered_word_list}

        # Sort words by their scores and get the top five
        sorted_words = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)
        top_words = sorted_words[:10]

        # Update word_list for the next iteration
        word_list = filtered_word_list

        count += 1
        
        feedback_data.append((guess, feedback))
        
        guess = find_best_guess_from_feedback(feedback_data, top_words)
        
    print("Thank you for using Hunter's Wordle bot!")
    
if __name__ == "__main__":
    # find_best_model(DAYS, NUM_OF_LETTERS, REPORT_NAME, 1000, TARGET_WORD, 1000, True)
    # automated_testing(TARGET, 1000, POSS_SOLUTIONS_LIST, RECENT_WORDS_LIST, DAYS, NUM_OF_LETTERS)
    main()
