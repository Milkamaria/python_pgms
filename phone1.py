contacts = {}

def add():
    name = input("Enter the name: ")
    phno = (input("Enter phone number: "))
    contacts[name] = phno
    print("Contact added successfully.")

def edit():
    name = input("Enter the name to edit: ")
    if name in contacts:
        new_ph = input("Enter new phone number: ")
        contacts[name] = new_ph
        print("Contact updated successfully")
    else:
        print("Contact not found")

def search():
    name = input("Enter the name to search: ")
    if name in contacts:
        print("Phone number for", name, "is", contacts[name])
    else:
        print("Contact not found.")

def display():
    if len(contacts) == 0:
        print("Contact not found")
    else:
        print(contacts)
        for name, phno in contacts.items():
            print("Name:", name, "\tPhone number:", phno)
        
def delete():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")