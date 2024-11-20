# Asking for user input (name)
name = input("Hello user! Please enter your name:\n").title()
message = f'Hello {name}, welcome to this'
print(message)

# Asking user for destination choice
destination = input("Where do you want to go? (mountain / beach): ").strip().lower()

if destination == "mountain":
    print("You have selected the mountain.")
elif destination == "beach":
    print("You have selected the beach.")
else:
    print("You have not selected any known destination.")

# Asking user for budget and number of days
budget = int(input("Enter your budget: "))
days = int(input("How many days will you be staying? "))

# Determine the type of trip based on the budget
if budget >= 500:
    print("Luxury trip!")
elif budget >= 200:
    print("Good trip!")
elif budget > 0:
    print("Budget-friendly trip!")
else:
    print("Invalid budget.")

# Function to calculate total cost
def total_cost(budget, days):
    return budget * days

# Calculate the total cost
total_cost_value = total_cost(budget, days)

# Displaying the details to the user
print(f'''Days: {days}
Budget: {budget}
Total cost: {total_cost_value}''')
