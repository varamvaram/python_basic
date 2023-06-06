"""Check if the value is a list
   Check if the value is a set
   Check if the value is a tuple
"""
value= [4, 5, 6, 7]
if isinstance(value, list):
    print("value is a list")

if isinstance(value, set):
    print("value is a set")

if isinstance(value, tuple):
    print("value is a tuple")
