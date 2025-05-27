import math

print("----------------------------------------------------")
print("Welcome to Ashton's Calculator")
print("Options are +, -, *, %, abs() (a), and sqrt() (s)")

val1 = float(input("Enter the first value: "))
val2 = input("Enter the second value: ('NA' for abs and sqrt) ")

if val2 != "NA":
    val2 = float(val2)

operator = input("Enter op: (+, -, *, %, a, or s) ")

if operator == "a":
    result = abs(val1)
    print(f"Absoulte value of {val1} is {result:.2f}")
elif operator == "s":
    result = math.sqrt(val1)
    print(f"The square root of {val1} is {result:.2f}")
else:
    if operator == "+":
        result = val1 + val2
        print(f"{val1} {operator} {val2} equals {result}")
    elif operator == "-":
        result = val1 - val2
        print(f"{val1} {operator} {val2} equals {result}")
    elif operator == "*":
        result = val1 * val2
        print(f"{val1} {operator} {val2} equals {result}")
    elif operator == "%":
        result = val1 / val2
        print(f"{val1} {operator} {val2} equals {result}")
    else:
        print("Not a valid input of some kind")

print("----------------------------------------------------")
