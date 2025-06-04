# Conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def display_menu():
    """Display temperature conversion menu"""
    print("\nTemperature Conversion Tool")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

def get_conversion_choice():
    """Get user's conversion choice"""
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number")

def get_temperature_input():
    """Get temperature value from user"""
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            return temp
        except ValueError:
            print("Please enter a valid number")

def get_temperature_scale():
    """Get temperature scale from user"""
    while True:
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if scale in ('C', 'F'):
            return scale
        print("Please enter 'C' or 'F'")

def main():
    while True:
        display_menu()
        choice = get_conversion_choice()
        
        if choice == 1:
            temp = get_temperature_input()
            scale = get_temperature_scale()
            if scale == 'C':
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result:.2f}°F")
            else:
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result:.2f}°C")
        
        elif choice == 2:
            temp = get_temperature_input()
            scale = get_temperature_scale()
            if scale == 'F':
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F = {result:.2f}°C")
            else:
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C = {result:.2f}°F")
        
        elif choice == 3:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()