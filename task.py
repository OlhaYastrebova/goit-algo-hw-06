from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        if not self._validate(value):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

    def _validate(self, value):
        return value.isdigit() and len(value) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = self.find_phone(old_phone)
        if old_phone_obj:
            self.phones.remove(old_phone_obj)
            self.add_phone(new_phone)
        else:
            raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
# Створення нової адресної книги
    # Приклад використання
address_book = AddressBook() 

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
address_book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
address_book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(address_book)

    # Знаходження та редагування телефону для John
john = address_book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
address_book.delete("Jane")