def perform_operation(num1: float, num2: float, operation: str) -> float:
    """Perform basic arithmetic operations."""
    operation = operation.lower()
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return float('nan')  # Return NaN for division by zero
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'.")
