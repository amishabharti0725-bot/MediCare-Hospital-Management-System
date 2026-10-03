
from patient import register_patient, display_patients

print("Welcome to MediCare Hospital")

while True:
    print("\n1. Register Patient")
    print("2. Display Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        display_patients()

    elif choice == "3":
        print("Thank you for using MediCare!")
        break

    else:
        print("Invalid choice. Try again.")
