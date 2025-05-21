# Performance Task: Static and Stack-Dynamic Variables

def session_counter():
    """Simulates a stack-dynamic variable (resets each call)"""
    counter = 0  # Stack-dynamic variable
    counter += 1
    print(f"Session visits: {counter}")

def kiosk_usage():
    """Simulates a static-like variable (persists between calls)"""
    if not hasattr(kiosk_usage, 'total_users'):
        kiosk_usage.total_users = 0  # Static-like variable initialization
    
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

def main():
    """Simulates three customer sessions"""
    print("=== KIOSK SYSTEM START ===")
    
    # First customer session
    print("\nCustomer 1:")
    session_counter()
    kiosk_usage()
    
    # Second customer session
    print("\nCustomer 2:")
    session_counter()
    kiosk_usage()
    
    # Third customer session
    print("\nCustomer 3:")
    session_counter()
    kiosk_usage()
    
    # Additional calls to demonstrate reset behavior (as required)
    print("\nAdditional session_counter() calls:")
    for _ in range(2):  # Called twice more (total 5 times as required)
        session_counter()
    
    print("\n=== KIOSK SYSTEM SHUTDOWN ===")

if __name__ == "__main__":
    main()