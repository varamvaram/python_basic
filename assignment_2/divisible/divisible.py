def check_divisibility():
    """
    Check the divisibility of one number by another number.
    This function prompts the user to enter two numbers and checks if the first number
    is divisible by the second number. It returns a string indicating the divisibility result.
    A string indicating whether the first number is divisible by the second number or not.
    """
# Get user input for the numbers
    num = int(input("Enter the first number: "))
    divisor = int(input("Enter the second number: "))

    # Check if the first number is divisible by the second number
    if num % divisor == 0:
        result = f"{num} is divisible by {divisor}."
    else:
        result = f"{num} is not divisible by {divisor}."

    return result

# Call the function to test it
divisibility_result = check_divisibility()
print(divisibility_result)
