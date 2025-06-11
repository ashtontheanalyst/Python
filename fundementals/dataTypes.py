# Holding data types apart from the basic one values like int, float, char, etc.

# LIST  = []    Ordered and changeable. Duplicates ok
# SET   = {}    Unordered and immutable, but adding/removing ok. Can't duplicate
# TUPLE = ()    Ordered and unchangeable. Duplicates ok. FAST


# This is a LIST of strings
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)           # Prints the list straight-up, not nicely readable
print(fruits[::-1])     # backwards
print(fruits[1::2])     # prints even indexes
print(fruits[::2])      # prints odd indexes

# Modifing it
fruits[1] = "guava"
fruits.append("kiwi")
fruits.remove("apple")
fruits.insert(2, "tangerine")
fruits.sort()                   # alpha order
fruits.reverse()                # reversed after we sorted so now it's backwards alpha
print(fruits.index("guava"))
print(fruits.count("apple"))

# Prints the way you want it by iterating
for fruit in fruits:
    print(fruit, end=" ")
print()

# dir() tells you what functions are available for that object, in this case a list#
#print(dir(fruits))

# help() gives you a full man page on what those functions do, how to use them, etc.
#print(help(fruits))

# Check to see if value in the list, set, or tuple
print("apple" in fruits)       # is this string in the list? Return T/F



# SET   = {}    Unordered and immutable (can't change values), but adding/removing ok. Can't duplicate

# This is a SET of strings, looks similar to a list
cars = {"f40", "corvette", "335i", "c63 amg"}

print(cars)                # each time, this print will be different since it's unordered 
print(len(cars))
print("corvette" in cars)

# We cannot use subscripting on a string since it's unordered. i.e.
# print(cars[::-1])     would make it reveresed
# print(cars[0])        would print first value
# etc..

# "modifying" the set
cars.add("mustang")
cars.remove("f40")
cars.pop()                 # removes the first value

print(cars)



# TUPLE = ()    Ordered and unchangeable values. Duplicates ok. FAST

# a TUPLE of strings, can't change the assigned values within, but at least they're ordered
colors = ("black", "white", "black", "green", "red", "blue")

print(colors)

print(colors[0])           # can be indexed list a list
# colors[0] = "orange"     # not allowed!
print(colors[::-1])        # reversing it
print(colors[::2])         # every odd indexed vals
print(colors[1::2])        # even indexed vals

print(len(colors))
print("red" in colors)

# Our only two TUPLE methods
print(colors.count("black"))
print(colors.index("green"))



# 2D LIST, think of this like an excel spreadsheet with rows and columns
dodges = ["hellcat", "durango", "1500", "charger"]
fords = ["mustang", "SUV", "F150", "escape"]
chevys = ["corvette", "tahoe", "suburban", "silverado"]

# Now we have a list of lists, 2D LIST
brands = [dodges, fords, chevys]

# Prints in the less readable format
print(brands)
print(brands[1])            # prints the first indexed sub list
brands[2][2] = "camaro"     # changes the third value in the third list (2,2) indexes

# Pretty print each value
for i in range(len(brands)):
    for j in range(len(brands[i])):
        print(brands[i][j], end=" ")
    print()

# Another way to do the above print
for brand in brands:
    for car in brand:
        print(car, end=" ")
    print()



# 2D TUPLE, similar to the 2D list but with tuple properties
numPad = ((1, 2, 3), 
          (4, 5, 6), 
          (7, 8, 9), 
          ("*", 0, "#"))

for row in numPad:
    for button in row:
        print(button, end=" ")
    print()