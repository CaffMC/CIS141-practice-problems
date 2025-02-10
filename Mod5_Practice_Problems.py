# 1.
n = int(input("Enter a positive integer: "))
sum = 0
current_int = 1
while current_int <= n:
    sum += current_int
    current_int += 1
print("The sum of all integers from 1 to " + str(n) + " is: " + str(sum))
# 2.
string = "Coffee Cup"
for char in string:
    print(char.upper())
# 3.
for numbers in range(2, 21, 2):
    print(numbers)
# 4.
for i in range(5):
    for j in range(5):
        print(str(i + 1) + "/t", end='')
    print("")
# 5.
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("Exiting...")
        break
    print("You entered " + str(number))

