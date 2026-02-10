# and
# or
# not

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

cost=0
if height >= 120 :
    print("You can ride the rollercoaster")
    age=int(input("What is your age now? "))
    if age<12:
        cost += 5
    elif age>=12 and age<18:
        cost += 7
    elif age>=18 and age<45:
        cost += 12
    else:
        cost += 0

    photos= input("Do you want pepperoni on your pizza? Y or N: ")

    if photos.upper()=="Y":
        cost+=3
    
    print(f"Your Total Bill is : ${cost}")



else:
    print("Sorry you have to grow taller before you can ride.")