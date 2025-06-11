# Using the math module and basic python to get circum and more of a circle
import math

radius = float(input("Please state the radius of the circle (cm): "))

circum = 2 * math.pi * radius
print(f"\nCircumference:    {circum:.2f} cm")

area = math.pi * (pow(radius, 2))
print(f"Area:             {area:.2f} cm^2")
