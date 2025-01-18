import os
import platform

WORDLIST_LINK = "https://eagerterrier.github.io/previous-wordle-words/chronological.txt"

print("Running chronological wordlist update...")
os.system(f"curl -O -s {WORDLIST_LINK}")
os.system("mv chronological.txt .\\wordlists\\prior_wordle_list_chrono.txt")