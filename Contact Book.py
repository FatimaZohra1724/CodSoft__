# Contact Book Dictionary
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    if name in contacts:
        print(f"Contact '{name}' already exists!")
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact '{name}' added!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts available!")
    else:
        print("Here are your contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Found: {name} - Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
    else:
        print(f"No contact found with the name '{name}'.")

# Function to update a contact
def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        print("Leave blank if you don’t want to change the field.")
        phone = input("New Phone (or press Enter to keep current): ")
        email = input("New Email (or press Enter to keep current): ")
        address = input("New Address (or press Enter to keep current): ")
        if phone: contacts[name]["Phone"] = phone
        if email: contacts[name]["Email"] = email
        if address: contacts[name]["Address"] = address
        print(f"Contact '{name}' updated!")
    else:
        print(f"No contact found with the name '{name}'.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted!")
    else:
        print(f"No contact found with the name '{name}'.")

# Main function to run the program
def contact_book():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
contact_book()
