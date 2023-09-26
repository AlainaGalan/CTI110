# Alaina Galan
# 9/26/2023
# This program calculates and displays travel expenses

budget = int(input("Enter your budget: ")) 
travel = input("Enter your travel destination: ")
gas = int(input("How much do you think you'll spend on gas: "))
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

#This will display the results
def display():# I just added this so it's easier for me to format the design and it looks nicer!
    print("\n")
    print("-"*20, "Travel Expenses", "-"*20)

display() # Display the user inputs
print("Location: ", travel)
print("Initial Budget: ", budget,"\n")
print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food,"\n")

#add the expenses
expenses = gas + accomodation + food
remaining = budget - expenses # subtract the expenses from the budget the user gave
print("Remaining Balance: ", remaining) # display remaining balance
