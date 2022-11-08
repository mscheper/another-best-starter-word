from collections import Counter
import string

# Refer to README.md for a description of this program.

DICTIONARY_PATH = '/usr/share/dict/british-english'
"""The path to the dictionary, which is a file of words separated by line
breaks.

Linux, unfortunately, doesn't come with an Australian dictionary, and sadly,
Macquarie subscribers don't get access to the word list. But it seems Wordle
uses a US dictionary anyhow, and devs are free to use whatever dictionary they
want.
"""

LETTER_USED_MULTIPLIER = 0
"""The number of points to award for each five-letter word that contains a
letter at all.
"""

LETTER_IN_PLACE_MULTIPLIER = 1
"""The number of points to award for each five-letter word that has a letter in
the same position (index).
"""

ASCII_LOWERCASE_SET = set(string.ascii_lowercase)
"""The set of lowercase ASCII characters. We'll therefore miss words like
'naïve'.
"""


def five_letter_words():
    """Generator that yields all five-letter words in the dictionary."""
    for word in open(DICTIONARY_PATH):
        word = word.strip()
        # We only want five-letter words.
        if len(word) != 5:
            continue
        if not (ASCII_LOWERCASE_SET > set(word)):
            continue
        if word[-1] == 's' or word[-1] == 'd' or word[-2:] == 'er':
            continue
        yield word


def get_counters():
    """Analyse the dictionary and return an array of 6 `Counter`s, each keyed
    by a lowercase ASCII letter. The first 5 `Counter`s count the number of
    times a letter appears in the respective index of a five-letter word in the
    dictionary. The last `Counter` counts the number of five-letter words in
    the dictionary that contain the letter at all.
    """
    counters = [Counter() for _ in range(6)]

    for word in five_letter_words():
        for index, letter in enumerate(word):
            counters[index][letter] += 1
        for letter in set(word):
            counters[-1][letter] += 1

    return counters


def score_words(counters):
    """Score all five-letter words in the dictionary. The scores are returned
    in a dict, keyed by the words.
    """
    word_scores = {}
    for word in five_letter_words():
        letter_used_score = 0
        letter_in_place_score = 0
        for letter in set(word):
            letter_used_score += counters[-1][letter] * LETTER_USED_MULTIPLIER
        for index, letter in enumerate(word):
            letter_in_place_score += counters[index][
                letter] * LETTER_IN_PLACE_MULTIPLIER
        word_scores[word] = letter_used_score + letter_in_place_score

    return word_scores


counters = get_counters()
word_scores = score_words(counters)
for word in sorted(word_scores, key=word_scores.get):
    print(word, word_scores[word])
