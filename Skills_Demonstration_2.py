import math
import statistics
# 1. Create a program that prints the following output to the screen:
# "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony.
# Then, everything changed when the Fire Nation attacked."

print("""Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony.
Then, everything changed when the Fire Nation attacked.""")

# 2. Create a program that prompts for 2 numbers and then outputs the addition,
# subtraction, multiplication, and division of the first number by the second number.

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print(x + y, x - y, x * y, x / y)

# 3. Create a program that prompts for the side lengths of a triangle and computes
# the area using Heron's formula.(https://en.wikipedia.org/wiki/Heron%27s_formula)

a = int(input("Enter first side: "))
# Would use "float(input" to allow integers...
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(f"The area of the triangle is: {area}")
    # Wanted to inlay the area inside the text, thus the "f" and "{area}".
else:
    print("The numbers inputed do not make a valid triangle. Please check that a + b > c, a + c > b, and b + c > a.")
    # Wanted something to show in case the inputed numbers were invalid.

# 4. Create a program that computes different statistics given five numbers including the total
# average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))
e = int(input("Enter fifth number:"))

average_value = (a + b + c + d + e) / 5
min_value = min(a, b, c, d, e)
max_value = max(a, b, c, d, e)
range_value = max_value - min_value
# I imported statistics to make the standard deviation calculation super simple.
numbers = (a, b, c, d, e)
standard_value = statistics.stdev(numbers)

print(average_value, min_value, max_value, range_value, standard_value)
