'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
string_input = input("Please enter a string: ")

def count_vowels(input):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in input:
        if char in vowels:
            vowel_count += 1
    return vowel_count

print("The number of vowels in the string is: ", count_vowels(string_input))
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
s = input("Please enter a string: ")
print(is_palindrome(s))
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attacker, defender):
    if (attacker, defender) == ("Water", "Fire"):
        return "Super Effective"
    elif (attacker, defender) == ("Fire", "Water"):
        return "Not Very Effective"
    elif (attacker, defender) == ("Electric", "Grass"):
        return "Neutral"
    else:
        return "Neutral"

print(type_advantage("Water", "Fire"))
print(type_advantage("Fire", "Water"))
print(type_advantage("Electric", "Grass"))

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    if age < 19:
        return 0
    elif 19 <= age <= 64:
        return 10 if not vehicle else 20
    elif age >+ 65:
        return 5 if not vehicle else 15
# examples
print(ferry_fare(25, True))
print(ferry_fare(70, False))
print(ferry_fare(10, False))
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience):
    if experience <= 99:
        return "Level 1"
    elif experience <= 199:
        return "Level 2"
    else:
        return "Level 3"

print(level_up(32))
print(level_up(159))
print(level_up(346))
