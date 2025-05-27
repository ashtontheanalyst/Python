# Different things you can do with a string

name = input("Enter your full name: ")

print(f"\n{name}")

name = name.capitalize()
print(name)
name = name.title()
print(name)
name = name.upper()
print(name)
name = name.lower()
print(name)


result = len(name)
# -1 is the returned value if one of these doesn't work
space = name.find(" ")      # first index of the string or char
last = name.rfind("o")      # last index occurence

print(f"\n{name} is {result} char's long")
print(f"The first space is at index {space}")
print(f"The last 'o' is at index {last}")


val = input("\nEnter one char or digit: ") 

result1 = val.isdigit()
result2 = val.isalpha()
result3 = val.isspace()
print(f"\nIs it a digit?: {result1}")
print(f"Is it a char?: {result2}")
print(f"Is it a space?: {result3}")