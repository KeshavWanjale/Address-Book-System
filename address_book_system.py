class Contact:
    '''
    Description:
        Represents a contact with personal information.
    '''

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        '''
        Description:
            Initializes a new Contact instance with personal details.
        Parameters:
            first_name: The first name of the contact.
            last_name: The last name of the contact.
            address: The address of the contact.
            city: The city where the contact resides.
            state: The state where the contact resides.
            zip_code: The postal code for the contact's address.
            phone: The phone number of the contact.
            email: The email address of the contact.
        Return:
            None
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def update_contact(self, first_name=None, last_name=None, address=None, city=None, state=None, zip_code=None, phone=None, email=None):
        '''
        Description:
            Updates the contact details if new values are provided.
        Parameters:
            first_name: Updated first name (optional).
            last_name: Updated last name (optional).
            address: Updated address (optional).
            city: Updated city (optional).
            state: Updated state (optional).
            zip_code: Updated postal code (optional).
            phone: Updated phone number (optional).
            email: Updated email address (optional).
        Return:
            None
        '''
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if address:
            self.address = address
        if city:
            self.city = city
        if state:
            self.state = state
        if zip_code:
            self.zip_code = zip_code
        if phone:
            self.phone = phone
        if email:
            self.email = email



class AddressBook:
    '''
    Description:
        Represents an address book that stores and manages multiple contacts.
    '''

    def __init__(self):
        '''
        Description:
            Initializes an empty AddressBook.
        Parameters:
            None
        Return:
            None
        '''
        self._contacts = {}

    def get_full_name(self, contact):
        '''
        Description:
            Returns the full name of the contact in lowercase format.
        Parameters:
            contact: The contact whose full name is needed.
        Return:
            A string representing the full name in lowercase.
        '''
        return f"{contact.first_name} {contact.last_name}".lower()
    
    def add_contact(self, contact):
        '''
        Description:
            Adds a new contact to the address book.
        Parameters:
            contact: The contact object to be added.
        Return:
            None
        '''
        full_name = self.get_full_name(contact)
        self._contacts[full_name] = contact
        print("Contact added successfully.")

    def find_contact_by_name(self, first_name, last_name):
        '''
        Description:
            Finds and returns a contact by their first and last name.
        Parameters:
            first_name: The first name of the contact.
            last_name: The last name of the contact.
        Return:
            The contact object if found, otherwise None.
        '''
        for contact in self._contacts.values():
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                return contact
        return None

    def edit_contact(self, first_name, last_name):
        '''
        Description:
            Edits the details of an existing contact by prompting the user for new values.
        Parameters:
            first_name: The first name of the contact to edit.
            last_name: The last name of the contact to edit.
        Return:
            None
        '''
        contact = self.find_contact_by_name(first_name, last_name)
        if contact:
            print("Contact found. Enter new details or press Enter to keep current value:")
            new_first_name = input(f"First Name ({contact.first_name}): ") or contact.first_name
            new_last_name = input(f"Last Name ({contact.last_name}): ") or contact.last_name
            new_address = input(f"Address ({contact.address}): ") or contact.address
            new_city = input(f"City ({contact.city}): ") or contact.city
            new_state = input(f"State ({contact.state}): ") or contact.state
            new_zip_code = input(f"ZIP Code ({contact.zip_code}): ") or contact.zip_code
            new_phone = input(f"Phone ({contact.phone}): ") or contact.phone
            new_email = input(f"Email ({contact.email}): ") or contact.email
            # Remove the old entry
            old_full_name = self.get_full_name(contact)
            del self._contacts[old_full_name]
            # Update the contact details
            contact.update_contact(new_first_name, new_last_name, new_address, new_city, new_state, new_zip_code, new_phone, new_email)
            # Add the updated contact with a new key
            new_full_name = self.get_full_name(contact)
            self._contacts[new_full_name] = contact
            contact.update_contact(new_first_name, new_last_name, new_address, new_city, new_state, new_zip_code, new_phone, new_email)
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def remove_contact(self, first_name, last_name):
        '''
        Description:
            Removes a contact from the address book by their full name.
        Parameters:
            first_name: The first name of the contact to remove.
            last_name: The last name of the contact to remove.
        Return:
            None
        '''
        full_name = f"{first_name} {last_name}".lower()
        if full_name in self._contacts:
            del self._contacts[full_name]
            print(f"Contact {first_name} {last_name} removed successfully.")
        else:
            print("Contact not found.")
    
    def display_all_contacts(self):
        '''
        Description:
            Displays all the contacts in the address book.
        Parameters:
            None
        Return:
            None
        '''
        if not self._contacts:
            print("No contacts in Address Book.")
        else:
            for contact in self._contacts.values():
                print(f"\nContact Details:\n"
                      f"Name: {contact.first_name} {contact.last_name}\n"
                      f"Address: {contact.address}, {contact.city}, {contact.state} - {contact.zip_code}\n"
                      f"Phone: {contact.phone}\n"
                      f"Email: {contact.email}\n")

class AddressBookMain:
    '''
    Description:
        The main class for running the Address Book application.
    '''

    def __init__(self):
        ''' 
        Description:
            Initializes the AddressBookMain with an empty AddressBook.
        Parameters:
            None
        Return:
            None
        '''
        self.address_book = AddressBook()

    def menu(self):
        '''
        Description:
            Displays the menu options to the user.
        Parameters:
            None
        Return:
            None
        '''
        print(f'{"-"*10} Select Option {"-"*10}')
        print('1 - Add Contact')
        print('2 - Edit Contact')
        print('3 - Remove Contact')
        print('4 - Display All Contacts')
        print('5 - Exit')

    def get_contact_details(self):
        '''
        Description:
            Prompts the user for contact details and returns a Contact object.
        Parameters:
            None
        Return:
            A Contact object with the provided details.
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
        '''
        Description:
            Runs the main loop of the Address Book application.
        Parameters:
            None
        Return:
            None
        '''
        while True:
            self.menu()
            choice = input("Enter your option: ")
            if choice == '1':
                while True:
                    contact = self.get_contact_details()
                    self.address_book.add_contact(contact)
                    add_another = input("Would you like to add another contact? (y/n): ").lower()
                    if add_another != 'y':
                        break
            elif choice == '2':
                first_name = input("Enter First Name of contact to edit: ")
                last_name = input("Enter Last Name of contact to edit: ")
                self.address_book.edit_contact(first_name, last_name)
            elif choice == '3':
                first_name = input("Enter First Name of contact to remove: ")
                last_name = input("Enter Last Name of contact to remove: ")
                self.address_book.remove_contact(first_name, last_name)
            elif choice == '4': 
                self.address_book.display_all_contacts()
            elif choice == '5': 
                print("Exiting Address Book Program")
                break 
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    app = AddressBookMain()
    app.run()