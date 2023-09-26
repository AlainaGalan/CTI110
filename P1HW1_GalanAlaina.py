# Alaina Galan
# 9/26/2023
# I will take 2 user inputs, add and multiply them. I will square and cube the first user input. Everything will be displayed

user_num = int(input('Enter integer:\n'))

print("You entered:", user_num)
print(user_num, "squared is", user_num**2)
print("And", user_num, "cubed is", user_num**3, "!!")

user_num2 = int(input("Enter another integer:\n"))
add = user_num + user_num2
print(user_num, "+", user_num2, "is", add)

mult = user_num * user_num2
print(user_num, "*", user_num2, "is", mult)
