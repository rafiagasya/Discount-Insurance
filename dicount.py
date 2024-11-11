# Create a discount program
# Ask the user which type of trip they are taking
# Ask the user for an expected trip cost

cost = int(input("Enter your trip funds:"))

if cost < 450:
    print("Go on a stay-cation!")
if cost >= 450 and cost < 35000:
    print("Go on a road flight")
if cost >= 35000:
    print("Pack your book for learn ") 
print("Nice Trip!") 

# Note what is the price variable !
# If you want to make variable A-B
# How much cost you make variable

bag_weight = int(input("Enter weight in KG: "))
destination = input("Enter domestic or internasional: ")

if bag_weight <= 19:
    price = 35
else:
    price = 80
    
if destination == "domestic":
    price = price + 300
elif destination == "internasional":
    price += 650
else:
    print("Spelling error!")

print("Ticket Price:, 14000")

# Continue with calculating the final ticket price based on inputs and conditions
# Assume the base cost is 'price' plus any additional costs for bag weight and trip cost

# Calculate the final ticket price based on user input
final_price = cost + price  # total ticket price based on trip cost and bag weight adjustments

# Show the results to the user
print("\n----- Trip Details -----")
print(f"Base Trip Cost: ${cost}")
print(f"Bag Weight Charge: ${price - 35 if bag_weight > 19 else 0}")  # shows only the extra charge
print(f"Destination Charge: ${300 if destination == 'domestic' else 650 if destination == 'international' else 0}")

# Check for any spelling errors or unhandled input errors
if destination not in ["domestic", "international"]:
    print("Spelling error detected in destination input!")

# Show final price
print("\nTotal Ticket Price:", final_price)

# Ask if user wants to add any other services
add_meal = input("\nWould you like to add a meal for an additional $50? (yes or no): ")
if add_meal.lower() == "yes":
    final_price += 50
    print("Meal service added. Total updated.")

# Option for insurance
add_insurance = input("\nWould you like to add travel insurance for $100? (yes or no): ")
if add_insurance.lower() == "yes":
    final_price += 100
    print("Travel insurance added. Total updated.")
    
# Option For Cars
add_cars = input("\nWould you like to add a cars for trip an price $350 (yes or no): ")
if add_cars.lower() == "yes":
    final_price += 200
    print("Trip cars added. Total updated.")

# Display the final summary and price
print("\n----- Final Ticket Summary -----")
print(f"Final Ticket Price: ${final_price}")
print("Thank you for using our ticketing service!")


