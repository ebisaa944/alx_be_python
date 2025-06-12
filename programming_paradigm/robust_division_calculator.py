def safe_divide(numerator, denominator):
    """
    Performs division with comprehensive error handling.
    
    Args:
        numerator: The numerator (expected as string from command line)
        denominator: The denominator (expected as string from command line)
        
    Returns:
        float: Result of division if successful
        str: Error message if division fails
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return result
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
