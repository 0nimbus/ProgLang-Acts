# Travel Time Calculator
# This program calculates the travel time based on distance and speed.
# It also checks if a rest stop is needed based on the travel time.

# Get trip details (string inputs)
starting_location = input("Enter starting location: ")
destination = input("Enter destination: ")
mode_of_transport = input("Enter mode of transport: ")

# Get numerical inputs (float)
distance = float(input("Enter distance in kilometers: "))
speed = float(input("Enter speed in km/h: "))

# Calculate travel time
travel_time = distance / speed

# Determine if rest stop is needed (boolean)
needs_rest = travel_time > 5

# Display results
print("\n--- Travel Details ---")
print(f"From: {starting_location}")
print(f"To: {destination}")
print(f"Mode: {mode_of_transport}")
print(f"Distance: {distance} km")
print(f"Speed: {speed} km/h")
print(f"\nEstimated Travel Time: {travel_time:.2f} hours")

# Warning if travel time is long
if needs_rest:
    print("\nWARNING: This trip will take more than 5 hours.")
    print("Recommendation: Plan for rest stops during your journey.")
else:
    print("\nThis trip duration is within recommended limits.")