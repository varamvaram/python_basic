"""
Prompts the user to enter a list of numbers, finds the maximum and minimum values,
and returns them as a tuple.
Returns:
A tuple containing the maximum and minimum values.
"""
def find_max_min():
    # Prompt the user to enter a list of numbers
    num_list = input("Enter a list of numbers: ").split()
    # Convert the input values to integers
    num_list = [int(num) for num in num_list]
    # Find the maximum and minimum values
    max_value = max(num_list)
    min_value = min(num_list)
    # Return the maximum and minimum values as a tuple
    return max_value, min_value
# Call the function and store the result
result = find_max_min()
# Print the maximum and minimum values
print("Maximum value:", result[0])
print("Minimum value:", result[1])
