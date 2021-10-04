# Everyone uses a contact book to save contact details, including name, address, phone number
# This is a command-line project where you will design a contact book application
# that users can use to save and find contact details.
# The application should also allow users to update contact information, delete contacts, and list saved contacts.

information = list()
Fname = []
Lname = []
num = []

print("Welcome to ContactBook")
i = 0
i = i + 1
while i > 0:
    starterQuestion = input("\nWould you like to\n1. Add\n2. List All contacts\n3. Find a specific Contact\n4. Delete contact?(press Q to quit the program): ").upper()
    if starterQuestion == "1":
        getFName = input("\nPerson's first name: ").upper()
        getLName = input("Person's last name: ").upper()
        getNumber = input("Person's Contact Number: ")

        Fname.append(getFName)
        Lname.append(getLName)
        num.append(getNumber)


        print("Contact Saved!")

    elif starterQuestion == "2":
        print("First name: ", Fname[i])
        print("Last name: ", Lname[i])
        print("Number: ", num[i])
        print("------------\n")

    elif starterQuestion == "3":
        name = input("\nEnter name of person: ").upper()
        if name in Fname:
            index = Fname.index(name)
            LTname = Lname[index]
            number = num[index]
            print("\n---------\nFirst name:", name, "\nLast Name:", LTname, "\nNumber:", number)
            enter = input("Press ENTER to go back to the menu. Hit Q to quit: ")
            if enter == "":
                pass
            else:
                break
        else:
           print("Person is not on the directory.")
           enter = input("Press ENTER to go back to the menu. Hit Q to quit: ")
           if enter == "":
               pass
           else:
               break

    elif starterQuestion == "4":
        name = input("\nEnter Contact to be removed: ").upper()
        index = Fname.index(name)
        for name in Fname:
            if name == Fname[index]:
                warn = input("Are you sure?(Enter Y or N) ")
                if warn == "Y":
                    del Fname[index]
                    del Lname[index]
                    del num[index]
                    
            else:
                print("Person does not exist in the directory.\n")
            enter = input("Press ENTER to go back to the menu. Hit Q to quit: ")
            if enter == "":
                pass
            else:
                break
    elif starterQuestion == "Q":
        break
