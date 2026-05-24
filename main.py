import pickle
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
            
        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) >= 2:
                name, phone = args[0], args[1]
                record = book.find(name)
                if record is None:
                    record = Record(name)
                    book.add_record(record)
                record.add_phone(phone)
                print("Contact added.")
            else:
                print("Invalid command.")

        elif command == "all":
            if not book.data:
                print("Address book is empty.")
            else:
                for record in book.data.values():
                    print(record)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()