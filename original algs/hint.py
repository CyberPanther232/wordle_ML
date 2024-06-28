from collections import Counter
from wordle import load_words

# Load the word list
word_list = load_words('valid-wordle-words.txt')

# Function to update the list of possible words based on feedback
def filter_words(words, guess, feedback):
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

# Score each word based on letter frequencies
def score_word(word, frequencies):
    return sum(frequencies.get(letter, 0) for letter in word)

count = 0

while count < 7:
    guess = input("Enter guess: ").strip().lower()
    feedback = input("Enter feedback in format (gybgy): ").strip().lower()
    
    if feedback == "ggggg":
        print("Great! Glad I could help!")
        print(f"This was guessed in {count} guesses!")
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

    # Output the top five words
    print("Top five words sorted by frequency-based score after applying feedback:")
    for word, score in top_words:
        print(f"{word}: {score:.4f}")

    # Update word_list for the next iteration
    word_list = filtered_word_list

    count += 1
    
print("Thank you for using the hint algorithm!")
