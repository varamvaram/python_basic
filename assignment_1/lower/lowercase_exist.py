"""
Check if a given string contains lowercase letters.
string : The input string to check.
bool: True if lowercase letters exist, False otherwise.
"""
string_1 = input("Enter a string: ")
LOWERCASE_EXIST = False
for char in string_1:
    if char.islower():
        LOWERCASE_EXIST = True
        break
print("Lowercase letters exist in the string:", LOWERCASE_EXIST)
