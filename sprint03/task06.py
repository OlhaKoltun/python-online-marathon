# Generator function randomWord has as an argument list of words. It should return any random word from this list. 
# Each time words are different until the end of the list is reached. Then words are taken from the initial list again.

import random

def randomWord(words):
    if not words:
        words = [None]
    while True:
        unique_index = random.sample(range(len(words)), len(words))
        for i in unique_index:
            yield words[i]
