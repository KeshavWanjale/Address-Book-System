import csv
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

    def to_list(self):
        """
        Description:
            Converts the contact details into a list format suitable for CSV writing.
        Return:
            List[str]: List of contact details in string format.
        """
        return [self.first_name, self.last_name, self.address, self.city, self.state, self.zip_code, self.phone, self.email]

    @staticmethod
    def from_list(contact_list):
        """
        Description:
            Creates a Contact object from a list of contact details.
        Parameters:
            contact_list (List[str]): List of contact details in string format.
        Return:
            Contact: A Contact object initialized with the provided details.
        """
        return Contact(*contact_list)


class AddressBook:
    """
    Description:
        Manages a collection of contacts, with functionality to add, remove, update, and display contacts.
    Parameters:
        file_name (str): The name of the CSV file used to store the address book data.
    Return:
        None
    """

    def __init__(self, file_name):
        self.file_name = file_name
        # Create the file if it doesn't exist
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'Phone', 'Email'])

    def add_contact(self, contact):
        """
        Description:
            Adds a new contact to the address book CSV file.
        Parameters:
            contact (Contact): The contact to be added.
        Return:
            None
        """
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(contact.to_list())

    def find_contact_by_name(self, first_name, last_name):
        """
        Description:
            Searches for a contact by first name and last name in the address book CSV file.
        Parameters:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
        Return:
            Contact: The found contact, or None if not found.
        """
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                contact = Contact.from_list(row)
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    return contact
        return None

    def remove_contact(self, first_name, last_name):
        """
        Description:
            Removes a contact by first name and last name from the address book CSV file.
        Parameters:
            first_name (str): The first name of the contact to be removed.
            last_name (str): The last name of the contact to be removed.
        Return:
            bool: True if the contact was removed, False otherwise.
        """
        contacts = []
        removed = False
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header
            contacts.append(header)  # Add header to new list
            for row in reader:
                contact = Contact.from_list(row)
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    removed = True
                else:
                    contacts.append(row)

        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        return removed

    def display_all_contacts(self):
        """
        Description:
            Displays all contacts in the address book.
        Return:
            None
        """
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header row
            lines = list(reader)
            if not lines:
                print("No contacts in Address Book.")
            else:
                print("\nContacts:")
                for row in lines:
                    contact = Contact.from_list(row)
                    print(f"\nContact Details:\n"
                          f"Name: {contact.first_name} {contact.last_name}\n"
                          f"Address: {contact.address}, {contact.city}, {contact.state} - {contact.zip_code}\n"
                          f"Phone: {contact.phone}\n"
                          f"Email: {contact.email}\n")

    def update_contact(self, first_name, last_name, new_contact):
        """
        Description:
            Updates a contact with new details in the address book CSV file.
        Parameters:
            first_name (str): The first name of the contact to be updated.
            last_name (str): The last name of the contact to be updated.
            new_contact (Contact): The new contact details.
        Return:
            bool: True if the contact was updated, False otherwise.
        """
        contacts = []
        updated = False
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header
            contacts.append(header)  # Add header to new list
            for row in reader:
                contact = Contact.from_list(row)
                if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                    contacts.append(new_contact.to_list())
                    updated = True
                else:
                    contacts.append(row)

        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        return updated

    def search_by_city(self, city):
        """
        Description:
            Searches for contacts by city in the address book CSV file.
        Parameters:
            city (str): The city to search for.
        Return:
            List[Contact]: List of contacts found in the specified city.
        """
        results = []
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                contact = Contact.from_list(row)
                if contact.city.lower() == city.lower():
                    results.append(contact)
        return results

    def search_by_state(self, state):
        """
        Description:
            Searches for contacts by state in the address book CSV file.
        Parameters:
            state (str): The state to search for.
        Return:
            List[Contact]: List of contacts found in the specified state.
        """
        results = []
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                contact = Contact.from_list(row)
                if contact.state.lower() == state.lower():
                    results.append(contact)
        return results

    def sort_contacts(self, key):
        """
        Description:
            Sorts contacts in the address book by a specified key.
        Parameters:
            key (str): The key by which to sort the contacts (e.g., 'first_name', 'city').
        Return:
            List[List[str]]: List of rows with sorted contacts, including the header row.
        """
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header
            contacts = [Contact.from_list(row) for row in reader]

        contacts.sort(key=lambda x: getattr(x, key).lower())
        return [header] + [contact.to_list() for contact in contacts]  # Return sorted contacts with header


class AddressBookSystem:
    """
    Description:
        Manages multiple address books, allowing users to create, list, delete address books and perform operations such as searching, counting, and sorting contacts across all address books.
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
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
        else:
            file_name = f"{name}.csv"
            self.address_books[name] = AddressBook(file_name)
            print(f"Address book '{name}' created.")

    def get_address_book(self, name):
        """
        Description:
            Retrieves an address book by its name.
        Parameters:
            name (str): The name of the address book to retrieve.
        Return:
            AddressBook: The address book with the specified name, or None if not found.
        """
        return self.address_books.get(name)

    def list_address_books(self):
        """
        Description:
            Lists all address books managed by the system.
        Return:
            None
        """
        if self.address_books:
            print("\nAddress Books:")
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
            with open(address_book.file_name, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    contact = Contact.from_list(row)
                    all_contacts.append(contact)

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
            with open(address_book.file_name, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    contact = Contact.from_list(row)
                    all_contacts.append(contact)

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

    def remove_contact(self, address_book):
        """
        Description:
            Prompts the user for the contact details to remove and attempts to remove the contact from the selected address book.
        Parameters:
            address_book (AddressBook): The address book from which the contact will be removed.
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
            Prompts the user for the details of the contact to update and applies the changes to the selected address book.
        Parameters:
            address_book (AddressBook): The address book containing the contact to be updated.
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