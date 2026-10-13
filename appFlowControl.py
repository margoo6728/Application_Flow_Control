from datetime import datetime

# Display the Student ID and name of application
print("margoo6728's Spreadsheet Automation Menu")

# Store the menu options in a list
menuOptions = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
    ]

# Display the menu
print("Choose a number from the following options")

for option in menuOptions:
    print(option)

# Ask user to select an option
userChoice = input("")

# Check if the user's selection is valid
if userChoice in ["1", "2", "3"]:
    currentDateTime = datetime.now()
    print(f'You selected {userChoice} at {currentDateTime}')
    
else:
    print("Error: Invalid choice selected")

