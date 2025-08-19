""""This is a menu driven program that will:
Diplay states in alphabetical order.
Display a specific states capital, pop, and flower.
Display the top 5 populated states with a bar graph.
Allow updates to data for states for reusablity."""
import matplotlib.pyplot as plt

#Data for U.S. states (pop. from https://worldpopulationreview.com/states)
states_data = {
    'Alabama': ['Montgomery', 5143030, 'Camellia'],
    'Alaska': ['Juneau', 733536, 'Forget-Me-Not'],
    'Arizona': ['Phoenix', 7497000, 'Saguaro Cactus Blossom'],
    'Arkansas': ['Little Rock', 3089060, 'Apple Blossom'],
    'California': ['Sacramento', 38965200, 'California Poppy'],
    'Colorado': ['Denver', 5914180, 'Rocky Mountain Columbine'],
    'Connecticut': ['Hartford', 3625650, 'Mountain Laurel'],
    'Delaware': ['Dover', 1044320, 'Peach Blossom'],
    'Florida': ['Tallahassee', 22975900, 'Orange Blossom'],
    'Georgia': ['Atlanta', 11145300, 'Cherokee Rose'],
    'Hawaii': ['Honolulu', 1430880, 'Pua Aloalo'],
    'Idaho': ['Boise', 1990460, 'Syringa'],
    'Illinois': ['Springfield', 12516900, 'Violet'],
    'Indiana': ['Indianapolis', 6892120, 'Peony'],
    'Iowa': ['Des Moines', 3214320, 'Wild Prairie Rose'],
    'Kansas': ['Topeka', 2944380, 'Wild Native Sunflower'],
    'Kentucky': ['Frankfort', 4540740, 'Golden Rod'],
    'Louisiana': ['Baton Rouge', 4559480, 'Magnolia'],
    'Maine': ['Augusta', 1404110, 'White pine cone and tassel'],
    'Maryland': ['Annapolis', 6196520, 'Black-eyed Susan'],
    'Massachusetts': ['Boston', 7020060, 'Mayflower'],
    'Michigan': ['Lansing', 10041200, 'Apple Blossom'],
    'Minnesota': ['Saint Paul', 5761530, 'Pink and white lady slipper'],
    'Mississippi': ['Jackson', 2940450, 'Magnolia'],
    'Missouri': ['Jefferson City', 6215140, 'White Hawthorn Blossom'],
    'Montana': ['Helena', 1142750, 'Bitterroot'],
    'Nebraska' :['Lincoln', 1988700, 'Goldenrod'],
    'Nevada': ['Carson City', 3210930, 'Sagebrush'],
    'New Hampshire': ['Concord', 1405100, 'Purple Lilac'],
    'New Jersey': ['Trenton', 9320860, 'Violet'],
    'New Mexico': ['Santa Fe', 2115270, 'Yucca Flower'],
    'New York': ['Albany', 19469200, 'Rose'],
    'North Carolina': ['Raleigh', 10975000, 'American Dogwood'],
    'North Dakota': ['Bismarck', 788940, 'Wild Priarie Rose'],
    'Ohio': ['Columbus', 11812200, 'Scarlet Carnation'],
    'Oklahoma': ['Oklahoma City', 4088380, 'Oklahoma Rose'],
    'Oregan': ['Salem', 4227340, 'Oregon Grape'],
    'Pennsylvania': ['Harrisburg', 12951300, 'Mountain Laurel'],
    'Rhode Island': ['Providence', 1098080, 'Common Blue Violet'],
    'South Carolina': ['Columbia', 5464160, 'Yellow Jasmine'],
    'South Dakota': ['Pierre', 928767, 'Americana Pasque'],
    'Tennessee': ['Nashville', 7204000, 'Iris'],
    'Texas': ['Austin', 30976800, 'Bluebonnet'],
    'Utah': ['Salt Lake City', 3454230, 'Sego Lily'],
    'Vermont': ['Montpelier', 647818, 'Red Clover'],
    'Virginia': ['Richmond', 8752300, 'American Dogwood'],
    'Washington': ['Olympia', 7841280, 'Coast Rhododendron'],
    'West Virginia': ['Charlstone', 1766110, 'Rhododendront'],
    'Wisconsin': ['Madison', 5931370, 'Wood Violet'],
    'Wyoming': ['Cheyenne', 586485, 'Indian Paintbrush'],
}

def display_states():
    """Display all states in alphabetical order."""
    print("\nU.S. States in Alphabetical Order:")
    print(f"{'State':<15} {'Capital':<15} {'Population':<12} Flower")#This is the header for the list that is displayed, left aligned with char fields set for readability
    print("=" * 60)#The "=" will act as a seperator for the header to improve readability and cleanliness of the list
    for state in sorted(states_data):#This code will also help improve readability by aligning each element to the left with set char fields as well as sorting alphabetically
        print(f"{state:<15} {states_data[state][0]:<15} {states_data[state][1]:<12} {states_data[state][2]}")

def search_state():
    """Search for a state and display its details."""
    state_name = input("\nEnter the name of the state you want to search for: ").strip()#Gets input from user of what state they wish to see
    if not state_name:
        print("\nInvalid input. Please enter a valid state name.")
        return
    state_name_title = state_name.title()#This converts the state name to a title so that case sensitivity does not matter(Ex:"tennessee", "Tennessee", and "TENNESSEE" would be show the same data)

    state_info = states_data.get(state_name_title)
    if state_info:
        print(f"\nState: {state_name_title}\nCapital: {state_info[0]}\nPopulation: {state_info[1]}\nFlower: {state_info[2]}")#Shows each element on its own line for readability and cleanliness
        display_flower_image(state_info[2])#Calls function to display state flower
    else:
        print("\nState not found. Try again.")

def display_flower_image(flower_name):
    """Display the image of the state flower."""
    img_path = f'images/{flower_name.lower().replace(" ", "_")}.jpg'#This is the path for the state flower replaceing " " with "_" and all uppercase to lowercase
    try:
        img = plt.imread(img_path)#If found, assigns correct state flower to img
        plt.imshow(img)#Preps image to be rendered
        plt.title(flower_name)#Sets title of img to flower name
        plt.axis('off')#Turns off axis labels(looks cleaner)
        plt.show()#Renders image
    except FileNotFoundError:#Exception handling if state flower is not found.
        print(f"Image for {flower_name} not found.")

def display_top_5_populated_states():
    """Display a bar graph of the top 5 populated states."""
    sorted_states = sorted(states_data.items(), key=lambda x: x[1][1], reverse=True)[:5]#I chose to use lambda to sort the list. This extracts the pop. and sorts reverse(decending) order giving top 5 populated states
    states = [state[0] for state in sorted_states]#This was my first time using lamda and it was interesting to work with
    populations = [state[1][1] for state in sorted_states]

    plt.bar(states, populations, color='red')#Creates a bar graph with x-axis states, y-axis population, with the bar color red.
    plt.xlabel('States')
    plt.ylabel('Population')
    plt.title('Top 5 Populated States')#Title for bar graph
    plt.show()#Renders bar graph

def update_population():
    """Update the population for a specific state."""
    state_name = input("\nEnter the name of the state you want to update the population for: ").strip().lower()#Promts user for state to update population
    if not state_name:#If input is empty or state not found
        print("\nInvalid input. Enter a valid state name.")
        return
    state_to_update = {state.lower(): state for state in states_data}#Convert each state name to lowercase so that case sensitivity is not an issue when searching for keys

    if state_name in state_to_update:
        try:
            new_population = int(input("Enter the new population: "))#Promts user for new population
            if new_population < 0:#Population can not be negative number
                print("\nPopulation cannot be negative. Enter a valid number.")
                return
            states_data[state_to_update[state_name]][1] = new_population#If user input passes checks, updates pop for desired state
            print("\nPopulation updated successfully.")#Confirmation of update
        except ValueError:#Exception handling for string
            print("\nInvalid input. Enter a numeric value for the population.")
    else:#If state is not in database
        print("\nState not found. Try again.")

def main():
    """Main function to run the menu driven application."""
    while True:#Loop for menu to ensure, and prompt until, choice "5"(exits program)
        print("\nWelcome to the U.S. States Information Program")
        print("1. Display all U.S. States in Alphabetical Order")
        print("2. Search for a specific state")
        print("3. Display a Bar Graph of the Top 5 Populated States")
        print("4. Update the population for a specific state")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()#Prompt user for input of which menu item they wish to select

        if choice == '1':#If choice is "1", calls function to display states in alphabetical order
            display_states()
        elif choice == '2':#If choice "2", calls function to search for specific states info
            search_state()
        elif choice == '3':#If choice "3", calls function to display top 5 populated states
            display_top_5_populated_states()
        elif choice == '4':#If choice "4", calls function to update states population
            update_population()
        elif choice == '5':#If choice "5", exits program displaying a thank you message
            print("\nThank you for using the U.S. States Information Program. Goodbye!")
            break
        else:#If choice not "1-5" displays error message asking for valid input
            print("\nInvalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
