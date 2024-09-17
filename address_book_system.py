import json
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

    def to_dict(self):
        """
        Description:
            Converts the Contact object to a dictionary.
        Return:
            dict: A dictionary representation of the Contact object.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, data):
        """
        Description:
            Creates a Contact object from a dictionary.
        Parameters:
            data (dict): A dictionary containing contact details.
        Return:
            Contact: A Contact object created from the dictionary.
        """
        return cls(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            zip_code=data['zip_code'],
            phone=data['phone'],
            email=data['email']
        )
    

class AddressBook:
    """
    Description:
        Represents an address book that stores contacts in a JSON file.
    Parameters:
        file_name (str): The name of the JSON file where contacts are stored.
    Return:
        None
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Description:
            Loads contacts from the JSON file.
        Return:
            List[Contact]: A list of Contact objects.
        """
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return [Contact(**contact) for contact in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        """
        Description:
            Saves all contacts to the JSON file.
        Return:
            None
        """
        with open(self.file_name, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def add_contact(self, contact):
        """
        Description:
            Adds a contact to the address book and saves it to the JSON file.
        Parameters:
            contact (Contact): The contact to add.
        Return:
            None
        """
        self.contacts.append(contact)
        self.save_contacts()

    def remove_contact(self, first_name, last_name):
        """
        Description:
            Removes a contact by first and last name from the address book and saves the updated list to the JSON file.
        Parameters:
            first_name (str): The first name of the contact to remove.
            last_name (str): The last name of the contact to remove.
        Return:
            bool: True if the contact was removed, False if not found.
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False

    def update_contact(self, first_name, last_name, new_contact):
        """
        Description:
            Updates a contact's information and saves the changes to the JSON file.
        Parameters:
            first_name (str): The first name of the contact to update.
            last_name (str): The last name of the contact to update.
            new_contact (Contact): The new contact information.
        Return:
            bool: True if the contact was updated, False if not found.
        """
        for i, contact in enumerate(self.contacts):
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts[i] = new_contact
                self.save_contacts()
                return True
        return False

    def find_contact_by_name(self, first_name, last_name):
        """
        Description:
            Finds a contact by first and last name.
        Parameters:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
        Return:
            Contact: The contact if found, otherwise None.
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def search_by_city(self, city):
        """
        Description:
            Searches for contacts by city.
        Parameters:
            city (str): The city to search for.
        Return:
            List[Contact]: A list of contacts in the specified city.
        """
        return [contact for contact in self.contacts if contact.city.lower() == city.lower()]

    def search_by_state(self, state):
        """
        Description:
            Searches for contacts by state.
        Parameters:
            state (str): The state to search for.
        Return:
            List[Contact]: A list of contacts in the specified state.
        """
        return [contact for contact in self.contacts if contact.state.lower() == state.lower()]
    

class AddressBookSystem:
    """
    Description:
        Manages multiple address books, providing functionality to create, list, delete, and access individual address books.
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
            name (str): The name of the new address book.
        Return:
            None
        """
        if name not in self.address_books:
            self.address_books[name] = AddressBook(f"{name}.json")
            print(f"Address book '{name}' created.")
        else:
            print(f"Address book '{name}' already exists.")

    def get_address_book(self, name):
        """
        Description:
            Retrieves an address book by its name.
        Parameters:
            name (str): The name of the address book.
        Return:
            AddressBook: The address book if found, otherwise None.
        """
        return self.address_books.get(name)

    def list_address_books(self):
        """
        Description:
            Lists all available address books.
        Parameters:
            None
        Return:
            None
        """
        if self.address_books:
            print("Available Address Books:")
            for name in self.address_books:
                print(f"- {name}")
        else:
            print("No address books available.")

    def delete_address_book(self, name):
        """
        Description:
            Deletes an address book by its name.
        Parameters:
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
            Searches for contacts in all address books by city.
        Parameters:
            city (str): The city to search for.
        Return:
            None
        """
        found = False
        for address_book in self.address_books.values():
            contacts = address_book.search_by_city(city)
            if contacts:
                found = True
                print(f"\nContacts in City '{city}':")
                for contact in contacts:
                    print(f"Name: {contact.first_name} {contact.last_name}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip: {contact.zip_code}, Phone: {contact.phone}, Email: {contact.email}")

        if not found:
            print(f"No contacts found in City '{city}'.")

    def search_by_state(self, state):
        """
        Description:
            Searches for contacts in all address books by state.
        Parameters:
            state (str): The state to search for.
        Return:
            None
        """
        found = False
        for address_book in self.address_books.values():
            contacts = address_book.search_by_state(state)
            if contacts:
                found = True
                print(f"\nContacts in State '{state}':")
                for contact in contacts:
                    print(f"Name: {contact.first_name} {contact.last_name}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip: {contact.zip_code}, Phone: {contact.phone}, Email: {contact.email}")

        if not found:
            print(f"No contacts found in State '{state}'.")

    def count_by_city(self, city):
        """
        Description:
            Counts the number of contacts in all address books by city.
        Parameters:
            city (str): The city to count contacts for.
        Return:
            None
        """
        count = 0
        for address_book in self.address_books.values():
            contacts = address_book.search_by_city(city)
            count += len(contacts)

        print(f"\nNumber of contacts in City '{city}': {count}")

    def count_by_state(self, state):
        """
        Description:
            Counts the number of contacts in all address books by state.
        Parameters:
            state (str): The state to count contacts for.
        Return:
            None
        """
        count = 0
        for address_book in self.address_books.values():
            contacts = address_book.search_by_state(state)
            count += len(contacts)

        print(f"\nNumber of contacts in State '{state}': {count}")

    def sort_by_name(self):
        """
        Description:
            Sorts and displays all contacts in all address books by their name.
        Parameters:
            None
        Return:
            None
        """
        all_contacts = []
        for address_book in self.address_books.values():
            all_contacts.extend(address_book.contacts)

        all_contacts.sort(key=lambda x: (x.first_name.lower(), x.last_name.lower()))
        print("\nContacts sorted by Name:")
        for contact in all_contacts:
            print(f"Name: {contact.first_name} {contact.last_name}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip: {contact.zip_code}, Phone: {contact.phone}, Email: {contact.email}")

    def sort_by_city(self):
        """
        Description:
            Sorts and displays all contacts in all address books by their city.
        Parameters:
            None
        Return:
            None
        """
        all_contacts = []
        for address_book in self.address_books.values():
            all_contacts.extend(address_book.contacts)

        all_contacts.sort(key=lambda x: x.city.lower())
        print("\nContacts sorted by City:")
        for contact in all_contacts:
            print(f"Name: {contact.first_name} {contact.last_name}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip: {contact.zip_code}, Phone: {contact.phone}, Email: {contact.email}")


class AddressBookMain:
    """
    Description:
        Manages the main user interface for the address book system, allowing users to create, select, list, delete, and manage address books and contacts.
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
            Runs the main loop of the address book application, presenting the user with a menu of options and executing the selected actions.
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
            Displays the main menu options for the address book application.
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
            Displays the menu options for a selected address book, allowing users to add, display, remove, update contacts, or return to the main menu.
        Parameters:
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
                self.display_contacts(address_book)
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
            Displays the submenu options for managing contacts within a selected address book.
        Parameters:
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
            Prompts the user for contact details and adds a new contact to the selected address book.
        Parameters:
            address_book (AddressBook): The address book to which the contact will be added.
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

    def display_contacts(self, address_book):
        """
        Description:
            Displays all contacts in the selected address book.
        Parameters:
            address_book (AddressBook): The address book whose contacts are to be displayed.
        Return:
            None
        """
        contacts = address_book.contacts
        if contacts:
            print("\nContacts:")
            for contact in contacts:
                print(f"Name: {contact.first_name} {contact.last_name}, Address: {contact.address}, City: {contact.city}, State: {contact.state}, Zip: {contact.zip_code}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("No contacts available.")

    def remove_contact(self, address_book):
        """
        Description:
            Prompts the user for the name of a contact to remove from the selected address book.
        Parameters:
            address_book (AddressBook): The address book from which the contact will be removed.
        Return:
            None
        """
        first_name = input("Enter first name of the contact to remove: ")
        last_name = input("Enter last name of the contact to remove: ")
        if address_book.remove_contact(first_name, last_name):
            print(f"Contact {first_name} {last_name} removed from {address_book.file_name}.")
        else:
            print(f"Contact {first_name} {last_name} not found in {address_book.file_name}.")

    def update_contact(self, address_book):
        """
        Description:
            Prompts the user for the current and new details of a contact and updates it in the selected address book.
        Parameters:
            address_book (AddressBook): The address book where the contact will be updated.
        Return:
            None
        """
        first_name = input("Enter first name of the contact to update: ")
        last_name = input("Enter last name of the contact to update: ")
        contact = address_book.find_contact_by_name(first_name, last_name)
        if contact:
            print("Enter new details (leave blank to keep current value):")
            new_first_name = input(f"New first name [{contact.first_name}]: ") or contact.first_name
            new_last_name = input(f"New last name [{contact.last_name}]: ") or contact.last_name
            new_address = input(f"New address [{contact.address}]: ") or contact.address
            new_city = input(f"New city [{contact.city}]: ") or contact.city
            new_state = input(f"New state [{contact.state}]: ") or contact.state
            new_zip_code = input(f"New zip code [{contact.zip_code}]: ") or contact.zip_code
            new_phone = input(f"New phone number [{contact.phone}]: ") or contact.phone
            new_email = input(f"New email [{contact.email}]: ") or contact.email
            new_contact = Contact(new_first_name, new_last_name, new_address, new_city, new_state, new_zip_code, new_phone, new_email)
            if address_book.update_contact(first_name, last_name, new_contact):
                print(f"Contact {first_name} {last_name} updated.")
            else:
                print(f"Contact {first_name} {last_name} not found.")
        else:
            print(f"Contact {first_name} {last_name} not found.")


if __name__ == "__main__":
    app = AddressBookMain()
    app.run()