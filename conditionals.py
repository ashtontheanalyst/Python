# if statement, do something IF and condition is TRUE; else do something ELSE
age = int(input("Enter your age: "))

if age > 120:
    print("\tYou're definently dead.")
elif age >= 18:
    print("\tYou can sign up for a credit card!")
elif age < 0:
    print("\tYou haven't even been born.")
else:
    print("\tYou've got some time...")


# Little bit different
response = input("\nWould you like some food? (Y/N): ")

if response == "Y" or response == "y":
    print("Here's some food")
elif response == "N" or response == "n":
    print("That's fine, more for me")
else:
    print("Invalid response")


# Another with boolean
response = input("\nAre you online? (Y/N): ")

if response == "Y" or response == "y":
    online = True
elif response == "N" or response == "n":
    online = False

if online:
    print("The user is online")
elif not online:
    print("The user is not online")
else:
    print("Invalid input")



# Logical operators, these are the and, or, nots
# The not operator is for boolean values to say if it's False
temp = 75
isRaining = False
isSunny = True

if temp > 90 or temp < 40 or isRaining:
    print("\nOur event is cancelled!")
else:
    print("\nThe event is on")

if temp > 60 and temp < 80 and isSunny:
    print("It's a perfect day")
else:
    print("Not the best weather")

if not isRaining:
    print("It's not raining")



# Ternary operator, another way of writing a conditional expression
# Do THIS if condition met, ELSE do THAT
num = 5010498

sign = "Positive" if num > 0 else "Negative"
oddEven = "Even" if num % 2 == 0 else "Odd"
# This one has an elif function in it
size = "Large" if num >= 100000 else "Moderate" if num > 100 else "Small"

print(f"\n{num} is {sign}, {oddEven}, and {size}")