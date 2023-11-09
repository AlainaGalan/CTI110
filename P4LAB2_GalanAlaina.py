number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number1 <= number2:
    while number1 <= number2:
        print(number1, end=" ")
        number1 += 5
else:
    print("Second integer can't be less than the first.")

# For loop

print("")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
if number1 <= number2:
    for item in range(number1, number2 + 1,5):
        print(item)
            
else:
    while number1 > number2:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        for item in range(number1, number2 + 1,5):
            print(item)

  

        
    
    
