# Alaina Galan
# 10/3/2023
# Dictionary that recieves user input on attributes then displays them in a sentence.

name = input("Enter your first name: ").title() # .title() capitilizes the first letter of the users input
hair = input("What is your hair color: ").lower() # .lower() makes every letter lowercase no matter what the user inputs
eye = input("What is your eye color: ").lower()
height = float(input("How tall are you: "))
age = int(input("What is your age: "))
food = input("What is your favorite food: ").lower()

user_traits = {"name":name, # this is a dictionary that will get user traits from the input above and add it to the dictionary
               "hair":hair,
               "eye":eye ,
               "height":height,
               "age":age,
               "food": food}

print() # just adds a space to make it look better
# I utilize the f sring so I can put these expressions in them
print(f'{user_traits["name"]} is a {user_traits["height"]}' + "'", f'tall student with {user_traits["hair"]} hair and {user_traits["eye"]} eyes. They are {user_traits["age"]} years old and their favorite food is {user_traits["food"]}.')
