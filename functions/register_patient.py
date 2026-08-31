"""
Patient Registration System
Asks the staff member for a patient's basic details (name, age, ID),
validating each field until a valid value is provided, then displays a
confirmation of the patient information and a short success message.
"""

# In-memory list of registered patients.
# Each patient is a dict: {name, age, patient_id}
patients = []


def get_valid_name():
    """Ask for the patient's name and validate it isn't blank."""
    while True:
        name = input("Enter patient name: ").strip()
        if not name:
            print("Error: Name cannot be blank.\n")
            continue
        return name


def get_valid_age():
    """Ask for the patient's age and validate it's a positive whole number."""
    while True:
        age_input = input("Enter patient age: ").strip()
        if not age_input.isdigit():
            print("Error: Age must be a positive number.\n")
            continue
        age = int(age_input)
        if age <= 0:
            print("Error: Age must be a positive number.\n")
            continue
        return age


def get_valid_id():
    """Ask for the patient's ID and validate it isn't blank and is unique."""
    while True:
        patient_id = input("Enter patient ID: ").strip()
        if not patient_id:
            print("Error: Patient ID cannot be blank.\n")
            continue
        if any(p["patient_id"] == patient_id for p in patients):
            print(f"Error: Patient ID '{patient_id}' is already registered.\n")
            continue
        return patient_id


def register_patient():
    """Collect and validate a patient's details, then confirm registration."""
    name = get_valid_name()
    age = get_valid_age()
    patient_id = get_valid_id()

    patient = {
        "name": name,
        "age": age,
        "patient_id": patient_id,
    }
    patients.append(patient)

    print("\n--- Patient Registered Successfully ---")
    print(f"Name           : {name}")
    print(f"Age            : {age}")
    print(f"Patient ID     : {patient_id}")
    print("----------------------------------------\n")


def view_patients():
    """Display all currently registered patients."""
    if not patients:
        print("\nNo patients registered yet.\n")
        return

    print("\n--- Registered Patients ---")
    for i, p in enumerate(patients, start=1):
        print(f"{i}. {p['name']} | Age {p['age']} | ID: {p['patient_id']}")
    print("----------------------------\n")


def main_menu():
    while True:
        print("===== Patient Registration =====")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main_menu()