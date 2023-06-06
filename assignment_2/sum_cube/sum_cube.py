"""
Function to calculate the sum of the cubes of positive integers smaller than a specified number.
Args:n: A positive integer.
Returns:The sum of the cubes of positive integers smaller than the specified number.
"""
def sum_of_cubes():
    number = int(input("Enter a positive integer: "))  # Get user input
    # Validate input
    if number <= 0:
        print("Invalid input. Please enter a positive integer.")
        return None
    # Calculate sum of cubes using a generator expression
    sum_cubes = sum(i ** 3 for i in range(1, number))
    return sum_cubes
# Call the function and print the result
result = sum_of_cubes()
print("Sum of cubes:", result)
