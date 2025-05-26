# This is a comment, we use # instead of // like in C++
print("Hello Rupert the Dog")
print("I meant... hello world!")



# Strings
# We can still use /n /t etc. as well as functions on the string like up/low/title
firstName = "john"
lastName = "DOE"
wholeName = firstName + " " + lastName
print(f"\nWhat's up {firstName.upper()} {lastName.lower()}")    
wholeName = wholeName.title()   # setting to normal title font for a name

# Ints, whole numbers
age = 20
print(f"\n{wholeName} is {age}")

# Float, decimal numbers
wage = 14.95
print(f"\n{wholeName} makes {wage} per hour")

# Boolean, T/F
isStudent = True
print(f"\nIs {wholeName} a student: {isStudent}")

if isStudent:
    print("\tYep that's true!")
else:
    print("Not a student...")



# Typecasting, turning a variable from one data type to another
name = "James Dean"
age = 30
gpa = 2.1
isStudent = True

print(type(gpa))    # prints gpa's data type

gpa = int(gpa)      # changes gpa to an int, notice the drop of decimal points
print(gpa)

age = str(age)
print(type(age))    # notice how it's a string not an int anymore



# User Input, takes in user input as a string
name = input("\nWhat is your name?: ")
print(f"\tHello {name.title()}")

age = input("\nHow old are you?: ")
# since the input function returns a string, for the age var we have to
# typecast it to an int to make it usable, see below
# This also works: age = int(input("prompt?: "))
age = int(age)
print(f"\tYou'll be {age + 1} soon enough")