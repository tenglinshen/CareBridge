"""
Appointment Booking System
Builds on the existing triage room assignment logic: when a patient books an
appointment, they're first triaged (severity 1-10) to determine which room
they're assigned to, then their appointment slot is checked for conflicts
within that room before being confirmed.
"""

from datetime import datetime

WAITING_ROOM = "Waiting Room"
ROOM_1 = "Room 1"
ROOM_2 = "Room 2"

# In-memory list of booked appointments.
# Each appointment is a dict: {name, date, time, severity, room}
appointments = []


def get_severity():
    """Ask for severity (1-10), validate, and return it as an int."""
    while True:
        severity_input = input("Enter severity of condition (1-10): ").strip()
        if not severity_input.isdigit():
            print("Error: Please enter a whole number between 1 and 10.\n")
            continue
        severity = int(severity_input)
        if severity < 1 or severity > 10:
            print("Error: Severity must be between 1 and 10.\n")
            continue
        return severity


def classify_room(severity):
    """Classify a severity score into a triage room."""
    if 1 <= severity <= 4:
        return WAITING_ROOM
    elif 5 <= severity <= 7:
        return ROOM_1
    else:  # 8 to 10
        return ROOM_2


def get_valid_date():
    """Ask for an appointment date and validate the format (DD-MM-YYYY)."""
    while True:
        date_input = input("Enter appointment date (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(date_input, "%D-%M-%Y")
            return date_input
        except ValueError:
            print("Error: Date must be in DD-MM-YYYY format.\n")


def get_valid_date():
    """Ask for an appointment date and validate the format (YYYY-MM-DD)."""
    while True:
        date_input = input("Enter appointment date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Error: Date must be in YYYY-MM-DD format.\n")


TIME_FORMATS = [
    "%H:%M",     # 09:00 / 9:00  (24hr)
    "%I:%M %p",  # 09:00 AM
    "%I:%M%p",   # 09:00AM
    "%I %p",     # 9 AM
    "%I%p",      # 9AM
    "%H%M",      # 0900
]



def get_valid_time():
    """Ask for an appointment time, accept several common formats,
    and return it normalized to HH:MM (24hr)."""
    while True:
        time_input = input("Enter appointment time (e.g. 14:30 or 2:30 PM): ").strip()
        for fmt in TIME_FORMATS:
            try:
                parsed = datetime.strptime(time_input.upper(), fmt)
                return parsed.strftime("%H:%M")
            except ValueError:
                continue
        print("Error: Couldn't understand that time. Try formats like "
    "'14:30', '2:30 PM', or '9AM'.\n")


def is_slot_taken(date, time, room):
    """Check if a date/time slot is already booked in the given room."""
    for appt in appointments:
        if appt["date"] == date and appt["time"] == time and appt["room"] == room:
            return True
    return False


def book_appointment():
    """Collect patient info, triage them, and book a conflict-free slot."""
    name = input("Enter patient name: ").strip()
    while not name:
        print("Error: Name cannot be empty.\n")
        name = input("Enter patient name: ").strip()

    severity = get_severity()
    room = classify_room(severity)

    while True:
        date = get_valid_date()
        time = get_valid_time()
        if is_slot_taken(date, time, room):
            print(f"Error: {room} is already booked on {date} at {time}. "
                "Please choose a different date/time.\n")
            continue
        break

    appointment = {
        "name": name,
        "date": date,
        "time": time,
        "severity": severity,
        "room": room,
    }
    appointments.append(appointment)

    print("\n--- Appointment Confirmed ---")
    print(f"Patient        : {name}")
    print(f"Severity Level : {severity}")
    print(f"Assigned Room  : {room}")
    print(f"Date           : {date}")
    print(f"Time           : {time}")
    print("------------------------------\n")


def view_appointments():
    """Display all currently booked appointments."""
    if not appointments:
        print("\nNo appointments booked yet.\n")
        input("Press Enter to return to the menu...")
        return

    print("\n--- All Appointments ---")
    for i, appt in enumerate(appointments, start=1):
        print(f"{i}. {appt['name']} | {appt['date']} {appt['time']} | "
    f"{appt['room']} (Severity {appt['severity']})")
    print("-------------------------\n")
    input("Press Enter to return to the menu...")

    print("\n--- All Appointments ---")
    for i, appt in enumerate(appointments, start=1):
        print(f"{i}. {appt['name']} | {appt['date']} {appt['time']} | "
            f"{appt['room']} (Severity {appt['severity']})")
    print("-------------------------\n")


def main_menu():
    while True:
        print("===== Appointment Booking System =====")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main_menu()