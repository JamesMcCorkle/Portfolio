""" Voter Registraion code"""

def is_valid_name(name):
    """Check if the name is valid (not empty and contains only letters)."""
    return name.strip() != "" and name.replace(" ", "").isalpha()

def is_valid_age(age):
    """Check if the age is a reasonable number."""
    return age.isdigit() and 0 <= int(age) <= 120

def is_valid_state(state):
    """Check if the state code is valid (2 uppercase letters)."""
    return len(state) == 2 and state.isalpha() and state.isupper()

def main():
    """Main function to run the voter registration application."""
    print("Welcome to the Voter Registration Application!")

    # Get user information
    while True:
        first_name = input("Enter your first name (or type 'exit' to cancel): ")
        if first_name.lower() == 'exit':
            print("Registration canceled.")
            return
        if not is_valid_name(first_name):
            print("Error: Please enter a valid first name (only letters and not empty).")
            continue
        break

    while True:
        last_name = input("Enter your last name (or type 'exit' to cancel): ")
        if last_name.lower() == 'exit':
            print("Registration canceled.")
            return
        if not is_valid_name(last_name):
            print("Error: Please enter a valid last name (only letters and not empty).")
            continue
        break

    while True:
        age = input("Enter your age (or type 'exit' to cancel): ")
        if age.lower() == 'exit':
            print("Registration canceled.")
            return
        if not is_valid_age(age):
            print("Error: Please enter a valid age between 0 and 120.")
            continue
        break
    country = input("Enter country of citizenship such as United States (type 'exit' to cancel): ")
    if country.lower() == 'exit':
        print("Registration canceled.")
        return

    while True:
        state = input("Enter your state of residence (2-letter state, or type 'exit' to cancel): ")
        if state.lower() == 'exit':
            print("Registration canceled.")
            return
        if not is_valid_state(state):
            print("Error: Please enter a valid 2-letter state code.")
            continue
        break

    zipcode = input("Enter your zipcode (or type 'exit' to cancel): ")
    if zipcode.lower() == 'exit':
        print("Registration canceled.")
        return

    # Eligibility check
    if int(age) >= 18 and country.lower() == "united states":
        print("\nCongratulations! You are eligible to vote.")
        print("Your registration details:")
        print(f"Name: {first_name} {last_name}")
        print(f"Age: {age}")
        print(f"Country: {country}")
        print(f"State: {state}")
        print(f"Zipcode: {zipcode}")
    else:
        print("\nYou are not eligible to register to vote.")
        if int(age) < 18:
            print("You must be at least 18 years old.")
        if country.lower() != "united states, US, us":
            print("You must be a U.S. citizen.")

if __name__ == "__main__":
    main()
