import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

user = input("Choose rock, paper, or scissors: ").lower()

if user not in art:
    print("Invalid choice!")
else:
    computer = random.choice(list(art.keys()))

    print("\nYou chose:")
    print(art[user])

    print("Computer chose:")
    print(art[computer])

    if user == computer:
        print("It's a tie! 🤝")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
