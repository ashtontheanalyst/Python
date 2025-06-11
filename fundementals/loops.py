import time

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

# using continue and break
for x in range(1, 21):
    # skip over 11 through 14
    if x >= 11 and x < 15:
        continue
    elif x == 18:
        break
    print(x)
print("-----")



# Using the time module to countdown
# see 'import time' at top of doc

uTime = int(input("\nEnter a time in seconds for countdown: "))

for x in range(uTime, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("BOOM!!!!!!!!!!!!!")
'''


# NESTED LOOPS, a loop within one, maybe within another, within something..
for x in range(1, 11):
    print(x, end=" ")       # Instead of newline, we put a space after each x
print("\n")

# The outter loop spits out the inner loop 1-10, four times
for i in range(4):          
    for j in range(1, 11):
        print(j, end=" ")
    print()
print()

# Making it cooler looking
for i in range(3):
    if i < 2:
        print("------------------")
        for j in range(20, -1, -2):
            if j == 0:
                print(j)
            else:
                print(j, end=", ")
    else:
        print("------------------")
        for j in range(20, -1, -2):
            if j == 0:
                print(j)
            else:
                print(j, end=", ")
        print("------------------")