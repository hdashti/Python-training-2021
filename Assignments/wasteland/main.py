import urllib.request
from collections import Counter

url = "https://www.gutenberg.org/files/1321/1321-0.txt"

with urllib.request.urlopen(url) as req:
    text = req.read().decode('utf-8')

start_text = "*** START OF THIS PROJECT GUTENBERG EBOOK THE WASTE LAND ***"
stop_text = "*** END OF THIS PROJECT GUTENBERG EBOOK THE WASTE LAND ***"

start = text.find(start_text) + len(start_text)
stop = text.find(stop_text)
poem = text[start:stop]

# Split the words and keep them in a list
words = poem.split()
#print(words)

#number of words
num_words= len(words)
print(num_words)

# Find the unique words
# Set remove the repeated words
unique_words = set(words)
#print(unique_words)
print(len(unique_words))

# We can work with set while we change all words to lowercase
words_lowecase = poem.lower().split()
unique_words = set(words_lowecase)
#print(unique_words)

# How many times each word repeated? # use counter from collections

words_lower = poem.lower().split()
word_counter = Counter(words_lower)
#print(word_counter)

# check one word
#print(word_counter['unreal'])





