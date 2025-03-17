def factorial(n):
    # Initialize the result to 1
    result = 1
    
    # Use a for loop to calculate the factorial
    for i in range(2, n + 1):
        result *= i
    
    return result

# Test the function
number = int(input("Enter a number to calculate its factorial: "))
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
