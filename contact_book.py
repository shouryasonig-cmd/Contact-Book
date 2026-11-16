# Myu contact book 


Contact_Book = {}

while True:

    print("\n__________________________")
    print('     WELCOME TO MY CONTACTS')
    print("**************************")

    print('\n~~~ Please Select The Operation ~~~')
    print('\n A --> Create Contact')
    print('\n B --> Delete Contact')
    print('\n C --> Update Contact')
    print('\n D --> View Contact List')
    print('\n E --> EXIT')

    operation = input('\nEnter Your Choice - ')

    # CREATE CONTACT

    if operation.upper() == 'A':

        print('\n~ CREATE A NEW CONTACT ~')

        Contact_Name = input('\nEnter Name: ').strip()
        Contact_Number = input('Enter Contact Number: ')
        Contact_email = input('Enter Email: ').strip()

        Person = {
            'Contact_Name': Contact_Name,
            'Contact_Number': Contact_Number,
            'Contact_email': Contact_email
        }

        Contact_Book[Contact_Name] = Person

        print('\nContact Successfully Added!')
        print(Contact_Book)

    # DELETE CONTACT

    elif operation.upper() == 'B':

        print('\n~ DELETE CONTACT ~')

        for contact in Contact_Book:
            print(contact)

        Dlt_Name = input('\nEnter Contact Name To Delete: ').strip()

        if Dlt_Name in Contact_Book:
            Contact_Book.pop(Dlt_Name)
            print('\nContact Successfully Deleted!')
        else:
            print('\nContact Not Found!')

    # UPDATE CONTACT

    elif operation.upper() == 'C':

        print('\n~ UPDATE CONTACT ~')

        for contact in Contact_Book:
            print(contact)

        Edit_Name = input('\nEnter Contact Name: ').strip()

        if Edit_Name in Contact_Book:

            print('\nG --> Contact Name')
            print('H --> Contact Number')
            print('I --> Contact Email')

            operation3 = input('\nSelect Option: ')

            if operation3.upper() == 'G':

                Updated_Name = input('Enter New Name: ').strip()

                temp = Contact_Book.pop(Edit_Name)

                temp['Contact_Name'] = Updated_Name

                Contact_Book[Updated_Name] = temp

                print('\nName Successfully Updated!')

            elif operation3.upper() == 'H':

                Update_Number = input('Enter New Number: ')

                Contact_Book[Edit_Name]['Contact_Number'] = Update_Number

                print('\nNumber Successfully Updated!')

            elif operation3.upper() == 'I':

                Update_email = input('Enter New Email: ')

                Contact_Book[Edit_Name]['Contact_email'] = Update_email

                print('\nEmail Successfully Updated!')

            else:
                print('\nInvalid Option!')

        else:
            print('\nContact Not Found!')

    # VIEW CONTACT

    elif operation.upper() == 'D':

        print('\n~ CONTACT BOOK ~')

        if len(Contact_Book) == 0:
            print('\nContact Book Is Empty!')

        else:

            for contact in Contact_Book:
                print(contact)

            print('\nP --> View Contact Details')
            print('Q --> Exit')

            operation4 = input('\nSelect Option: ')

            if operation4.upper() == 'P':

                Details = input('Enter Contact Name: ').strip()

                if Details in Contact_Book:

                    for key, value in Contact_Book[Details].items():
                        print(key, '--->', value)

                else:
                    print('\nContact Not Found!')

    # EXIT

    elif operation.upper() == 'E':

        print('\nThanks For Accessing Contact Book!')
        print('### EXIT ###')
        break

    else:
        print('\nInvalid Operation!')