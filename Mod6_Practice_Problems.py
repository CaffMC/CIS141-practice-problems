# 1.
numbers = [1, 2, 3, 4, 5]
# Sets 'Sum' to an integer to later be added too.
Sum = 0
# Iterates through each number in the list.
for i in numbers:
    # Checks if the number is even using modulus.
    if i % 2 == 0:
        # Adds even numbers to 'Sum' to be printed. Same as 'Sum = Sum + i'
        Sum += i
# Prints result using concatenation after labeling 'sum' as a string.
print("The sum of all the even numbers is: " + str(Sum))
# 2.
# Chosen list of strings in my list.
list_of_strings = ["Olympic College is great!", "One branch of Olympic Collge is located in Shelton."]
count = 0
for string in list_of_strings:
   if "Olympic" in string:
       count += 1
print("The word 'Olympic' appears", count, "times in the list.")
# 3.
# List of strings.
strings = ["cat", "dog", "apple", "hi", "bye", "banana", "tree"]
# Create a new list for the strings longer than three characters.
filtered_strings = []
for string in strings:
    # If the string's length is longer than three, it will be appended to 'filtered_strings'
    if len(string) > 3:
        # Adds chosen strings to my empty list, 'filtered_strings'.
        filtered_strings.append(string)
print(filtered_strings)
# 4.
list_of_integers = [2, 3, 7, 9, 4, 6, 3, 7, 2]
even_int = 0
odd_int = 0
for i in list_of_integers:
    if i % 2 == 0:
        even_int += 1
    else:
        odd_int += 1
print("Even count is: " + str(even_int))
print("Odd count is: " + str(odd_int))
# 5.
list_of_integers = [2, 3, 7, 9, 4, 6, 3, 7, 2]
squared_integers = []
for i in list_of_integers:
    squared_value = i ** 2
    squared_integers.append(squared_value)
print(squared_integers)







