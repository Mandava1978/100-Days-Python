print("\033[32m" + r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |                   
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[srinu]
*******************************************************************************
''' + "\033[0m")

print("Welcome to Treasure Island")
print("Your Mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
LorR = input('Type "left" or "right" ')

if LorR.upper()=="LEFT":
    print("you've come to a lake. There is an island in the middle of the lake.")
    WorS = input('Type "wait" to wait for a boat. Type "swim" to swim across.')
    if WorS.upper()=='WAIT':
        print("Boat")
        color = input('Which color Door you want open (Red , Blue, Green). Type "Red" , "Blue", "Yellow"  ?')
        if color.upper() == "YELLOW":
             print("You found the treasure. You Win!!!")
        elif color.upper() == "BLUE":
             print("Eaten by beasts. Game Over.")
        elif color.upper() == "RED":
             print("Burned by fire. Game Over.")
        else:
             print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
        print("You Fall into a hole. Game Over.")