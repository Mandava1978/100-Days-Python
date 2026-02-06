
print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? $"))
tip = int(input("\nHow much tip percent would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_with_tip = total_bill + (total_bill * tip_percent)
per_person = total_with_tip / people

print(f"Each person should pay: ${per_person:.2f}")
