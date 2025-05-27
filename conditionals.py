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