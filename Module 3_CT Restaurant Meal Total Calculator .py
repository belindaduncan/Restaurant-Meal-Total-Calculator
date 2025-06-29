# Module 3: Critical Thinking Assignment
# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.

# Part 1: Restaurant Meal Total Calculator

# Simple menu: 

menu = {
    1: ("Hamburger", 5.99),
    2: ("Hot Dog", 3.49),
    3: ("BLT", 4.79),
    4: ("Fries", 2.29),
    5: ("Drink", 1.99)
}

# Display the menu: (loop through the menu dictionary, there is an invisible /n after each item) the loop will show the menu items in a nice user friendly format. 
print("Menu:")
for key, (item, price) in menu.items():
    print(f"{key}: {item} - ${price:.2f}")

# Get the charge for the food items ordered (waitress input) 
ordered_items = (input("Enter the food item/s orders (separate with a comma): "))

item_numbers = [int(num.strip()) for num in ordered_items.split(",")]

# can not use int(input()) directly as it may raise ValueError if input is not a number due 
# to input needed to be separated by commas. 

charges = []

# Add each food item price to the charges list via loop
for num in item_numbers:
    if num in menu:
        charges.append(menu[num][1])
    else:
        print(f"Item {num} does not exist.")

food_charge = sum(charges)
    
# Calculate tip and tax
tip = food_charge * 0.18
tax = food_charge * 0.07

# Calculate total
total = food_charge + tip + tax

# Display the results
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%):   ${tip:.2f}")
print(f"Tax (7%):    ${tax:.2f}")
print(f"Total:       ${total:.2f}")
print("Thank you, come again. Have a nice day!")