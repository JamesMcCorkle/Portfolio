"""This program is menu driven.
When you run this program you will be asked to enter a letter to choose
what you want the program to do.
There are several options to choose from. To exit, enter the corresponding letter."""

import secrets
import string
from datetime import datetime
import math

def generate_secure_password(length=12):
    """Generate a secure password."""
    if length < 6:
        length = 12  #Defaults to 12 if chosen length is not in range 6-12
    while True:#While loop to ensure at least one of each required character type is included
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
        if (any(c.islower() for c in password) and #Check for at least one uppercase letter, one lowercase letter, one digit, and one special character
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            break

    return password

def calculate_percentage(numerator, denominator):
    """Calculate and format a percentage."""
    if denominator == 0:
        return "Denominator cannot be zero."
    percentage = (numerator / denominator) * 100
    return f"{percentage:.2f}%" #Format the percentage to hundredths

def days_until_date(target_date):
    """Calculate the number of days from today until the target date(does not include today in count)."""
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)#Sets the time to 12 am so that the count is correct
    future_date = datetime.strptime(target_date, "%Y-%m-%d")
    days_until = future_date - today
    return days_until.days #Had to include .days so that the output would stop outputing the time as well

def law_of_cosines(a, b, angle_degrees):
    """Calculate the third leg of a triangle using the Law of Cosines."""
    angle_radians = math.radians(angle_degrees)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_radians))#This is the formula for the law of cosines
    return f"{c:.2f}"#Returns C(answer) formated to the second decimal

def volume_of_cylinder(radius, height):
    """Calculate the volume of a right circular cylinder."""
    volume = math.pi * radius**2 * height#Formula for volume of a cylinder
    return f"{volume:.2f}"#Formatted to the second decimal

def main():
    """Main function to display menu-driven program"""
    while True:
        print("\nMenu:")
        print("a. Generate a Secure Password")
        print("b. Calculate a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Law of Cosines to calculate the leg of a triangle.")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'a':
            try:
                length = int(input("Enter the length of the password(6-12 chars): "))#Ask user for length of password to generate
                print(f"Generated Password: {generate_secure_password(length)}")
            except ValueError:
                print("Invalid input. Enter a number.")#Incase user enters a letter

        elif choice == 'b':
            try:
                numerator = float(input("Enter the numerator(Ex: 3.14): "))
                denominator = float(input("Enter the denominator(Ex: 5.57): "))#Must be bigger than and not 0
                print(f"Percentage: {calculate_percentage(numerator, denominator)}")
            except ValueError:
                print("Invalid input. Enter numerical values.")#Incase user enters a number

        elif choice == 'c':
            target_date = "2025-07-04"
            print(f"Days until {target_date}: {days_until_date(target_date)}")

        elif choice == 'd':
            try:
                a = float(input("Enter the length of side a(Ex: 5.78): "))
                b = float(input("Enter the length of side b(Ex: 9.99): "))
                angle_degrees = float(input("Enter the angle between them in degrees(Ex: 67.87): "))
                print(f"The third side of the triangle is: {law_of_cosines(a, b, angle_degrees)}")
            except ValueError:
                print("Invalid input. Enter numerical values.")#Incase user enters a letter

        elif choice == 'e':
            try:
                radius = float(input("Enter the radius of the cylinder(Ex: 9.21): "))
                height = float(input("Enter the height of the cylinder(Ex:88.4): "))
                print(f"Volume of the cylinder: {volume_of_cylinder(radius, height)}")
            except ValueError:
                print("Invalid input. Enter numerical values.")#Incase user enters a letter

        elif choice == 'f':
            print("Thank you for using the application. Goodbye!")
            break

        else:
            print("Invalid choice. Select a valid option.")#Incase user doesn't choose a valid option

if __name__ == "__main__":
    main()
