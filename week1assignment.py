# Basic Calculator Program

def calculate(num1, num2, operation):
    """Perform the specified operation on the two numbers and return the result."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Calculate and display the result
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")
    
except ValueError:
    print("Error: Please ent