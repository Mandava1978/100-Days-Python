# List
# Data Structure

# For Example to store All states in USA
# Votes 

# fruits = [item1, item2] -- any type of data

states_of_america = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii",
                     "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan",
                     "Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
                     "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
                     "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin"]

print(states_of_america[0])
print(states_of_america[-1])

states_of_america.append("Wyoming")
print(states_of_america[-1])
states_of_america.append("Washington, D.C")
states_of_america.extend("American Samoa (AS)","Guam (GU)","Northern Mariana Islands (MP)","Puerto Rico (PR)","U.S. Virgin Islands (VI) ")

# https://docs.python.org/3/tutorial/datastructures.html