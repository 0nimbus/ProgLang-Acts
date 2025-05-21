# Task C: Password Checker
def password_checker():
    """Repeatedly asks for a password until correct"""
    correct_password = "default123"
    
    while True:
        user_input = input("Enter password: ")
        if user_input == correct_password:
            print("Access granted!")
            break
        else:
            print("Incorrect password. Try again.")

# Execute Task C
print("\n--- TASK C: PASSWORD CHECKER ---")
password_checker()