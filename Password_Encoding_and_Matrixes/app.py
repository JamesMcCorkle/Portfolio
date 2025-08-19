"""This is a menu driven program.
The program will promt user for their phone number and zipcode.
The program with then prompt user for 2 3x3 matrixes.
The program will then prompt the user asking if they want to add/sub/mult or element multi."""
import re
import numpy as np

def validate_phone_number(phone):
    """Check if provided phone number is valid(10-digits)."""
    pattern = re.compile(r"^\d{10}$")#Check is phone number is 10 digits
    return bool(pattern.match(phone))#Returns true if 10-digits or false if not

def validate_zipcode(zipcode):
    """Check if provided zipcode is 5-digit zipcode or zip+4 code."""
    pattern = re.compile(r"^\d{5}(-\d{4})?$")#Check for 5-digit zip or zip+4 code if applies
    return bool(pattern.match(zipcode))#Return true if digits match either 5-digit or zip+4 code


def get_valid_phone_number():
    """Prompts user for phone number until valid response is given"""
    while True:
        phone = input("Enter your phone number (10 digits): ")#Prompt user for their phone number
        if validate_phone_number(phone):#Calls function to validate phone number
            return phone#Returns phone number if valid
        else:
            print("Invalid phone number. Enter exactly 10 digits.")#Error message for invalid input

def get_valid_zipcode():
    """Prompts user for zipcode until valid response is given"""
    while True:
        zipcode = input("Enter your ZIP+4 code (##### or #####-####): ")#Prompts user for their zipcode
        if validate_zipcode(zipcode):#Calls function to validate zipcode
            return zipcode#If valid, returns zipcode
        else:
            print("Invalid ZIP+4 code. Enter in the Format ##### or #####-####.")#Error message for invalid zipcode

def get_matrix_input(name):
    """Prompts user for a 3x3 matrix"""
    while True:
        try:
            print(f"Enter the values for {name} (3x3 matrix(Ex. 3 3 3)):")
            matrix = []#Initialize empty list named matrix
            for i in range(3):#Iterates 3 times, once for each row
                row = input(f"Enter row {i+1} (3 space-separated integers): ").split()#Prompts user for input for matrix
                if len(row) != 3:#If row is not 3 ints
                    raise ValueError("Each row must contain exactly 3 integers.")#Error message for incorrect input
                matrix.append([int(x) for x in row])#Adds user valus to matrix
            return np.array(matrix)#After all 3 rows are entered, converts list into NumPy array
        except ValueError as e:#Error message for invalid input
            print(f"Invalid input: {e}. Try again.")

def main():
    """Main function of the menu-driven program"""
    phone = get_valid_phone_number()
    zipcode = get_valid_zipcode()

    matrix1 = get_matrix_input("Matrix 1")
    matrix2 = get_matrix_input("Matrix 2")

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Matrix Multiplication")
        print("4. Element-wise Multiplication")
        print("5. Exit")
        operation = input("Enter the number of the operation you want to perform: ")

        if operation == "1":
            result = matrix1 + matrix2#Matrix addition for matrix1 and matrix2
        elif operation == "2":
            result = matrix1 - matrix2#Matrix subtraction for matrix1 and matrix2
        elif operation == "3":
            result = np.matmul(matrix1, matrix2)#Matrix multiplication for matrix1 and matrix2
        elif operation == "4":
            result = np.multiply(matrix1, matrix2)#Element-wise multiplication
        elif operation == "5":
            print("Exiting the program. Thank you for your time!")#Exits program when chosen
            break
        else:
            print("Invalid operation selected. Try again.")#Error message for invalid menu input
            continue

        transpose_result = np.transpose(result)#Computes transpose of the result matrix
        row_means = np.mean(result, axis=1)#Computes mean of result matrix
        column_means = np.mean(result, axis=0)#Computes mean of the result matrix

        """I know that this part was not asked for but I do not like to waste user inputs :D"""
        print(f"Phone number: {phone}")#Displays user entered phone number
        print(f"ZIP+4 code: {zipcode}")#Displays user entered zipcode

        print("\nResulting matrix:")
        for row in result: #Format the resulting matrix to hundredths
            print(" ".join([f"{x:.2f}" for x in row]))
        print("\nTranspose of the result:")
        for row in transpose_result:#Format the transpose result to hundredths
            print(" ".join([f"{x:.2f}" for x in row]))
        print("\nMean of the rows:")
        print(" ".join([f"{x:.2f}" for x in row_means]))#Format the row means to hundredths
        print("\nMean of the columns:")
        print(" ".join([f"{x:.2f}" for x in column_means]))#Format the column means to hundredths

if __name__ == "__main__":
    main()
