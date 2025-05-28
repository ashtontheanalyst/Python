# All things loops
'''
# WHILE LOOP, execute something while a condition remains true, stop if it becomes false
food = input("Enter a food: (q to quit) ")

# Condition, while this do that
while not food == "q" and not food == "Q":
    # Body of the loop
    if not food.isalpha():
        print("Not a valid food")
        # Exit cond.
        food = input("Enter an actual food: (q to quit) ")
    else:
        print(f"So you like {food}, great!")
        food = input("Enter another food: (q to quit) ")
# When loop is done do this
print("You have good taste")
'''


# FOR LOOP, execute a block for a fixed iteration, for iterating over strings, nums, arays, etc.

# print 1 - 10
for x in range(1, 11):
    print(x)
print("-----")

# print 1 - 10, step by 3's
for x in range(1, 11, 3):
    print(x)
print("-----")

# print backwards, so 10 - 1
for x in reversed(range(1, 11)):
    print(x)
print("-----")
