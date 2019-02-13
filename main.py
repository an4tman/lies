#!/usr/bin/python3

import bot, val

print("Hi There! Let's play 2 truths and a lie!")
print("Please enter 3 statements, 2 true and 1 false.")
print("Statements must be correct english sentences ending in a period.")

while True:
    s1=input("Please enter your first statment:")
    #assert val.input_val == True
    if val.input_val(s1):
        break
    else:
        print("Your input is invalid.")


while True:
    s2=input("Please enter your second statment:")
    if val.input_val(s2):
        break
    else:
        print("Your input is invalid.")

while True:
    s3=input("Please enter your third statement:")
    if val.input_val(s3):
        break
    else:
        print("Your input is invalid.")

print("your statements are: " + s1 + ", " + s2 + ", " + s3)
s = [s1,s2,s3]
lie = bot.longest(s1,s2,s3)
print("The bot thinks that, \"" + lie + "\" is a lie.\n")
correct_lie = ""
while correct_lie not in ["1","2","3"]:
    correct_lie = input("Which was your lie? [1|2|3]")
if s[int(correct_lie)-1] == lie:
    print("The bot was right!")
else:
    print("stupid bot")

