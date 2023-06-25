import phone1


while True:
    print("Enter your choices: ")
    print("1. Add")
    print("2. Edit")
    print("3. Search")
    print("4. Display")
    print("5. Delete")
    print("6. Exit")

    choice = input("Enter your choices: ")

    if choice == '1':
        phone1.add()
    elif choice == '2':
        phone1.edit()
    elif choice == '3':
        phone1.search()
    elif choice == '4':
        phone1.display()
    elif choice == '5':
        phone1.delete()
    elif choice == '6':
        print ("Exiting")
        break
    else:
        print ("Invalid choice.")