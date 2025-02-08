# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = input("Give me a word!")
repeat = int(input("How many times should I repeat your word?"))
print(word * repeat)
# 2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("What's your name?")
age = int(input("What's your age?"))
age2 = str(age + 1)
print("Hello, " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(age2) + " years old.")
# 3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Enter a sentence: ")
word_to_find = input("Enter a word to find: ")
found = word_to_find  in sentence
print(found)
# 4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word2 = input("Give me a word: ")
index1 = int(input("Give me an index: "))
index2 = int(input("Give me a second index: "))
sliced = word2[index1:index2]
print(sliced)
# 5. Print 3 words ith a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
phrase = "big red dog"
new_phrase = "|".join(phrase.split())
print(new_phrase)
