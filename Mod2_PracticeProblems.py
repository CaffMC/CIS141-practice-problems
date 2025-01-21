import math
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

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("The area of the triangle is:")
print(area)

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
numbers = (a, b, c, d, e)
Standard_a = ((a - average_value) ** 2)
Standard_b = ((b - average_value) ** 2)
Standard_c = ((c - average_value) ** 2)
Standard_d = ((d - average_value) ** 2)
Standard_e = ((e - average_value) ** 2)
Sum_of_sqrt_dif = Standard_a + Standard_b + Standard_c + Standard_d + Standard_e
standard_value = math.sqrt(Sum_of_sqrt_dif / 5)
print(average_value, min_value, max_value, range_value, standard_value)
