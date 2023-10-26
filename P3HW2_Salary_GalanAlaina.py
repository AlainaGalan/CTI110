# CTI-110
#P3HW2 - Salary
# Alaina Galan
# Oct 26, 2023
# Uses if/3lse statements to calculate employees gross pay

# Get employee name from user
employee = input("Enter the name of employee: ")
# Get number of hours from user
hours = float(input("Enter the number of hours employee worked this week: "))
# Get payrate per hour from user
payRate = float(input("Enter employee's hourly pay rate: "))
# displays lines for design
print("-"*40)
# Displays employee's name
print("Employee name:", employee)
print("")

# I chose to do the math inside of the if statements
# Determine if employee worked more than 40 hours
if hours > 40:
    # calculates how many hours overtime
    overtime = hours - 40
    # calculates overtime payrate based on normal payrate
    amount = payRate * 1.5
    # calculates amount owed for overtime hours. does overtime hours times the overtime payrate
    amountOwed = overtime * amount
    # calculates the normal hours the employee worked without overtime 
    normalHours = hours - overtime
    # calculates normal payrate of employee without overtime hours
    normalTotal = normalHours * payRate
    # calculates grosspay of employee, adds overtime pay and normal pay
    grosspay = amountOwed + normalTotal
    # displays the menu
    list = ["Hours Worked", "Pay Rate", "Overtime", "OverTime Pay", "RegHour Pay", "Gross Pay"]
    print("\t\t".join(list))
    print("-"*100)
    print(hours, "\t\t\t\t", payRate, "\t\t\t", overtime, "\t\t\t", "${:,.2f}".format(amountOwed),"\t\t\t", "${:,.2f}".format(normalTotal), "\t\t", '${:,.2f}'.format(grosspay))
    
else:
    # calculates normal payrate of employee
    regularHours = hours * payRate
    # displays the menu
    list = ["Hours Worked", "Pay Rate", "Overtime", "OverTime Pay", "RegHour Pay", "Gross Pay"]
    print("\t\t".join(list))
    print("-"*100)
    print(hours, "\t\t\t\t", payRate, "\t\t\t", "0.0", "\t\t\t", "$0.0" ,"\t\t\t\t", "${:,.2f}".format(regularHours), "\t\t", '${:,.2f}'.format(regularHours))
