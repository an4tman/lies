import sys
import random 
import nltk
from nltk.corpus  import words as nltk_words
import re


def is_english_word(word):   
    dictionary = set(nltk_words.words())
    if word in dictionary == True:
        return True
    else:
        return False


def is_statement_english(statement):
    words_in_statement = re.split(r'[;,\.\s]\s*', statement) #deliminates on commas, semicolon, period and any amounnt of white spaces
    print(words_in_statement)
    for word in words_in_statement:
        if is_english_word(word) == False:
#            print(word+" is not a word")
            return False
    return True


print("Hi There! Let's play 2 truths and a lie!")
print("Please enter 3 statements, 2 true and 1 false.")
s1=input("Please enter your first statment:")
assert is_statement_english(s1) == True

s2=input("Please enter your second statment:")
s3=input("Please enter your third statement:")

print("your statements are: " + s1 + ", " + s2 + ", " + s3)



statement1=(s1, True)
statement2=(s2, True)
statement3=(s3, True)

#print(statement1)
