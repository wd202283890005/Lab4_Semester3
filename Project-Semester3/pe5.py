def factorial(n):
    # Initialize the result to 1
    result = 1
    
    # Use a while loop to calculate the factorial
    while n > 1:
        result *= n
        n -= 1
    
    return result

# Test the function
number = int(input("Enter a number to calculate its factorial: "))
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
