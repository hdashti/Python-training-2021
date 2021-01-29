# Define a function to print the number of unique words in a text

from collections import Counter


def word_frequncy(text):
    words = text.lower().split()
    unique_words = set(words)
    word_counter = Counter(unique_words)
    return word_counter


text = "Hello How are you"
ex = word_frequncy(text)
print(ex)
