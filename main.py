#!/usr/bin/python3

import bot, val

print("Hi There! Let's play 2 truths and a lie!")
print("Please enter 3 statements, 2 true and 1 false.")
s1=input("Please enter your first statment:")
assert val.input_val == True

s2=input("Please enter your second statment:")
s3=input("Please enter your third statement:")

print("your statements are: " + s1 + ", " + s2 + ", " + s3)



statement1=(s1, True)
statement2=(s2, True)
statement3=(s3, True)

#print(statement1)
