from register_patient import register_patient
from book_appointment import book_appointment
from calculate_bill import calculate_bill
from assign_triage import assign_triage_room


def display_menu():
    print("\n===== CareBridge Hospital Management System =====")
    print("1. Register Patient")
    print("2. Book Appointment")
    print("3. Calculate Bill")
    print("4. Assign Triage Room")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            book_appointment()

        elif choice == "3":
            calculate_bill()

        elif choice == "4":
            assign_triage_room()

        elif choice == "5":
            print("Thank you for using CareBridge Hospital.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()