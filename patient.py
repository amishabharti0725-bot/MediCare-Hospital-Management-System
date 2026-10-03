
# Patient details

patients = []

def register_patient():
    print("\n--- Register Patient ---")

    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    disease = input("Enter disease: ")

    patient = (patient_id, name, age, disease)
    patients.append(patient)

    print("Patient registered successfully!")


def display_patients():
    print("\n--- Patient Records ---")

    if len(patients) == 0:
        print("No patient records found.")
    else:
        for patient in patients:
            print("Patient ID:", patient[0])
            print("Name:", patient[1])
            print("Age:", patient[2])
            print("Disease:", patient[3])
            print("-------------------")
