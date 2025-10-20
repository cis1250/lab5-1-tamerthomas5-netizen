#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
def get_sentence():
    """Prompt user for a valid sentence and return it."""
    while True:
        sentence = input("Enter a sentence: ")

        # validation: starts capital & ends with . ? !
        if (len(sentence) > 0 and
            sentence[0].isupper() and
            sentence[-1] in ".?!"):
            return sentence
        else:
            print("Invalid sentence. It must start with a capital letter and end with . ? or !\n")


def calculate_frequencies(sentence):
    """Return two lists: words and their frequencies."""
    words = []
    freqs = []

    # remove ending punctuation and split
    word_list = sentence[:-1].split()

    for w in word_list:
        if w in words:
            idx = words.index(w)
            freqs[idx] += 1
        else:
            words.append(w)
            freqs.append(1)

    return words, freqs


def print_frequencies(words, freqs):
    """Print the frequencies in readable format."""
    print("\nWord Frequencies:")
    for w, f in zip(words, freqs):
        print(f"{w}: {f}")


def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)


# -------- Run program --------
main()
