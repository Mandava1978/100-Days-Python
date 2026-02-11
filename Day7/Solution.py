word_list = ["aardvark","baboon","camel"]
#  ["python", "developer", "hangman", "programming", "computer"]
# TODO-1 - Randomly choose a word from the word_list and assign to a variable called choosen_word. Then print it. _

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the choosen_word. Print "Right" 
#          If it is "Wrong" if it's not.

import random
# Hangman stages (from 6 lives to 0)
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

randomword = random.choice(word_list)
print(randomword)
dashword=""
for char in randomword:
    dashword+="_"
print(dashword)

game_over = False
correct_letters = []
lives =6

while not game_over:

    guess_letter = input("Guess a letter: ").lower()

    print(guess_letter)

    display=""

    for char in randomword:
        if char == guess_letter:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char            
        else:
            display += "-"
    print(display)

    if guess_letter  not in randomword:
        lives-=1
        if lives == 0:
            game_over =True
            print(stages[lives])
            print("****************************YOU LOSE.****************************")
        else:
            print(f"you have pending lives is {lives}")
            print(stages[lives])

    if "-" not in display:
        game_over = True
        print("****************************GAME OVER.****************************")
