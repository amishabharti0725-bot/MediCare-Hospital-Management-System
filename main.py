print("========================================")
print("   MEDICARE HOSPITAL MANAGEMENT SYSTEM")
print("========================================")

while True:
    print("\nMain Menu")
    print("1. Patient Management")
    print("2. Doctor Management")
    print("3. Appointment Management")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nPatient Management")
        print("Patient module will be added soon.")

    elif choice == "2":
        print("\nDoctor Management")
        print("Doctor module will be added soon.")

    elif choice == "3":
        print("\nAppointment Management")
        print("Appointment module will be added soon.")

    elif choice == "4":
        print("\nThank you for using MediCare!")
        break

    else:
        print("\nInvalid choice. Please try again.")
