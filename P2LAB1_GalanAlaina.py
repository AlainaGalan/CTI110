# Alaina Galan
# Oct 2, 2023
# Use floats and expressions to calcukate gas cost

#create input variables
milesPerGallon = float(input("Type miles per gallon: "))
dollarsPerGallon = float(input("Type dollars per gallon: "))

#Calculate gas cost based off gallons needed & price per gallon
#Calculate for 20miles, 75miles, 500 miles
cost20 = (20/milesPerGallon) * dollarsPerGallon
cost75 = (75/milesPerGallon) * dollarsPerGallon
cost500 = (500/milesPerGallon) * dollarsPerGallon

#Ouput values using f'string & format floats
print(f'{cost20:.2f} {cost75:.2f} {cost500:.2f}')
