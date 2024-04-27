def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(contacts, name=None, phone=None):
    if not name or not phone:
        return "Invalid arguments!"
    if name in contacts:
        return "Contact with this name already exists!"
    contacts[name] = phone
    return "Contact added."

def get_phone(contacts, name=None):
    if not name:
        return "Invalid arguments!"
    if name not in contacts:
        return "Contact with this name does not exist!"
    return contacts[name]

def change_contact(contacts, name=None, phone=None):
    if not name or not phone:
        return "Invalid arguments!"
    if name not in contacts:
        return "Contact with this name does not exist!"
    contacts[name] = phone
    return "Contact changed."

def all(contacts):
    return "\n".join([f"Name: {name}, phone: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(contacts, *args))
        elif command == "change":
            print(change_contact(contacts, *args))
        elif command == "phone":
            print(get_phone(contacts, *args))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()