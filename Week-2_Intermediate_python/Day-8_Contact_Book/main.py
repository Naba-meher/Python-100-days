# Contact Book
import json

# Step 1: Initialize an empty contact book or import existing contacts from a file
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

# Step 2: Display the menu
def show_menu():
  print("\n========== Contact Book Menu ==========")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Search Contact")
  print("4. Edit Contact")
  print("5. Delete Contact")
  print("6. Total Contacts")
  print("7. Exit")
  print("========================================")

# Step 3: Add a Contact
def add_contact():
    name = input("Enter contact name: ").strip().title()
    if name in contacts:
        print("Contact already exists!")
        return
    while True:
      phone = input("Enter contact number: ")

      if phone.isdigit() and len(phone) == 10:
        break
      print("Invalid phone number! Enter a 10-digit number.")
    email = input("Enter contact email: ")
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"{name} added successfully!")

# Step 4: View All Contacts
def view_contacts():
  if contacts:
    print("\n--- Contact List ---")
    for name, details in contacts.items():
      print("-"*30)
      print(f"Name: {name}")
      print(f"Phone: {details['phone']}")
      print(f"Email: {details['email']}")
  else:
    print("Your contact book is empty.")

# Step 5: Search a Contact
def search_contact():
  name = input("Enter the name of the contact you want to search: ").strip().title()
  if name in contacts:
    print(f"\n--- Contact Details for {name} ---")
    print(f"Name: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    print("-"*30)
  else:
    print(f"Contact {name} not found in your contact book.")

# Step 6: Edit a contact
def edit_contact():
  name = input("Enter the name of the contact you want to edit: ").strip().title()
  if name in contacts:
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} has been updated successfully!")
  else:
    print(f"Contact {name} not found in your contact book.")

# Step 7: Delete a contact
def delete_contact():
  name = input("Enter the name of the contact you want to delete: ").strip().title()
  if name in contacts:
    del contacts[name]
    print(f"Contact {name} has been deleted successfully!")
  else:
    print(f"Contact {name} not found in your contact book.")

#Step 8: Save contacts to a file before exiting
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Step 9: Main Program Loop
while True:
  show_menu()
  choice = input("Enter your choice (1-7): ")

  if choice == "1":
    add_contact()
    save_contacts()
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    search_contact()
  elif choice == "4":
    edit_contact()
    save_contacts()
  elif choice == "5":
    delete_contact()
    save_contacts()
  elif choice == "6":
    print("\n" + "-" * 30)
    print(f"Total Contacts : {len(contacts)}")
    print("-" * 30)
  elif choice == "7":
    print("Thank you for using the Contact Book. Goodbye!")
    save_contacts()
    break
  else:
    print("Invalid choice. Please select a valid option (1-7).")