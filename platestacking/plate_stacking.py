plates = []
def display_menu():
    print("\nMenu:")
    print("=" * 20)
    print("0. [Exit]")
    print("1. Add the plate")
    print("2. Print plates")
    print("3. Remove a plate")

def add_plate():
    global plates

    size = input("Enter plate size: ")

    try:
        size = int(size)
    except ValueError:
        print("Invalid size of plate given")
        return

    if size <= 0:
        print("Cannot add a plate of invalid size")
        return

    if len(plates) > 0:
        if size <= plates[-1]:
            plates.append(size)
        else:
            print(f"Cannot place a plate of size {size} on top of another plate of size {plates[-1]}")
    else:
        plates.append(size)


def print_plates():
    global plates

    if len(plates) == 0:
        print("No plates in the stack, please add some.")
        return

    for num in reversed(plates):
        print('#' * num)


def remove_plates():
    global plates

    try:
        num_plates = input("Enter the number of plates to remove: ")
        num_plates = int(num_plates)

        if num_plates <= 0:
            print("Invalid number of plates given, Number should be greater than 0")
            return
        
        if num_plates > len(plates):
            print(f"Max number of plates that can be removed are {len(plates)}, Please input a valid number.")
            return
        
        plates = plates[:-num_plates]
        print(f"Number of plates removed {num_plates}")

    except ValueError:
        print("Invalid number of plates given.")

if __name__ == "__main__":
    
    while True:
        display_menu()

        opt = input("Please select from [0-3]: ")
        
        if opt == "0":
            print("Exiting. Goodbye!")
            break

        elif opt == "1":
            add_plate()

        elif opt == "2":
            print_plates()

        elif opt == "3":
            remove_plates()
        else:
            print("Invalid choice. Please select a valid option.")