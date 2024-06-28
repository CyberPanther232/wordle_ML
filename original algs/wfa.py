from collections import Counter
import string
from wordle import load_words

# Example word list (replace this with the actual Wordle word list)
# word_list = ["apple", "brace", "crane", "drake", "flake", "glaze", "house", "jumps", "knife", "llama"]
word_list = load_words('prior_wordle_list_chrono.txt')

# Step 1: Calculate letter frequencies
letter_counts = Counter()
for word in word_list:
    letter_counts.update(word)

# Step 2: Calculate the frequency of each letter
total_letters = sum(letter_counts.values())
letter_frequencies = {letter: count / total_letters for letter, count in letter_counts.items()}

# Step 3: Score each word based on letter frequencies
def score_word(word, frequencies):
    return sum(frequencies.get(letter, 0) for letter in word)

word_scores = {word: score_word(word, letter_frequencies) for word in word_list}

sorted_words = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)

top_ten_words = sorted_words[:10]

# Output the top ten words
print("Top ten words sorted by frequency-based score:")
for word, score in top_ten_words:
    print(f"{word}: {score:.4f}")

# Output the sorted words
# print("Words sorted by frequency-based score:")
# for word in sorted_words:
#     print(f"{word}: {word_scores[word]:.4f}")
