def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    Supported operations: '+', '-', '*', '/'
    
    Args:
        num1 (float/int): First operand
        num2 (float/int): Second operand
        operation (str): The arithmetic operation to perform
    
    Returns:
        float/int: Result of the operation
    
    Raises:
        ValueError: If operation is invalid or division by zero occurs
    """
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Use '+', '-', '*', or '/'")

def add(num1, num2):
    """Returns the sum of num1 and num2."""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference between num1 and num2."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of num1 and num2."""
    return num1 * num2

# Example test cases (optional)
if __name__ == "__main__":
    print(perform_operation(10, 2, '+'))  # 12
    print(perform_operation(10, 2, '-'))  # 8
    print(perform_operation(10, 2, '*'))  # 20
    print(perform_operation(10, 2, '/'))  # 5.0
    try:
        print(perform_operation(10, 0, '/'))  # Raises ValueError
    except ValueError as e:
        print(e)