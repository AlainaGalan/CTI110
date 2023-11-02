

list = ["Hours Worked", "Pay Rate", "Overtime", "OverTime Pay", "RegHour Pay", "Gross Pay"]
count = 0
overtimeTotal = 0
normTotal = 0
totalPaid = 0

while True:
    print("")
    employee = input("Enter the name of employee or type Done: ")
    if employee != "Done":
        hours = float(input("Enter the number of hours employee worked this week: "))
        # Get payrate per hour from user
        payRate = float(input("Enter employee's hourly pay rate: "))
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
        overtimeTotal = overtimeTotal + amountOwed
        normTotal = normTotal + normalTotal
        totalPaid = totalPaid + grosspay
        count += 1
    else:
        print("")
        print("Total number of emplyees entered:", count)
        print("Total amount paid for overtime:" "${:.2f}".format(overtimeTotal))
        print("Total amount paid for regular hours:", "${:.2f}".format(normTotal))
        print("Total amount paid in gross:", "${:.2f}".format(totalPaid))
        break
    if hours > 40:
        print("Employee name:", employee)
        print("")
        print("\t\t".join(list))
        print("-"*150)
        print(hours, "\t\t\t", payRate, "\t\t\t", overtime, "\t\t\t", "${:.2f}".format(amountOwed),"\t\t", "${:.2f}".format(normalTotal), "\t\t", '${:.2f}'.format(grosspay))
    else:
        print("Employee name:", employee)
        print("")
        print("\t\t".join(list))
        print("-"*150)
        print(hours, "\t\t\t", payRate, "\t\t\t", overtime, "\t\t\t", "${:.2f}".format(amountOwed),"\t\t\t", "${:.2f}".format(normalTotal), "\t\t", '${:.2f}'.format(normalTotal))
    
