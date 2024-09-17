import os 


class Contact:
    """
    Description:
        Represents a contact in the address book with personal details.
    Parameters:
        first_name (str): First name of the contact.
        last_name (str): Last name of the contact.
        address (str): Address of the contact.
        city (str): City of the contact.
        state (str): State of the contact.
        zip_code (str): Zip code of the contact.
        phone (str): Phone number of the contact.
        email (str): Email address of the contact.
    Return:
        None
    """
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def to_string(self):
        """
        Description:
            Converts the contact information into a comma-separated string format.
        Parameters:
            Self object as a parameter.
        Return:
            str: Comma-separated string representation of the contact.
        """
        return f"{self.first_name},{self.last_name},{self.address},{self.city},{self.state},{self.zip_code},{self.phone},{self.email}"

    @staticmethod
    def from_string(contact_str):
        """
        Description:
            Converts a comma-separated string into a Contact object.
        Parameters:
            contact_str (str): Comma-separated string representation of a contact.
        Return:
            Contact: A Contact object created from the string.
        """
        fields = contact_str.strip().split(',')
        return Contact(*fields)


class AddressBook:
    """
    Description:
        Manages a collection of contacts, with functionalities to add, remove, find, update, and display contacts.
    Parameters:
        file_name (str): The name of the file where the contacts are stored.
    Return:
        None
    """
    def __init__(self, file_name):
        self.file_name = file_name
        open(self.file_name, 'a').close()  # Create the file if it doesn't exist

    def add_contact(self, contact):
        """
        Description:
            Adds a new contact to the address book file.
        Parameters:
            Self object as a parameter.
            contact (Contact): The Contact object to be added.
        Return:
            None
        """
        with open(self.file_name, 'a') as file:
            file.write(contact.to_string() + '\n')

    def find_contact_by_name(self, first_name, last_name):
        """
        Description:
            Finds a contact by first name and last name.
        Parameters:
            Self object as a parameter.
            first_name (str): First name of the contact to find.
            last_name (str): Last name of the contact to find.
        Return:
            Contact or None: The Contact object if found, else None.
        """
        with open(self.file_name, 'r') as file:
            for line in file:
                contact = Contact.from_string(line)
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    return contact
        return None

    def remove_contact(self, first_name, last_name):
        """
        Description:
            Removes a contact by first name and last name.
        Parameters:
            Self object as a parameter.
            first_name (str): First name of the contact to remove.
            last_name (str): Last name of the contact to remove.
        Return:
            bool: True if a contact was removed, else False.
        """
        contacts = []
        removed = False
        with open(self.file_name, 'r') as file:
            for line in file:
                contact = Contact.from_string(line)
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    removed = True
                else:
                    contacts.append(contact)

        with open(self.file_name, 'w') as file:
            for contact in contacts:
                file.write(contact.to_string() + '\n')

        return removed

    def display_all_contacts(self):
        """
        Description:
            Displays all contacts in the address book.
        Parameters:
            Self object as a parameter.
        Return:
            None
        """
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No contacts in Address Book.")
            else:
                print("\nContacts:")
                for line in lines:
                    contact = Contact.from_string(line)
                    print(f"\nContact Details:\n"
                          f"Name: {contact.first_name} {contact.last_name}\n"
                          f"Address: {contact.address}, {contact.city}, {contact.state} - {contact.zip_code}\n"
                          f"Phone: {contact.phone}\n"
                          f"Email: {contact.email}\n")

    def update_contact(self, first_name, last_name, new_contact):
        """
        Description:
            Updates an existing contact with new information.
        Parameters:
            Self object as a parameter.
            first_name (str): First name of the contact to update.
            last_name (str): Last name of the contact to update.
            new_contact (Contact): The new Contact object with updated information.
        Return:
            bool: True if a contact was updated, else False.
        """
        contacts = []
        updated = False
        with open(self.file_name, 'r') as file:
            for line in file:
                contact = Contact.from_string(line)
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    contacts.append(new_contact)
                    updated = True
                else:
                    contacts.append(contact)

        with open(self.file_name, 'w') as file:
            for contact in contacts:
                file.write(contact.to_string() + '\n')

        return updated

    def search_by_city(self, city):
        """
        Description:
            Searches for contacts by city.
        Parameters:
            Self object as a parameter.
            city (str): The city to search for.
        Return:
            list of Contact: List of contacts residing in the specified city.
        """
        results = []
        with open(self.file_name, 'r') as file:
            for line in file:
                contact = Contact.from_string(line)
                if contact.city.lower() == city.lower():
                    results.append(contact)
        return results

    def search_by_state(self, state):
        """
        Description:
            Searches for contacts by state.
        Parameters:
            Self object as a parameter.
            state (str): The state to search for.
        Return:
            list of Contact: List of contacts residing in the specified state.
        """
        results = []
        with open(self.file_name, 'r') as file:
            for line in file:
                contact = Contact.from_string(line)
                if contact.state.lower() == state.lower():
                    results.append(contact)
        return results

    def sort_contacts(self, key):
        """
        Description:
            Sorts the contacts based on a given attribute (key).
        Parameters:
            Self object as a parameter.
            key (str): The attribute to sort by (e.g., 'first_name', 'city').
        Return:
            list of Contact: Sorted list of contacts.
        """
        with open(self.file_name, 'r') as file:
            contacts = [Contact.from_string(line) for line in file]

        contacts.sort(key=lambda x: getattr(x, key).lower())
        return contacts  # Return sorted contacts for display


class AddressBookSystem:
    """
    Description:
        Manages multiple address books, allowing creation, retrieval, listing, deletion, and searching of address books.
    Parameters:
        None
    Return:
        None
    """
    def __init__(self):
        self.address_books = {}

    def create_address_book(self, name):
        """
        Description:
            Creates a new address book with the specified name.
        Parameters:
            Self object as a parameter.
            name (str): The name of the new address book.
        Return:
            None
        """
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
        else:
            file_name = f"{name}.txt"
            self.address_books[name] = AddressBook(file_name)
            print(f"Address book '{name}' created.")

    def get_address_book(self, name):
        """
        Description:
            Retrieves an address book by its name.
        Parameters:
            Self object as a parameter.
            name (str): The name of the address book to retrieve.
        Return:
            AddressBook or None: The AddressBook object if found, else None.
        """
        return self.address_books.get(name)

    def list_address_books(self):
        """
        Description:
            Lists all available address books.
        Parameters:
            Self object as a parameter.
        Return:
            None
        """
        if self.address_books:
            print("\nAddress Books:")
            for name in self.address_books:
                print(f" - {name}")
        else:
            print("No address books available.")

    def delete_address_book(self, name):
        """
        Description:
            Deletes an address book by its name.
        Parameters:
            Self object as a parameter.
            name (str): The name of the address book to delete.
        Return:
            None
        """
        if name in self.address_books:
            os.remove(self.address_books[name].file_name)
            del self.address_books[name]
            print(f"Address book '{name}' deleted.")
        else:
            print(f"Address book '{name}' not found.")

    def search_by_city(self, city):
        """
        Description:
            Searches for contacts across all address books by city.
        Parameters:
            Self object as a parameter.
            city (str): The city to search for.
        Return:
            None
        """
        found = False
        for book_name, book in self.address_books.items():
            contacts = book.search_by_city(city)
            if contacts:
                print(f"\nContacts in {book_name} from city {city}:")
                for contact in contacts:
                    print(f" - {contact.first_name} {contact.last_name}")
                found = True
        if not found:
            print(f"No contacts found in city {city}.")

    def search_by_state(self, state):
        """
        Description:
            Searches for contacts across all address books by state.
        Parameters:
            Self object as a parameter.
            state (str): The state to search for.
        Return:
            None
        """
        found = False
        for book_name, book in self.address_books.items():
            contacts = book.search_by_state(state)
            if contacts:
                print(f"\nContacts in {book_name} from state {state}:")
                for contact in contacts:
                    print(f" - {contact.first_name} {contact.last_name}")
                found = True
        if not found:
            print(f"No contacts found in state {state}.")

    def count_by_city(self, city):
        """
        Description:
            Counts the total number of contacts from a specified city across all address books.
        Parameters:
            Self object as a parameter.
            city (str): The city to count contacts from.
        Return:
            None
        """
        count = 0
        for book in self.address_books.values():
            count += len(book.search_by_city(city))
        print(f"Total contacts from city {city}: {count}")

    def count_by_state(self, state):
        """
        Description:
            Counts the total number of contacts from a specified state across all address books.
        Parameters:
            Self object as a parameter.
            state (str): The state to count contacts from.
        Return:
            None
        """
        count = 0
        for book in self.address_books.values():
            count += len(book.search_by_state(state))
        print(f"Total contacts from state {state}: {count}")

    def sort_by_name(self):
        """
        Description:
            Sorts and displays contacts by name in all address books.
        Parameters:
            Self object as a parameter.
        Return:
            None
        """
        for book_name, book in self.address_books.items():
            sorted_contacts = book.sort_contacts('first_name')
            print(f"\nContacts sorted by name in {book_name}:")
            if sorted_contacts:
                for contact in sorted_contacts:
                    print(f" - {contact.first_name} {contact.last_name}, {contact.address}, {contact.city}, {contact.state} - {contact.zip_code}, {contact.phone}, {contact.email}")
            else:
                print("No contacts found.")

    def sort_by_city(self):
        """
        Description:
            Sorts and displays contacts by city in all address books.
        Parameters:
            Self object as a parameter.
        Return:
            None
        """
        for book_name, book in self.address_books.items():
            sorted_contacts = book.sort_contacts('city')
            print(f"\nContacts sorted by city in {book_name}:")
            if sorted_contacts:
                for contact in sorted_contacts:
                    print(f" - {contact.first_name} {contact.last_name}, {contact.address}, {contact.city}, {contact.state} - {contact.zip_code}, {contact.phone}, {contact.email}")
            else:
                print("No contacts found.")


class AddressBookMain:
    """
    Description:
        Provides a user interface to interact with the AddressBookSystem and perform various operations.
    Parameters:
        None
    Return:
        None
    """
    def __init__(self):
        self.system = AddressBookSystem()

    def run(self):
        """
        Description:
            Starts the main loop for the user interface, allowing interaction with the address book system.
        Parameters:
            Self object as a parameter.
        Return:
            None
        """
        while True:
            self.menu()
            choice = input("Enter your option: ")
            if choice == '1':
                book_name = input("Enter new Address Book name: ")
                self.system.create_address_book(book_name)
            elif choice == '2':
                book_name = input("Enter the name of the Address Book to select: ")
                if self.system.get_address_book(book_name):
                    self.address_book_menu(book_name)
                else:
                    print(f"Address book '{book_name}' not found.")
            elif choice == '3':
                self.system.list_address_books()
            elif choice == '4':
                book_name = input("Enter the name of the Address Book to delete: ")
                self.system.delete_address_book(book_name)
            elif choice == '5':
                city = input("Enter the name of the City to search for the contacts: ")
                self.system.search_by_city(city)
            elif choice == '6':
                state = input("Enter the name of the State to search for the contacts: ")
                self.system.search_by_state(state)
            elif choice == '7':
                city = input("Enter the name of the City to count the contacts: ")
                self.system.count_by_city(city)
            elif choice == '8':
                state = input("Enter the name of the State to count the contacts: ")
                self.system.count_by_state(state)
            elif choice == '9':
                self.system.sort_by_name()
            elif choice == '10':
                self.system.sort_by_city()
            elif choice == '11':
                print("Exiting Address Book Program")
                break 
            else:
                print("Invalid option. Please try again.")

    def menu(self):
        """
        Description:
            Displays the main menu for the user interface.
        Parameters:
            Self object as a parameter.
        Return:
            None
        """
        print("\nMain Menu:")
        print("1. Create new Address Book")
        print("2. Select an Address Book")
        print("3. List all Address Books")
        print("4. Delete an Address Book")
        print("5. Search contacts by City")
        print("6. Search contacts by State")
        print("7. Count contacts by City")
        print("8. Count contacts by State")
        print("9. Sort contacts by Name")
        print("10. Sort contacts by City")
        print("11. Exit")

    def address_book_menu(self, book_name):
        """
        Description:
            Displays the menu for operations specific to a selected address book.
        Parameters:
            Self object as a parameter.
            book_name (str): The name of the selected address book.
        Return:
            None
        """
        address_book = self.system.get_address_book(book_name)
        while True:
            self.address_book_submenu(book_name)
            choice = input("Enter your option: ")
            if choice == '1':
                self.add_contact(address_book)
            elif choice == '2':
                address_book.display_all_contacts()
            elif choice == '3':
                self.remove_contact(address_book)
            elif choice == '4':
                self.update_contact(address_book)
            elif choice == '5':
                break
            else:
                print("Invalid option. Please try again.")

    def address_book_submenu(self, book_name):
        """
        Description:
            Displays the submenu for operations within a selected address book.
        Parameters:
            Self object as a parameter.
            book_name (str): The name of the selected address book.
        Return:
            None
        """
        print(f"\n--- Address Book: {book_name} ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Remove Contact")
        print("4. Update Contact")
        print("5. Back to Main Menu")

    def add_contact(self, address_book):
        """
        Description:
            Adds a new contact to the specified address book.
        Parameters:
            Self object as a parameter.
            address_book (AddressBook): The AddressBook object to add the contact to.
        Return:
            None
        """
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip code: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        address_book.add_contact(contact)
        print(f"Contact {first_name} {last_name} added to {address_book.file_name}.")

    def remove_contact(self, address_book):
        """
        Description:
            Removes a contact from the specified address book.
        Parameters:
            Self object as a parameter.
            address_book (AddressBook): The AddressBook object to remove the contact from.
        Return:
            None
        """
        first_name = input("Enter first name of contact to remove: ")
        last_name = input("Enter last name of contact to remove: ")
        removed = address_book.remove_contact(first_name, last_name)
        if removed:
            print(f"Contact {first_name} {last_name} removed from {address_book.file_name}.")
        else:
            print(f"Contact {first_name} {last_name} not found in {address_book.file_name}.")

    def update_contact(self, address_book):
        """
        Description:
            Updates an existing contact in the specified address book.
        Parameters:
            Self object as a parameter.
            address_book (AddressBook): The AddressBook object to update the contact in.
        Return:
            None
        """
        first_name = input("Enter first name of contact to update: ")
        last_name = input("Enter last name of contact to update: ")
        contact = address_book.find_contact_by_name(first_name, last_name)
        if contact:
            print(f"Updating contact: {contact.first_name} {contact.last_name}")
            new_first_name = input(f"Enter new first name (or press Enter to keep '{contact.first_name}'): ") or contact.first_name
            new_last_name = input(f"Enter new last name (or press Enter to keep '{contact.last_name}'): ") or contact.last_name
            new_address = input(f"Enter new address (or press Enter to keep '{contact.address}'): ") or contact.address
            new_city = input(f"Enter new city (or press Enter to keep '{contact.city}'): ") or contact.city
            new_state = input(f"Enter new state (or press Enter to keep '{contact.state}'): ") or contact.state
            new_zip_code = input(f"Enter new zip code (or press Enter to keep '{contact.zip_code}'): ") or contact.zip_code
            new_phone = input(f"Enter new phone number (or press Enter to keep '{contact.phone}'): ") or contact.phone
            new_email = input(f"Enter new email (or press Enter to keep '{contact.email}'): ") or contact.email

            new_contact = Contact(new_first_name, new_last_name, new_address, new_city, new_state, new_zip_code, new_phone, new_email)
            updated = address_book.update_contact(first_name, last_name, new_contact)
            if updated:
                print(f"Contact {first_name} {last_name} updated.")
            else:
                print(f"Contact {first_name} {last_name} not found.")
        else:
            print(f"Contact {first_name} {last_name} not found in {address_book.file_name}.")


if __name__ == "__main__":
    app = AddressBookMain()
    app.run()