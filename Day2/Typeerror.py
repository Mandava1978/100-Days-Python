#print(len(123456))

#print(len(123456)) -- TypeError: object of type 'int' has no len()

print(type("hello"))
print(type(123))
print(type(123.458))
print(type(True))

print("123"+"456")
print(int("123")+int("456"))

#print(int("abc")+int("456")) #ValueError: invalid literal for int() with base 10: 'abc'
'''

int()
float()
str()
bool()

'''

#print("Number of letters in your name: " + len(input("Enter your name"))) -- TypeError: can only concatenate str (not "int") to str
print("Number of letters in your name: " + str(len(input("Enter your name"))))

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)


print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))

