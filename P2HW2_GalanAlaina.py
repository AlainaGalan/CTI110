# CTI-110
# P2HW2 - List
# Alaina Galan

# Declare Float mod1, mod2, mod3, mod4, mod5, mod6
# Display "Grade for Module 1...2...3..."
mod1 = float(input("Grade for Module 1: "))
mod2 = float(input("Grade for Module 2: "))
mod3 = float(input("Grade for Module 3: "))
mod4 = float(input("Grade for Module 4: "))
mod5 = float(input("Grade for Module 5: "))
mod6 = float(input("Grade for Module 6: "))
print() # Display a blank space
# Creates a list that is filled with the users input
test = [mod1, mod2, mod3, mod4, mod5, mod6]

print("-"*12,"Results", "-"*12) # Display "-"times 12, "Results", "-"times 12
print("Lowest Grade:", end="\t") # Display "Lowest Grade:", connects next print statement and uses tab to give it space
print(min(test)) # Display minimum test value from list
print("Highest Grade:", end="\t") # Display "Highest Grade:", connects next print statement and uses tab to give it space
print(max(test)) # Display maximum test value from list
print("Sum of Grades:", end="\t") # Display "Sum of Grades:", connects next print statement and uses tab to give it space
print(sum(test)) # Display the sum  of all values in test list
print("Average:", end="\t") # Display "Average:", connects next print statement and uses tab to give it space
print(round((sum(test)/6), 2)) # Display the sum of test and divides it by 6 to get the average. Round average to nearest tenth
print("-"*40) # Display "-" times 40
