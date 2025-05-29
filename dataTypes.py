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