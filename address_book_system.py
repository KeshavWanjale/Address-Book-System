class Contact:
    '''
    Description:
        Represents a contact with personal information.
    '''
    def __init__(self,irst_name, last_name, address, city, state, zip_code, phone, email) :
        '''
        Description:
            Initializes a new Contact instance.
        '''
        self.contact['first_name'] = input("Enter First Name: ")
        self.contact['last_name'] = input("Enter Last Name: ")
        self.contact['address'] = input("Enter Address: ")
        self.contact['city'] = input("Enter City: ")
        self.contact['state'] = input("Enter State: ")
        self.contact['zip_code'] = input("Enter ZIP Code: ")
        self.contact['phone'] = input("Enter Phone Number: ")
        self.contact['email'] = input("Enter Email: ")


class AddressBook:
    '''
    Description:
        Represents an address book that stores multiple contacts.
    '''

    def __init__(self):
        '''
        Description:
            Initializes an empty AddressBook.
        '''
        self._contacts = {}

    def get_full_name(self, contact):
        '''
        Description:
            Returns the full name (first name + last name) of the contact in lowercase.
        '''
        return f"{contact.first_name} {contact.last_name}".lower()
    
    def add_contact(self, contact):
        '''
        Description:
            Adds a new contact to the address book, using the full name as the key.
        '''
        full_name = self.get_full_name(contact)
        self._contacts[full_name] = contact
        print("Contact added successfully.")


class AddressBookMain:
    '''
    Description:
        The main class for running the Address Book application.
    '''
    def __init__(self):
        ''' 
        Description:
            Initializes the AddressBookApp with an empty AddressBook.
        '''
        self.address_book = AddressBook()

    def menu(self):
        '''
        Description:
            Displays the menu options to the user.
        '''
        print(f'{"-"*10} Select Option {"-"*10}')
        print('1. Add Contact')
        print('2. Exit')

    def get_contact_details(self):
        '''
        Description:
            Prompts the user for contact details and returns a Contact object.
        Returns:
            Contact: The contact object with the provided details.
        '''
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter ZIP Code: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        return Contact(first_name, last_name, address, city, state, zip_code, phone, email)
    
    def run(self):
        """Runs the main loop of the program."""
        while True:
            self.menu()
            choice = input("Enter your option: ")
            if choice == '1':
                contact = self.get_contact_details()
                self.address_book.add_contact(contact)
            elif choice == '2':
                print("Exiting Address Book Program")
                break  
            else:
                print("Invalid option. Please try again.")



if __name__ == "__main__":
    app = AddressBookMain()
    app.run()
