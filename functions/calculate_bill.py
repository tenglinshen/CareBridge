"""
Bill Calculation System
Builds on the existing triage logic: a patient's severity determines their
room, and each room has a different flat fee. The final bill is the
consultation fee, plus the room fee, plus any additional charges (e.g.
medication or procedures) entered by staff.
"""

from book_appointment import get_severity, classify_room, WAITING_ROOM, ROOM_1, ROOM_2

CONSULTATION_FEE = 30.00

ROOM_FEES = {
    WAITING_ROOM: 20.00,
    ROOM_1: 50.00,
    ROOM_2: 100.00,
}

# In-memory list of generated bills.
# Each bill is a dict: {name, severity, room, room_fee, additional_charges, total}
bills = []


def get_patient_name():
    """Ask for the patient's name and validate it isn't blank."""
    while True:
        name = input("Enter patient name: ").strip()
        if not name:
            print("Error: Name cannot be blank.\n")
            continue
        return name


def get_additional_charges():
    """Ask for any additional charges (medication/procedures) and validate
    it's a non-negative number."""
    while True:
        charges_input = input(
            "Enter additional charges (medication/procedures), or 0 if none: "
        ).strip()
        try:
            charges = float(charges_input)
        except ValueError:
            print("Error: Please enter a valid number (e.g. 25 or 25.50).\n")
            continue
        if charges < 0:
            print("Error: Additional charges cannot be negative.\n")
            continue
        return round(charges, 2)


def calculate_bill():
    """Collect patient info, triage them, and calculate/display their bill."""
    name = get_patient_name()
    severity = get_severity()
    room = classify_room(severity)
    room_fee = ROOM_FEES[room]
    additional_charges = get_additional_charges()

    total = CONSULTATION_FEE + room_fee + additional_charges

    bill = {
        "name": name,
        "severity": severity,
        "room": room,
        "room_fee": room_fee,
        "additional_charges": additional_charges,
        "total": total,
    }
    bills.append(bill)

    print("\n--- Bill Summary ---")
    print(f"Patient            : {name}")
    print(f"Severity Level     : {severity}")
    print(f"Assigned Room      : {room}")
    print(f"Consultation Fee   : ${CONSULTATION_FEE:.2f}")
    print(f"Room Fee           : ${room_fee:.2f}")
    print(f"Additional Charges : ${additional_charges:.2f}")
    print(f"Total Bill         : ${total:.2f}")
    print("---------------------\n")


def view_bills():
    """Display all previously calculated bills."""
    if not bills:
        print("\nNo bills calculated yet.\n")
        return

    print("\n--- All Bills ---")
    for i, b in enumerate(bills, start=1):
        print(f"{i}. {b['name']} | {b['room']} | Total: ${b['total']:.2f}")
    print("------------------\n")


def main_menu():
    while True:
        print("===== Bill Calculation System =====")
        print("1. Calculate Bill")
        print("2. View Bills")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            calculate_bill()
        elif choice == "2":
            view_bills()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main_menu()