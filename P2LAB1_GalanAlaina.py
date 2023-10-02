# Alaina Galan
# Oct 2, 2023

milesPerGallon = float(input("Type miles per gallon: "))
dollarsPerGallon = float(input("Type dollars per gallon: "))

cost20 = 20 * dollarsPerGallon/milesPerGallon
cost75 = 75 * dollarsPerGallon/milesPerGallon
cost500 = 500 * dollarsPerGallon/milesPerGallon

print(f'{cost20:.2f} {cost75:.2f} {cost500:.2f}')
