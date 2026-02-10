print("Welcome to Python Pizza Deliveries!")
size =input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Small pizza :$15
# Medium pizza :$20
# Large pizza : $25

# Add pepperoni to small pizza : + $2
# Add Pepperoni to Medium or Large Pizza (Y or N): +$ 3
# Add extra cheese for any pizza (Y or N): +$1

# Work out how much they need to pay based on their pizza size choice.

cost=0
if size.upper()=='S':
    cost=15
elif size.upper()=='M':
    cost=20
elif size.upper() == 'L':
    cost=25

# Work out how much to add to their bill based on their pepperoni choice.

if pepperoni.upper()=='Y':
    if size.upper()=='S':
        cost+=2
    elif size.upper()=='M':
        cost+=3
    elif size.upper() == 'L':
        cost+=3
   
# Work out their final amount based on whether if they want extra cheese.

if extra_cheese.upper()=='Y':
    cost+=1

print(f"The total cost of pizza {size} & pepperoni is {pepperoni} and extra_cheese is {extra_cheese} = {cost}")
