from collections import defaultdict, Counter
import string
from wordle import load_words

# Example word list (replace this with the actual Wordle word list)
# word_list = ["apple", "brace", "crane", "drake", "flake", "glaze", "house", "jumps", "knife", "llama"]
word_list = load_words('prior_wordle_list_chrono.txt')

# Step 1: Calculate positional letter frequencies
position_counts = [Counter() for _ in range(5)]
for word in word_list:
    for i, letter in enumerate(word):
        position_counts[i][letter] += 1

# Step 2: Calculate the probability of each letter in each position
total_words = len(word_list)
position_probabilities = []
for counter in position_counts:
    total_counts = sum(counter.values())
    probabilities = {letter: count / total_counts for letter, count in counter.items()}
    position_probabilities.append(probabilities)

# Step 3: Score each word based on positional letter probabilities
def score_word(word, probabilities):
    return sum(probabilities[i].get(letter, 0) for i, letter in enumerate(word))

word_scores = {word: score_word(word, position_probabilities) for word in word_list}

# Step 4: Sort words by their scores and get the top ten
sorted_words = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)
top_ten_words = sorted_words[:10]

# Output the top ten words
print("Top ten words sorted by positional probability-based score:")
for word, score in top_ten_words:
    print(f"{word}: {score:.4f}")
