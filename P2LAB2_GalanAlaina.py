# Alaina Galan
# Oct 2, 2023
# Get the average and product of user input using float. Display using the f'

# Gets user input using datatype float
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
num3 = float(input("Enter number: "))
num4 = float(input("Enter number: "))

# Sets variable product to get the product and the variable avg to get the average
product= num1 * num2 * num3 * num4
avg = (num1 +num2 + num3 + num4) /4

# Prints out the product and average rounding it to the nearest whole number
print(f'{product:.0f} {avg:.0f}')
# Prints out the product and average and also shows three values after the decimal point
print(f'{product:.3f} {avg:.3f}')
