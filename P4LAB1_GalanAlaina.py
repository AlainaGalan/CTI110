#P4LAB1a
import turtle

length = int(input("What length do you want your square to be? "))
squareSides = 4
# while loop
while squareSides != 0:
    turtle.forward(length)
    turtle.left(90)
    squareSides -= 1

turtle.color("red")    
# for loop
for square in range(4):
    turtle.forward(length)
    turtle.left(90)

    
