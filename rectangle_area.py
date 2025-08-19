"""This is a simple calulator that will find the area of a rectangle.
Input numbers must be greater than 0.
"""
length = float(input("Enter the length. "))#This is where the user is prompted to input the length
width = float(input("Enter the width. "))#This is where the user is porpmted to input the width
area = length*width
if length <= 0:
    print("The length can't be 0 or smaller, try again.")
elif width <= 0:
    print("The width can't be 0 or smaller, try again.")
else:
    print(f"The area of the rectangle is: {area}.")
#The print function should display the entered lenght and width as well as the area.
