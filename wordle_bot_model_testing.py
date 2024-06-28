from collections import Counter
from wordle_funcs import load_words
from wordle_bot_filters import *
from prob_functions import probability_of_letter
import time
import statistics as stats

# Model Parameters
DAYS = 1
NUM_OF_LETTERS = 1
POSS_SOLUTIONS_LIST = r'wordlists\smaller_wordlist.txt'
RECENT_WORDS_LIST = r'wordlists\prior_wordle_list_chrono.txt'

# Model Evaluation Parameters
REPORT_NAME = 'overall_report.txt'
TARGET_WORD = 'order'

def find_best_model(days, letters, report_name, attempts, target, iterations, save_all_results=False) -> None:
    
    lowest_model_avg_score = automated_testing(target, attempts, days, letters)
    optimal_day_param = days
    optimal_letter_param = letters
    
    for iteration in range(0, iterations):
        model_avg_score = automated_testing(target, attempts, days, letters)
        if model_avg_score <= lowest_model_avg_score:
            lowest_model_avg_score = model_avg_score
            optimal_day_param = days
            optimal_letter_param = letters
            print(f"Current model has the lowest average score of {lowest_model_avg_score} guesses!")
            
        elif model_avg_score > lowest_model_avg_score:
            print(f"Current model tested has an average score of {model_avg_score} guesses. The lowest average is {lowest_model_avg_score} guesses!")
        
        if save_all_results:
            with open(report_name, 'a') as results:
                results.write(f'{iteration},{days},{letters},{model_avg_score}\n')
            results.close()
        
        if letters >= 7:
            days += 5
            print("Adjusting days by + 5!")
        else:
            letters += 1
            
    print("Model Evaluation Completed!")
    print(f"Out of {iterations} models tested the best model had the average score of {lowest_model_avg_score} guesses and the parameters of days: {optimal_day_param} and letters: {optimal_letter_param}")
                
    # with open(report_name, 'w') as results:
    #     results.write(f'The most optimal model is the model with these parameters:\nDays: {optimal_day_param} Lower Prob Letters: {optimal_letter_param} Average Guess Score: {lowest_model_avg_score}')
    # results.close()

def write_automated_report(word, attempt_number, guess_number, report_title, num_days, num_letters) -> None:
    try:
        open(report_title, 'x')
        
        with open(report_title, 'w') as report_file:
            report_file.write(f'MODEL PARAMETERS:\nNumber of Days: {num_days}\nNumber of Lower Probability Letters: {num_letters}\n')
            report_file.write('Test_Num,Num_Of_Attempts,Target_Word')
            
        report_file.close()
    except FileExistsError:
        pass
    
    with open(report_title, 'a') as report:
        report.write(f'\n{attempt_number},{guess_number},{word}')

# Score each word based on letter frequencies
def score_word(word, frequencies) -> list:
    return sum(frequencies.get(letter, 0) for letter in word)

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

def automated_testing(target, attempts, days, num_letters):
    
    print("Running automated wordle tests to evaluate model...")
    
    sum_of_guesses = 0
    
    for attempt in range(0, attempts + 1):
        
        word_list = load_words(POSS_SOLUTIONS_LIST)
        recent_word_list = load_words(RECENT_WORDS_LIST)
        
        count = 1

        word_list = filter_recent_words(word_list, recent_word_list, days)

        guess = first_guess_filter(word_list, num_letters)

        while count < 7:
            # print(guess)
            feedback = wordle_feedback(guess, target)
            # print(feedback)
            
            if feedback == "ggggg":
                # print("YES!!!")
                # print(f"I guessed it in {count} guesses!")
                
                # write_automated_report(target, attempt, count, REPORT_NAME, DAYS, NUM_OF_LETTERS)
                sum_of_guesses += count
                
                break
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
            top_words = sorted_words[:5]

            # Update word_list for the next iteration
            word_list = filtered_word_list

            count += 1
            
            guess = top_words[0][0]
    print(f"Model Testing Completed!\nNumber of attempts {attempts}!")
    
    # Descriptives
    average = round((sum_of_guesses / attempts),2)
    
    return round((sum_of_guesses / attempts),2)

if __name__ == "__main__":
    find_best_model(DAYS, NUM_OF_LETTERS, REPORT_NAME, 1000, TARGET_WORD, 150, True)
