# CTI-110
# Alaina Galan
# P4HW1 - Score List
# 10/31/23
# grade list loop


# create 6 variables bassed off the user's input
num_grades = int(input("How many grades would you like to enter? "))
# Create empty list
grade_list = []


for grade in range(num_grades):
    this_grade = int(input("Enter a grade: "))
    
    while this_grade < 0 or this_grade > 100:
        print("invalid grade entered.")
        this_grade = int(input("Enter a grade: "))
        
    grade_list.append(this_grade)
    print(f"{this_grade} has been added to the list")
for grade in grade_list:
    print(grade)

print("-"*12,"Results", "-"*12) # Display "-"times 12, "Results", "-"times 12
print("Lowest Grade:", end="\t") # Display "Lowest Grade:", connects next print statement and uses tab to give it space
print(min(grade_list)) # Display minimum test value from list
print("Highest Grade:", end="\t") # Display "Highest Grade:", connects next print statement and uses tab to give it space
print(max(grade_list)) # Display maximum test value from list
print("Sum of Grades:", end="\t") # Display "Sum of Grades:", connects next print statement and uses tab to give it space
print(sum(grade_list)) # Display the sum of all values in test list
print("Average:", end="\t\t") # Display "Average:", connects next print statement and uses tab to give it space
print(f"{sum(grade_list)/num_grades:.2f}") # Display the sum of test and divides it by 6 to get the average. Round average to nearest tenth

