""" 
'is' is added infront of the string
if already present is un changed the string 
"""
CHECK=input("Enter The String:")
WORD="is"
if WORD in CHECK:
    print(CHECK)
else:
    print(WORD,CHECK)
    