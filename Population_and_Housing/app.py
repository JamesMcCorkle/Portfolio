"""This is a multi menu-driven program that will:
Analyzes population and housing data from a CSV, displaying statistics and histograms for chosen columns. 
Requires pandas and matplotlib.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    """Load PopChange or Housing CSV file into a DataFrame."""
    try:
        df = pd.read_csv(file_path)#attempts to read chosen CSV file
        print(f"Successfully loaded {file_path}")#Displays message on successful load
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")#Exception handling for not finding the file
        return None

def analyze_column(df, column_name):
    """Analysis of a specific column."""
    if column_name in df.columns:
        print(f"\nAnalysis for {column_name}:")
        count = df[column_name].count()#Counts all values in the column
        mean = df[column_name].mean()#Calculates the mean
        std_dev = df[column_name].std()#Calculates standard deviation
        min_value = df[column_name].min()#Assigns lowest value to min_value
        max_value = df[column_name].max()#Assign highest value to max_value

        print(f"Count: {count}")#Display the calcualtions that were done
        print(f"Mean: {mean:.2f}")#and format them to hundreths for cleanliness
        print(f"Standard Deviation: {std_dev:.2f}")
        print(f"Min: {min_value:.2f}")
        print(f"Max: {max_value:.2f}")

        """Histogram for datasets"""
        plt.hist(df[column_name], edgecolor='black')#Histogram for specified column(outlining the bars with a black line for cleanliness)
        plt.title(f'Histogram of {column_name}')
        plt.show()
    else:
        print(f"Column {column_name} not found in the dataset.")

def analyze_population_change(file_path):
    """Analyze population change dataset."""
    df = load_csv(file_path)
    if df is not None:
        while True:#Loop for column menu
            print("\nSelect the Column you want to analyze:")
            print("a. Pop Apr 1")
            print("b. Pop Jul 1")
            print("c. Change Pop")
            print("d. Exit Column")

            column_choice = input("Enter a, b, c, or d: ").strip().lower()

            if column_choice == 'a':#Diplays correct column analysis for user choice
                print("You chosen Pop Apr 1")
                analyze_column(df, 'Pop Apr 1')
            elif column_choice == 'b':
                print("You chosen Pop Jul 1")
                analyze_column(df, 'Pop Jul 1')
            elif column_choice == 'c':
                print("You chosen Change Pop")
                analyze_column(df, 'Change Pop')
            elif column_choice == 'd':
                print("Exiting column choice.")
                break
            else:
                print("Invalid choice. Enter a, b, c, or d.")#incase of invalid input

def analyze_housing(file_path):
    """Analyze housing dataset."""
    df = load_csv(file_path)
    if df is not None:
        while True:#Loop for column menu
            print("\nSelect the Column you want to analyze:")
            print("a. AGE")
            print("b. BEDRMS")
            print("c. NUNITS")
            print("d. BUILT")
            print("e. ROOMS")
            print("f. WEIGHT")
            print("g. UTILITY")
            print("h. Exit Column")

            column_choice = input("Enter a, b, c, d, e, f, g or h: ").strip().lower()

            if column_choice == 'a':#Displays correct column analysis for user choice
                print("You have chosen AGE")
                analyze_column(df, 'AGE')
            elif column_choice == 'b':
                print("You have chosen BEDRMS")
                analyze_column(df, 'BEDRMS')
            elif column_choice == 'c':
                print("You have chosen NUNITS")
                analyze_column(df, 'NUNITS')
            elif column_choice == 'd':
                print("You have chosen BUILT")
                analyze_column(df, 'BUILT')
            elif column_choice == 'e':
                print("You have chosen ROOMS")
                analyze_column(df, 'ROOMS')
            elif column_choice == 'f':
                print("You have chosen WEIGHT")
                analyze_column(df, 'WEIGHT')
            elif column_choice == 'g':
                print("You have chosen UTILITY")
                analyze_column(df, 'UTILITY')
            elif column_choice == 'h':
                print("Exiting column choice.")
                break
            else:
                print("Invalid choice. Enter a, b, c, d, e, f, g or h.")#Incase of invalid input

#Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    """Main function for running the program"""
    while True:#Loop for data/exit
        print("\nSelect the dataframe to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == '1':#make sure the correct CSV file is loaded
            file_path = os.path.join(BASE_DIR, 'PopChange.csv')
            print("You have chosen Population Data.")
            analyze_population_change(file_path)
        elif choice == '2':
            file_path = os.path.join(BASE_DIR, 'Housing.csv')
            print("You have chosen Housing Data.")
            analyze_housing(file_path)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")#incase of invalid input

if __name__ == "__main__":
    main()
