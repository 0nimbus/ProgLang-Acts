# Task B: Number Checker
def number_checker():
    """Determines if a number is positive, negative, or zero"""
    try:
        num = int(input("Enter an integer: "))
        
        if num > 0:
            print(f"{num} is POSITIVE")
        elif num < 0:
            print(f"{num} is NEGATIVE")
        else:
            print("The number is ZERO")
    
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Execute Task B
print("\n--- TASK B: NUMBER CHECKER ---")
number_checker()