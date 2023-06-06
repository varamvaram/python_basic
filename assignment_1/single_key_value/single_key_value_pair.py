"""samlpe dictionary """
SAMPLE_DICT = {'name': 'John Doe', 'age': 25, 'city': 'New York'}
# selected key
SELECTED_KEY = 'age'

# Extract the key-value pair
SELECTED_KEY_VALUE = SAMPLE_DICT.get(SELECTED_KEY)

# Print the selected key and its corresponding value
print("Selected key:", SELECTED_KEY)
print("Corresponding value:", SELECTED_KEY_VALUE)
