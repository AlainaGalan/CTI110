# CTI-110
# Alaina Galan
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
# make sure there are no unexpected indents. If there is there will be an indentation error
# make sure you have user input for each module
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: ')) 
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
# make sure each mod in the list is seperated by a comma & have all the modules in your list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades) # make sure grades is not Grades
high = max(grades) # for the highest value you would use max
sum = sum(grades)
avg = sum / 6 

# determine letter grade for average
print("-"*40, "Results", "-" *20)
print("Lowest grade:", end="\t")
print(low)
print("Highest grade:", end="\t")
print(high)
print("Sum of grades:", end="\t")
print(sum)
print('Average:', end="\t")
print(f'{avg:.2f}')
print("-"*80)

if avg >= 90:
    print('Your grade is: A') # make sure there is indentation 
else:
    if avg > 80:
        print('Your grade is: B')
    else:
        if avg > 70:
            print("Your grade is: C")
        else:
            if avg > 60:
                print("Your grade is: D")
            else:
                if avg > 50:
                    print("Your grade is: D")
                else:
                    print('Your grade is: F') # TO DO: finish this
