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
            print("Register Patient selected.")

        elif choice == "2":
            print("Book Appointment selected.")

        elif choice == "3":
            print("Calculate Bill selected.")

        elif choice == "4":
            print("Assign Triage Room selected.")

        elif choice == "5":
            print("Thank you for using CareBridge Hospital.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()