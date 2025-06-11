import math
# Finds the area of a triangle based on user input

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = 0.5 * length * width
# The :.#f specifies the amount of decimal points to show
print(f"The area of a {length:.3f} x {width:.3f} triangle is {area:.3f}")


# Hypotenuse using some functionality from the math module
hyp = math.sqrt(pow(length, 2) + pow(width, 2))
print(f"The hypotenuse is: {hyp:.3f}")