import random

def display_word(word) -> list:
    display_word = []
    for letter in word:
        if letter == " ":
            display_word.append(" ")
        else:
            display_word.append("_")
    return display_word

def load_words(wordlist_filepath) -> list:
    
    wordlist = []
    
    with open(wordlist_filepath, 'r') as wordfile:
        for line in wordfile:
            fields = line.strip('\n').split(' ')
            
            word = fields[0].lower()
            
            wordlist.append(word)
            
    return wordlist


def main():
    
    words = load_words('valid-wordle-words.txt')
    
    wordle = random.choice(words)
    print(wordle)
    
    display_char_list = display_word(wordle)
    
    print(display_char_list)
    
if __name__ == "__main__":
    main()
            