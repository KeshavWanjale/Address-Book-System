def display_welcome():
    print("Welcome to Address Book Program")

def create_contact():
   
    contact = {}
    contact['first_name'] = input("Enter First Name: ")
    contact['last_name'] = input("Enter Last Name: ")
    contact['address'] = input("Enter Address: ")
    contact['city'] = input("Enter City: ")
    contact['state'] = input("Enter State: ")
    contact['zip_code'] = input("Enter ZIP Code: ")
    contact['phone'] = input("Enter Phone Number: ")
    contact['email'] = input("Enter Email: ")

    return contact

def display_contact(contact):
    
    print("\nContact Details:")
    print(f"Name: {contact['first_name']} {contact['last_name']}")
    print(f"Address: {contact['address']}, {contact['city']}, {contact['state']} - {contact['zip_code']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}\n")

if __name__ == "__main__":
    display_welcome()
    new_contact = create_contact()
    display_contact(new_contact)
