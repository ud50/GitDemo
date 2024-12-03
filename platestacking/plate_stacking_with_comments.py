
# Global scope vairable
plates = []

def display_menu():
    # This function simply prints the menu.
    print("\nMenu:")
    print("=" * 20)
    print("0. [Exit]")
    print("1. Add the plate")
    print("2. Print plates")
    print("3. Remove a plate")

def add_plate():
    # Accessing the global variable directly.
    global plates

    # Ask for the size of plate from user.
    size = input("Enter plate size: ")

    # If the user has input any number then good, otherwise there will be valueError and function will
    # print the warning message and will not further proceed.
    try:
        size = int(size)
    except ValueError:
        print("Invalid size of plate given")
        return
    
    # If the size of plate is less or equal to 0, Print a warning and do not let the function to proceed further
    if size <= 0:
        print("Cannot add a plate of invalid size")
        return
    
    # If there are any other plates in stack, Then the size logic will work, Otherwise just add the plate to stack.
    if len(plates) > 0:
        if size <= plates[-1]:
            plates.append(size)
        else:
            print(f"Cannot place a plate of size {size} on top of another plate of size {plates[-1]}")
    else:
        plates.append(size)


def print_plates():
    # Accessing the global variable directly.
    global plates

    # Check if the stack has not plates, Print a message and return from there.
    if len(plates) == 0:
        print("No plates in the stack, please add some.")
        return
    
    # Here the stack is reversed and then looped over, to print the stack in asceding order.
    for num in reversed(plates):
        print('#' * num)


def remove_plates():
    # Accessing the global variable directly.
    global plates

    try:
        # Ask for the number of plates, and ensure that it's a number. otherwise valueError will happen
        num_plates = input("Enter the number of plates to remove: ")
        num_plates = int(num_plates)

        # if no plate in stack, Show warning and return
        if num_plates <= 0:
            print("Invalid number of plates given, Number should be greater than 0")
            return
        
        # If number exceed from the size of stack, Then show warning and return
        if num_plates > len(plates):
            print(f"Max number of plates that can be removed are {len(plates)}, Please input a valid number.")
            return
        
        # Remove the plates from stack.
        plates = plates[:-num_plates]
        print(f"Number of plates removed {num_plates}")

    except ValueError:
        print("Invalid number of plates given.")

# Main entry of the program
if __name__ == "__main__":
    
    # Loop to ask for input again untill user choose to exit.
    while True:
        
        # Display the main menu
        display_menu()

        # Ask for user choice
        opt = input("Please select from [0-3]: ")
        
        if opt == "0":
            # Exit the loop, If user choice is 0
            print("Exiting. Goodbye!")
            break

        elif opt == "1":
            # Add the plate to stack if the user choose to press 1
            add_plate()

        elif opt == "2":
            # Print the plates, if user choose 2
            print_plates()

        elif opt == "3":
            # Remove the plates from list.
            remove_plates()
        else:
            print("Invalid choice. Please select a valid option.")