"""
Open the file in read mode
Initialize a variable to count the words
Read each line of the file
"""
WORD_COUNT= 0
with open("PYTHON.txt", "r", encoding="utf-8") as file:
    content = file.read()
    words = content.split(" ")
    word_count = len(words)

print("Number of words:", word_count)
