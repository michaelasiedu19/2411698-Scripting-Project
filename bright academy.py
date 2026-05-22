"""
Bright Minds Academy - Equipment Booking System
Author: [Michael Asiedu]
Date: 28-04-2026
Features: Add equipment, record bookings, view records, search, low-booking alerts.
"""

# ------------------ DATA STORAGE ------------------ #

# Predefined student list (can be expanded later)
students = ["John White", "Kofi Asiedu", "Peter Mills", "Papa Ofori", "John Wick"]

# Preloaded equipment names (laptops)
equipment_names = ["Laptop 1", "Laptop 2", "Laptop 3", "Laptop 4", "Laptop 5"]

# Dictionary to store bookings
# Key = equipment name, Value = list of (student, date) tuples
equipment_bookings = {name: [] for name in equipment_names}
# This makes it easier to expand (e.g., add “Projector 1” later).

# ------------------ MENU DISPLAY ------------------ #
def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print(" BRIGHT MINDS ACADEMY - EQUIPMENT BOOKING SYSTEM")
    print("=" * 50)
    print("1. Add New Equipment")
    print("2. Record a Booking")
    print("3. View All Booking Records")
    print("4. Search Bookings")
    print("5. Low-Booking Alert")
    print("6. Exit")
    print("=" * 50)


# ------------------ ADD EQUIPMENT ------------------ #
def add_equipment():
    """Allows the user to add new equipment to the system."""
    print("\n--- Add New Equipment ---")

    # Get user input
    equip_name = input("Enter equipment name: ").strip()

    # Validation: empty input
    if not equip_name:
        print("Error: Equipment name cannot be empty!")
        return

    # Validation: duplicate equipment
    if equip_name in equipment_bookings:
        print(f"Error: '{equip_name}' already exists!")
        return

    # Add equipment with empty booking list
    equipment_bookings[equip_name] = []
    print(f"Success: '{equip_name}' has been added.")


# ------------------ RECORD BOOKING ------------------ #
def record_booking():
    """Records a booking for a selected piece of equipment."""
    print("\n--- Record a Booking ---")

    # Check if equipment exists
    if not equipment_bookings:
        print("Error: No equipment available. Add equipment first.")
        return

    # Display available equipment
    print("Available equipment:")
    for equip in equipment_bookings:
        print(f" - {equip}")

    # Select equipment
    equip_name = input("Enter equipment name: ").strip()
    if equip_name not in equipment_bookings:
        print(f"Error: '{equip_name}' not found.")
        return

    # Display student list
    print("\nRegistered students:")
    for student in students:
        print(f" - {student}")

    # Get student name
    student_name = input("Enter student name: ").strip()

    # Validate student name
    if not student_name:
        print("Error: Student name cannot be empty!")
        return

    if student_name not in students:
        print("Error: Student not in system.")
        return

    # Get booking date
    booking_date = input("Enter booking date (DD-MM-YYYY): ").strip()

    # Validate date format
    if len(booking_date) != 10 or booking_date[2] != '-' or booking_date[5] != '-':
        print("Error: Invalid date format. Use DD-MM-YYYY.")
        return

    # Check for double booking
    for student, date in equipment_bookings[equip_name]:
        if date == booking_date:
            print(f"Warning: '{equip_name}' is already booked on {booking_date}.")
            return

    # Store booking
    equipment_bookings[equip_name].append((student_name, booking_date))
    print(f"Success: {equip_name} booked for {student_name} on {booking_date}.")


# ------------------ VIEW BOOKINGS ------------------ #
def view_all_bookings():
    """Displays all equipment and their bookings."""
    print("\n--- All Booking Records ---")

    if not equipment_bookings:
        print("No equipment added yet.")
        return

    # Loop through all equipment
    for equip_name, bookings in equipment_bookings.items():
        print(f"\nEquipment: {equip_name}")

        if not bookings:
            print(" Status: Available (No bookings)")
        else:
            print(" Bookings:")
            for student, date in bookings:
                print(f" - Student: {student}, Date: {date}")


# ------------------ SEARCH BOOKINGS ------------------ #
def search_bookings():
    """Search bookings by student name or equipment."""
    print("\n--- Search Bookings ---")
    print("1. Search by Student Name\n2. Search by Equipment Name")

    choice = input("Enter choice (1 or 2): ").strip()

    # Search by student
    if choice == "1":
        student_name = input("Enter student name: ").strip()

        if not student_name:
            print("Error: Student name cannot be empty!")
            return

        found = False
        print(f"\nBookings for student '{student_name}':")

        for equip_name, bookings in equipment_bookings.items():
            for student, date in bookings:
                if student.lower() == student_name.lower():
                    print(f" Equipment: {equip_name}, Date: {date}")
                    found = True

        if not found:
            print(f"No bookings found for '{student_name}'.")

    # Search by equipment
    elif choice == "2":
        equip_name = input("Enter equipment name: ").strip()

        if not equip_name or equip_name not in equipment_bookings:
            print("Error: Equipment not found.")
            return

        print(f"\nBookings for {equip_name}:")
        bookings = equipment_bookings[equip_name]

        if not bookings:
            print(" No bookings recorded.")
        else:
            for student, date in bookings:
                print(f" Student: {student}, Date: {date}")

    else:
        print("Error: Invalid choice.")


# ------------------ LOW BOOKING ALERT ------------------ #
def low_booking_alert():
    """Displays days with bookings below a chosen threshold."""
    print("\n--- Low-Booking Alert ---")

    if not equipment_bookings:
        print("No equipment or bookings in the system yet.")
        return

    # Get threshold from user
    try:
        threshold = int(input("Enter minimum expected bookings per day (e.g. 3): "))
        if threshold < 0:
            threshold = 0
    except ValueError:
        print("Invalid input. Using default threshold = 3.")
        threshold = 3

    # Count bookings per day
    daily_counts = {}
    for bookings in equipment_bookings.values():
        for _, date in bookings:
            daily_counts[date] = daily_counts.get(date, 0) + 1

    if not daily_counts:
        print("No bookings recorded yet.")
        return

    # Display alerts
    print(f"\n--- Days with fewer than {threshold} bookings ---")
    alert_raised = False

    for date, count in daily_counts.items():
        if count < threshold:
            print(f"⚠️ ALERT: {date} has only {count} booking(s)")
            alert_raised = True

    if not alert_raised:
        print(f"✓ All days meet or exceed the threshold of {threshold}.")


# ------------------ MAIN PROGRAM LOOP ------------------ #
def main():
    """Main program loop that runs the system."""
    print("Welcome to Bright Minds Academy Equipment Booking System!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_equipment()
        elif choice == "2":
            record_booking()
        elif choice == "3":
            view_all_bookings()
        elif choice == "4":
            search_bookings()
        elif choice == "5":
            low_booking_alert()
        elif choice == "6":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Error: Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()
