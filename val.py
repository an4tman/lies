import sys
import random
import nltk
from nltk.corpus  import words as nltk_words
import re


def is_english_word(word):
    """
    Check that individual word is in dictionary

    param word: string from split user input
    rtype: bool
    """
    dictionary = set(nltk_words.words())
    if word in dictionary:
        return True
    else:
        print(word + " is not a legal english word")
        return False


def is_statement_english(statement):
    """
    check that user input sentence is in english

    param statement: user input statement
    rtype: bool
    """
    words_in_statement = re.split(r'[;,\.\s]\s*', statement) #deliminates on commas, semicolon, period and any amounnt of white spaces
    for word in words_in_statement:
        if is_english_word(word) == False:
            print("This sentence contains illegal words")
            return False
    return True

def validate_length(us):
    """
    Check that input string is not longer than 140 characters.

    param us: a user-input string
    rtype: bool
    """
    if len(us) <= 140:
        return True
    else:
        print("This sentence is more than 140 characters.")
        return False


def validate_sentence(us):
    """
    Check that input string ends with a period.

    param us: a user-input string
    rtype: bool
    """
    if us[-1] == '.':
        return True
    else:
        print("This sentence does not end in a period")
        return False

def input_val(s):
    """
    run all input val checks on input

    param s: user input string
    rtype: bool
    """
    return validate_length(s) and validate_sentence(s) and is_statement_english(s)

