# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
CELSIUS_OFFSET = 32

def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_OFFSET

def main():
    """Main function for temperature conversion."""
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        if unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted:.2f}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted:.2f}°F")
        else:
            print("Error: Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
