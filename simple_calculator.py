def calculator():
    operators_count = {'+': 0, '-': 0, '*': 0, '/': 0, '**': 0}
    
    print("Simple Calculator: Supported operations are +, -, *, /, **")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, **): ")
            num2 = float(input("Enter second number: "))
            
            if operator == '+':
                result = num1 + num2
                operators_count['+'] += 1
            elif operator == '-':
                result = num1 - num2
                operators_count['-'] += 1
            elif operator == '*':
                result = num1 * num2
                operators_count['*'] += 1
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operators_count['/'] += 1
            elif operator == '**':
                result = num1 ** num2
                operators_count['**'] += 1
            else:
                print("Invalid operator. Please use one of the following: +, -, *, /, **")
                continue
            
            print(f"Result: {result}")
            
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue
        
        more_calculations = input("Do you want to perform another calculation? (yes/no): ").lower()
        if more_calculations != 'yes':
            break
    
    print("\nOperator Usage Count:")
    for op, count in operators_count.items():
        print(f"{op}: {count} times")

# Run the calculator function
if __name__ == "__main__":
    calculator()
