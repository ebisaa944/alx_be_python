from datetime import datetime, timedelta

def display_current_datetime() -> datetime:
    """Display current date and time."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(days: int) -> datetime:
    """Calculate and display future date."""
    future_date = datetime.now() + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    """Main function to demonstrate datetime operations."""
    # Part 1: Display current datetime
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("\nEnter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Error: Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()
