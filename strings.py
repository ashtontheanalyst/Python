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
counter = name.count("a")   # return a number with the specific sub string, char, digit, or etc.

print(f"\n{name} is {result} char's long")
print(f"The first space is at index {space}")
print(f"The last 'o' is at index {last}")
print(f"It has {counter} a's")


val = input("\nEnter one char or digit: ") 

result1 = val.isdigit()     # determine if it's a digit...
result2 = val.isalpha()
result3 = val.isspace()
print(f"\nIs it a digit?: {result1}")
print(f"Is it a char?: {result2}")
print(f"Is it a space?: {result3}")


phone = input("\nEnter your phone number with dashes: ")
phone = phone.replace("-", " ")
print(f"Now your number is {phone}")



# String Indexing, [start : end : step]
creditNum = "1234-5678-1111-2222"
print(creditNum)

print(creditNum[0 : len(creditNum) : 2])    # Print every second char start to end, stepping
print(creditNum[::2])                       # Does the same thing
print(creditNum[:4])                        # Print first 5 chars
print(creditNum[:-5])                       # Print everything but last five chars

last4 = creditNum[-4:]                      # assign last four chars
print(f"Hidden: XXXX-XXXX-XXXX-{last4}")

reverse = creditNum[::-1]                   # flips the string around, reverse
print(F"Backwards: {reverse}")



# Format specifiers, changes the value based on flags = {value:flag}
price = 3.14159
price2 = -1020392.0232

print(f"Price 1 is: ${price:.2f}")      # :.#f  The digit specifies the number after the float decimal
print(f"Now it's: ${price:10}")         # :#    The line takes up 10 spaces including the string
print(f"Now it's: ${price:010}")        # :0#   Zero padded, same as above but fills in blanks with 0's
print(f"Now it's: ${price:<10}")        # :<#   Left justified
print(f"Now it's: ${price:>10}")        # :>#   Right justified
print(f"Now it's: ${price:^10}")        # :^#   Centered
print(f"Now it's: ${price:+}")          # :+    Shows the sign
print(f"Price 2 is: ${price2:+,.2f}")   # Shows the sign, sep's thousands with comma, and tw odecimal places