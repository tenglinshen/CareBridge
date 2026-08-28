# Constants
WAITING_ROOM = "Waiting Room"
ROOM_1 = "Room 1"
ROOM_2 = "Room 2"

def assign_triage_room():
    """Ask for severity (1-10), validate, classify into a triage room, and display summary."""
    while True:
        severity_input = input("Enter severity of condition (1-10): ").strip()

        if not severity_input.isdigit():
            print("Error: Please enter a whole number between 1 and 10.\n")
            continue

        severity = int(severity_input)

        if severity < 1 or severity > 10:
            print("Error: Severity must be between 1 and 10.\n")
            continue

        break  # valid input, exit loop

    # Classify severity into a room
    if 1 <= severity <= 4:
        room = WAITING_ROOM
    elif 5 <= severity <= 7:
        room = ROOM_1
    else:  # 8 to 10
        room = ROOM_2

    # Display triage summary
    print("\n--- Triage Summary ---")
    print(f"Severity Level : {severity}")
    print(f"Assigned Room  : {room}")
    print("-----------------------\n")
if __name__ == "__main__":
    assign_triage_room()