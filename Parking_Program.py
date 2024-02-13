# set requirements
max_lot = 50
entry_fee = 4.00

# store plate+cards in list
vehicle_info = {}

#function 1 register_vehicle
def register_vehicle():
    def parking_availability():
        return len(vehicle_info) < max_lot

    if parking_availability():
        print("The parking lot has space for your vehicle")
        plate_num = input("Enter your plate number: ")

        if plate_num not in vehicle_info:
            cc = input("Enter your credit card number ($4.00 charge): ")
            vehicle_info[plate_num] = cc
            print("Thank you, your plate", plate_num, "has been added to the lot\n")
            return plate_num
        else:
            print(plate_num, "is already registered")
    else:
        print("Parking lot is full")
        return None


#check_password function
def check_password():
    pw = input("Enter user password:")
    return pw == 'password'


#function 2 verify_vehicle
def verify_vehicle():
    print("Verify your registration")
    if check_password():
        plate_num = input("Enter your plate number: ")
        if plate_num in vehicle_info:
            print("The vehicle with plate#", plate_num, "is registered in the lot")
        else:
            print('This vehicle is NOT registered')
    else:
        print("Password is incorrect!")


# function 3 display_vehicles
def display_vehicle():
    if check_password():
        if vehicle_info:
            with open("vehicles.txt", "w") as vehicle_list:
                vehicle_list.write("list of license plates: ")
                print("="*20) 
                print("       Plate")
                print("="*20)
                for plate_num in vehicle_info.keys():
                    vehicle_list.write(plate_num + "\n")
                    print(f"{plate_num}{' ' * 10}")
                print("List of license plates saved to vehicles.txt")
        else:
            print("No vehicles are registered in the lot, empty text file")
    else:
        print("Password is incorrect!")



#function 4 display_charges
def display_charges():
    if check_password():
        charges_day = entry_fee * len(vehicle_info)
        # Display information
        print("="*50)
        print(f"Plate{' ' * 10}Credit Card{' ' * 4}Charge in $")
        print("="*50)
        for plate, cc_number in zip(vehicle_info.keys(), vehicle_info.values()):
            print(f"{plate}{' ' * 10}{cc_number}{' ' * 10}${entry_fee:.2f}")
        print("="*50)
        print("Total:" f"{' ' * 25}${charges_day:.2f}")
        
        with open('charges.txt', 'w') as charges_file:
            charges_file.write("Registered License Plates:\n")
            for plate in vehicle_info.keys():
                charges_file.write(plate + '\n')

            charges_file.write("\nCredit Card Numbers:\n")
            for cc_number in vehicle_info.values():
                charges_file.write(cc_number + '\n')

            charges_file.write("\nCharges for the Day:\n")
            charges_file.write(f"${charges_day:.2f}\n")
    else:
        print("Password is incorrect!")


#function 5 remove_vehicle
def remove_vehicle():
    if check_password():
        if not vehicle_info:
            print("No vehicles registered.")
            return

        plate_to_remove = input("Enter the plate number to remove: ")

        if plate_to_remove in vehicle_info:
            del vehicle_info[plate_to_remove]
            print("Vehicle with plate number", plate_to_remove, "has been removed.")
        else:
            print("Plate number", plate_to_remove, "not found.")
    else:
        print("Password is incorrect!")


# function 6 clear_vehicles
def clear_vehicles():
    if check_password():
        vehicle_info.clear()
        print("All vehicles have been removed.")
    else:
        print("Password is incorrect!")

# function for printing the menu 
def print_menu():
    print("Menu:")
    print("1. Register a vehicle")
    print("2. Verify vehicle registration")
    print("3. Display registered vehicles and save them to a file")
    print("4. Display daily charges and save them to a file")
    print("5. Remove a vehicle")
    print("6. Clear vehicles")
    print("0. Exit")
    return int(input("Enter your choice (0-6): "))

print('****************************************************')
print("*** welcome to Park and Go Parking Application! ***\nPark from 6 PM - Midnight for a flat fee of $4.00")
print('****************************************************')

# menu loop to return print until 0 
while True:
    user_selection = print_menu()

    if user_selection == 1:
        register_vehicle()

    elif user_selection == 2:
        verify_vehicle()

    elif user_selection == 3:
        display_vehicle()

    elif user_selection == 4:
        display_charges()

    elif user_selection == 5:
        remove_vehicle()

    elif user_selection == 6:
        clear_vehicles()

    elif user_selection == 0:
        print("Exiting Program")
        break

    else:
        print("Invalid Input,\n")

    input("Press enter to continue...")
