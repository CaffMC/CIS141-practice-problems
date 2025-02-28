"""
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
"""
gardening_file = open("gardening_tips.txt", "r")
gardening_contents = gardening_file.read()
gardening_file.close()
# In the instructions, it said to print the tips one by one, so I assumed this meant to
# split them into seperate sentenses and use a loop to print them one at a time...
sentences = gardening_contents.split("\n")
for sentence in sentences:
    print(sentence)
"""
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
"""
hiking_file = open("hiking_log.txt","a")

while True:
    hike_name = input("Whats this hike's name: (Press 0 to exit) ")
    if hike_name == "0":
        break
    hike_miles = input("What's the distance in miles: (Press 0 to exit) ")
    if hike_miles == "0":
        break
    hiking_file.write("Name: " + hike_name + "\t" + "Miles: " + hike_miles + "\n")

hiking_file.close()

hiking_file = open("hiking_log.txt","r")
for line in hiking_file:
    print(line.strip())

hiking_file.close()
"""
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
"""
lyrics_file = open("song_lyrics.txt", "r")
lyrics = lyrics_file.read()
lyrics_file.close()

words_to_count = []
# Uses the range function to ask the user for words 1-5 so I did not have to ask for
# five inputs indivisually and assign them to five different variables.
for count in range(5):
    word = input(f"Enter word {count + 1} to count:")
    words_to_count.append(word)

word_counts = {}

for word in words_to_count:
    word_counts[word] = lyrics.count(word)

print("Word Counts:", word_counts)
"""
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
"""
yea_count = 0
nay_count = 0

poll_file = open("poll.txt", 'r')
poll_file_content = poll_file.read()
poll_file.close()

yea_count = poll_file_content.count('yea')
nay_count = poll_file_content.count('nay')

print('Yea votes:', yea_count)
print('Nay votes:', nay_count)
