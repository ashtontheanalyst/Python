import math     # for advanced math functionality

# Basic math and functionality built in
friends = 0
friends =+ 1
friends -= 3
friends *= 10
friends = float(friends) / 2.3
friends = int(30)

remainder = friends % 4     # gives us the remainder, using the modulous (good for finding even or odd num)

print(friends)
print(type(friends))

print()
print(remainder)



# built in functions
x = 3.14
y = -4
z = 5

result = round(x)
result = abs(y)
result = pow(z, 3)         # number to the something power
result = max(x, y, z)      # returns the max of a set
result = min(x, y, z)      # same but the min

print()
print(result)



# Things past here may need the MATH MODULE, as seen from the import at top of page
print()
print(math.pi)             # similar to in C++, we use the library.something to get the func
print(int(math.sqrt(25)))  # find the sqrt of 25 and cast to an int
