"""
Даты добавления файла:

Дата - 11.03.2025

Описание задачи:

Картотека — класс для хранения и поиска информации о людях (имя, адрес, телефон).
"""

import pickle

FILE_NAME = "people.pkl"

def load_people():
    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_people(people):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(people, file)

class DataBase:
    def __init__(self):
        self.people = load_people()

    def all_persone(self):
        print("\n----- Картотека -----")
        if not self.people:
            print("Картотека пуста")
        else:
            for name, data in self.people.items():
                print(f"Имя: {name}")
                print(f"Адрес: {data['address']}")
                print(f"Телефон: {data['phone']}")
                print("----------------------")

    def find_persone(self, name):
        if name in self.people:
            return self.people[name]
        else:
            print(f"Человек с именем {name} не найден")
            return None

    def add_persone(self, name, address, phone):
        self.people[name] = {"address": address, "phone": phone}
        save_people(self.people)

    def edit_person(self):
        name = input("\nВведите имя человека, которого хотите изменить - ").strip()
        if name in self.people:
            new_address = input("Введите новый адрес (Enter, чтобы оставить без изменений) - ").strip()
            new_phone = input("Введите новый телефон (Enter, чтобы оставить без изменений) - ").strip()
            if new_address:
                self.people[name]["address"] = new_address
            if new_phone:
                self.people[name]["phone"] = new_phone
            save_people(self.people)
            print(f"Информация о {name} обновлена.")
        else:
            print(f"Человек с именем {name} не найден.")

    def del_person(self):
        name = input("\nВведите имя человека, которого хотите удалить - ").strip()
        if name in self.people:
            del self.people[name]
            save_people(self.people)
            print(f"\n{name} успешно удалён")
        else:
            print(f"\nЧеловек с именем {name} не найден")

class Main:
    db = DataBase()

    while True:
        print("\nМеню")
        print("1. Список всех людей")
        print("2. Найти информацию о человеке")
        print("3. Добавить нового человека")
        print("4. Изменить информацию о человеке")
        print("5. Удалить человека из списка")
        print("6. Выйти")

        choice = input("Выберите действие - ").strip().lower()

        if choice == "1" or choice == "список всех людей":
            db.all_persone()
        elif choice == "2" or choice == "найти информацию о человеке":
            name = input("\nВведите имя человека для поиска - ").strip()
            person = db.find_persone(name)
            if person:
                print(f"Имя: {name}")
                print(f"Адрес: {person['address']}")
                print(f"Телефон: {person['phone']}")
        elif choice == "3" or choice == "добавить нового человека":
            name = input("\nВведите имя человека - ").strip()
            address = input("Введите адрес человека - ").strip()
            phone = input("Введите номер человека - ").strip()
            db.add_persone(name, address, phone)
        elif choice == "4" or choice == "изменить информацию о человеке":
            db.edit_person()
        elif choice == "5" or choice == "удалить человека из списка":
            db.del_person()
        elif choice == "6" or choice == "выйти":
            print("\nДо встречи!")
            break
        else:
            print("\nНеверный ввод, попробуйте снова")

if __name__ == "__main__":
    Main()