word_list = ["aardvark","baboon","camel"]

# TODO-1 - Randomly choose a word from the word_list and assign to a variable called choosen_word. Then print it. _

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the choosen_word. Print "Right" 
#          If it is "Wrong" if it's not.

import random
randomword = random.choice(word_list)
print(randomword)
dashword=""
for char in randomword:
    dashword+="_"
print(dashword)

guess_letter = input("Guess a letter: ").lower()

print(guess_letter)

display=""

for char in randomword:
    if char == guess_letter:
        display += char
    else:
        display += "-"
print(display)