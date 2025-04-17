# Birthday Celebration Budget Calculator

# Step 1: Get user input for each expense category
print("=== Birthday Celebration Budget Calculator ===")
print("Please enter estimated costs for each category:")

venue = float(input("Venue cost: $"))
catering = float(input("Catering cost: $"))
decorations = float(input("Decorations cost: $"))
entertainment = float(input("Entertainment cost: $"))
miscellaneous = float(input("Miscellaneous costs: $"))

# Step 2: Calculate total estimated cost
total_cost = 0.0
total_cost += venue
total_cost += catering
total_cost += decorations
total_cost += entertainment
total_cost += miscellaneous

# Step 3: Define budget and compare with total cost
budget = 2000.00  # Predefined budget
within_budget = total_cost <= budget

# Step 4: Print results
print("\n=== Budget Summary ===")
print(f"Total Estimated Cost: ${total_cost:.2f}")

# Step 5: Display budget status
if within_budget:
    print(f"Status: Within budget (Budget: ${budget:.2f})")
else:
    print(f"Status: Over budget by ${total_cost - budget:.2f} (Budget: ${budget:.2f})")