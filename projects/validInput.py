# Make sure the user input is no more than 12 char's
# it cannot contain spaces
# it cannot contain digits

userInput = input("Enter a user name: ")

# Checks
userLen = len(userInput)            # returns an int
userSpace = userInput.find(" ")     # returns -1 if space not found
userAlpha = userInput.isalpha()     # Returns TRUE if string is fully alpha chars

# Input validation checks (conditionals)
if userLen > 12 or userSpace != -1 or not userAlpha:
    print(f"{userInput} is not a valid username!")
else:
    print(f"{userInput} is fine.")