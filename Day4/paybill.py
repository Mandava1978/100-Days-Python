import random
friends = ["Srinu","Siri","Thanu","Hrushi"]

# Option 1
print(random.choice(friends))

# Option 2
print(friends[int(random.randint(0,len(friends)-1))])


