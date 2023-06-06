"""Prompt the user to enter a boolean value (True/False)"""
VAR = input("Enter a boolean value (True/False): ")
# Convert input to lowercase
VAR = VAR.lower()
# Convert the input to a boolean value
if VAR == "true":
    VAR = True
else:
    IVAR = False

# Convert the boolean value to an integer
CONVERT_VALUE= int(VAR)

# Print the converted value
print("Converted value:", CONVERT_VALUE)
