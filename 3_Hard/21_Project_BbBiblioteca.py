"""
Дата добавления файла:

Дата - 15.03.2025

Описание задачи:

Система управления библиотекой — создание системы для учета книг и пользователей библиотеки.
"""

import pickle
import uuid
import os
from typing import List, Optional

class Book:
    def __init__(self, title, author, isbn=None):
        self.title = title
        self.author = author
        self.isbn = isbn if isbn else str(uuid.uuid4())
        self.available = True

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {self.available})"

    def __str__(self):
        return f"{self.title} ({self.author}) - {'Доступна' if self.available else 'Занята'}"

    def is_available(self):
        return self.available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Книга '{self.title}' выдана читателю.")
        else:
            print(f"Ошибка: Книга '{self.title}' уже занята.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Книга '{self.title}' успешно возвращена в библиотеку.")
        else:
            print(f"Книга '{self.title}' уже находится в библиотеке.")

class User:
    def __init__(self, name: str, user_id: str = None):
        self.name = name
        self.user_id = user_id if user_id else str(uuid.uuid4())
        self.borrowed_books: List[Book] = []

    def __repr__(self):
        return f"User({self.name}, ID: {self.user_id}, Books: {[book.title for book in self.borrowed_books]})"

    def __str__(self):
        return f"Пользователь: {self.name}, ID: {self.user_id}"

    def borrow_book(self, book: 'Book', library: 'Library'):
        if book not in library.books:
            print(f"Ошибка: Книга '{book.title}' отсутствует в библиотеке.")
            return
        if book in self.borrowed_books:
            print(f"Ошибка: Вы уже взяли книгу '{book.title}'.")
            return
        if book.is_available():
            book.borrow()
            self.borrowed_books.append(book)
            print(f"Книга '{book.title}' успешно взята пользователем {self.name}.")
        else:
            print(f"Ошибка: Книга '{book.title}' уже занята.")

    def return_book(self, book: 'Book', library: 'Library'):
        if book not in library.books:
            print(f"Ошибка: Книга '{book.title}' больше не принадлежит библиотеке.")
            return
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"Книга '{book.title}' успешно возвращена в библиотеку.")
        else:
            print(f"Ошибка: У вас нет книги '{book.title}'.")

    def get_borrowed_books(self) -> List[str]:
        return [book.title for book in self.borrowed_books]

class Admin(User):
    def __init__(self, name: str, user_id: str = None):
        super().__init__(name, user_id)
        self.is_admin = True

    def add_book(self, library: 'Library', book: 'Book'):
        if any(b.isbn == book.isbn for b in library.books):
            print(f"Ошибка: Книга с ISBN {book.isbn} уже есть в библиотеке.")
            return
        library.add_book(book)
        print(f"Книга '{book.title}' успешно добавлена в библиотеку.")

    def remove_book(self, library: 'Library', book: 'Book'):
        if book in library.books:
            if book.is_available():
                library.remove_book(book)
                print(f"🗑 Книга '{book.title}' удалена из библиотеки.")
            else:
                print(f"Ошибка: Книга '{book.title}' сейчас занята и не может быть удалена.")
        else:
            print("Ошибка: Книга не найдена в библиотеке.")

class Library:
    def __init__(self, filename="library.pkl"):
        self.filename = filename
        self.books: List[Book] = []
        self.users: List[User] = []
        self.load_data()

    def save_data(self):
        try:
            with open(self.filename, "wb") as file:
                pickle.dump({"books": self.books, "users": self.users}, file)
            print("Данные библиотеки сохранены.")
        except IOError:
            print("Ошибка: Не удалось сохранить данные библиотеки.")

    def load_data(self):
        try:
            with open(self.filename, "rb") as file:
                data = pickle.load(file)

            if isinstance(data, dict):
                self.books = data.get("books", [])
                self.users = data.get("users", [])
            elif isinstance(data, Library):
                self.books = data.books
                self.users = data.users
            else:
                raise ValueError("Ошибка: Некорректный формат данных.")

            print("Данные библиотеки загружены.")

        except (FileNotFoundError, EOFError):
            print("Файл данных не найден или поврежден. Создана новая библиотека.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def add_book(self, book: Book):
        if any(b.isbn == book.isbn for b in self.books):
            print(f"Ошибка: Книга '{book.title}' уже есть в библиотеке.")
        else:
            self.books.append(book)
            self.save_data()
            print(f"Книга '{book.title}' добавлена в библиотеку.")

    def remove_book(self, book: Book):
        if book in self.books:
            if book.is_available():
                self.books.remove(book)
                self.save_data()
                print(f"Книга '{book.title}' удалена из библиотеки.")
            else:
                print(f"Ошибка: Книга '{book.title}' сейчас занята и не может быть удалена.")
        else:
            print(f"Ошибка: Книга '{book.title}' не найдена в библиотеке.")

    def register_user(self, name: str, role: str) -> Optional[User]:
        if name.lower() in ["q", "отмена"]:
            print("Регистрация отменена.")
            return None

        existing_user = next((user for user in self.users if user.name.lower() == name.lower()), None)
        if existing_user:
            print(f"Ошибка: Пользователь '{name}' уже зарегистрирован.")
            return existing_user

        user_id = str(uuid.uuid4())
        new_user = Admin(name, user_id) if role.lower() == "admin" else User(name, user_id)

        self.users.append(new_user)
        self.save_data()
        print(f"{role.capitalize()} {name} зарегистрирован с ID: {user_id}")
        return new_user

    def authenticate(self, user_id: str) -> Optional[User]:
        if user_id.lower() in ["q", "отмена"]:
            print("Вход отменён.")
            return None

        user = next((user for user in self.users if user.user_id == user_id), None)
        if user is None:
            print("Ошибка: Пользователь с таким ID не найден.")
        return user

    def lend_book(self, user: User, book: Book):
        if book not in self.books:
            print(f"Ошибка: Книга '{book.title}' отсутствует в библиотеке.")
            return
        if book.is_available():
            user.borrow_book(book, self)
            self.save_data()
        else:
            print("Ошибка: Книга уже занята.")

    def accept_return(self, user: User, book: Book):
        if book in user.borrowed_books:
            user.return_book(book, self)
            self.save_data()
        else:
            print("Ошибка: Книга не была взята этим пользователем.")

    def list_available_books(self) -> str:
        available_books = [book for book in self.books if book.is_available()]
        if available_books:
            result = "Доступные книги:\n" + "\n".join(f"- {book.title} ({book.author})" for book in available_books)
            print(result)
            return result
        else:
            print("Нет доступных книг в библиотеке.")
            return "Нет доступных книг."

def clear_screen():
    print("\033[H\033[J", end="")

def main_menu():
    library = Library()
    commands = {
        "1": "войти", "войти": "1",
        "2": "зарегистрироваться", "зарегистрироваться": "2",
        "3": "выйти", "выйти": "3"
    }

    while True:
        clear_screen()
        print("\n=== БИБЛИОТЕКА ===")
        print("Выберите действие:")
        for num, cmd in commands.items():
            if num.isdigit():
                print(f"{num}. {cmd.capitalize()}")

        choice = input("Введите команду (номер или слово): ").strip().lower()
        print(f"DEBUG: Введено '{choice}'")

        if choice in commands:
            choice = commands[choice]
        print(f"DEBUG: После обработки '{choice}'")

        if choice == "1":
            user_id = input("Введите ваш user ID: ").strip()
            user = library.authenticate(user_id)
            if user:
                user_menu(library, user)
            else:
                print("Ошибка: пользователь не найден.")
                input("Нажмите Enter, чтобы продолжить...")

        elif choice == "2":
            name = input("Введите ваше имя: ").strip()
            role = input("Выберите роль (user/admin): ").strip().lower()
            if role in ["user", "admin"]:
                user = library.register_user(name, role)
                if user:
                    user_menu(library, user)
            else:
                print("Ошибка: некорректная роль.")
                input("Нажмите Enter, чтобы продолжить...")

        elif choice == "3":
            library.save_data()
            print("Данные сохранены. До свидания!")
            break

        else:
            print("Ошибка: выберите корректный вариант.")
            input("Нажмите Enter, чтобы продолжить...")

def user_menu(library, user):

    commands = {
        "1": "взять книгу", "взять книгу": "1",
        "2": "вернуть книгу", "вернуть книгу": "2",
        "3": "список доступных книг", "список доступных книг": "3",
        "4": "выйти", "выйти": "4"
    }

    if isinstance(user, Admin):
        admin_commands = {
            "5": "добавить книгу", "добавить книгу": "5",
            "6": "удалить книгу", "удалить книгу": "6"
        }
        commands.update(admin_commands)

    while True:
        clear_screen()
        print(f"\nВы вошли как {user.name} ({'Admin' if isinstance(user, Admin) else 'User'})")
        print("=== Меню ===")
        for num, cmd in commands.items():
            if num.isdigit():
                print(f"{num}. {cmd.capitalize()}")

        choice = input("Введите команду (номер или слово): ").strip().lower()
        choice = commands.get(choice, choice)

        if choice == "1":
            book_title = input("Введите название книги: ").strip()
            book = next((b for b in library.books if b.title.lower() == book_title.lower()), None)
            if book:
                library.lend_book(user, book)
            else:
                print("Ошибка: книга не найдена.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choice == "2":
            book_title = input("Введите название книги: ").strip()
            book = next((b for b in user.borrowed_books if b.title.lower() == book_title.lower()), None)
            if book:
                library.accept_return(user, book)
            else:
                print("Ошибка: у вас нет этой книги.")
            input("Нажмите Enter, чтобы продолжить...")

        elif choice == "3":
            library.list_available_books()
            input("Нажмите Enter, чтобы продолжить...")

        elif choice == "4":
            print("Выход в главное меню...")
            library.save_data()
            break

        elif choice == "5" and isinstance(user, Admin):
            book_title = input("Введите название книги: ").strip()
            book_author = input("Введите автора книги: ").strip()
            book_isbn = input("Введите ISBN книги (или оставьте пустым для автогенерации): ").strip()

            if not book_isbn:
                book_isbn = str(uuid.uuid4())

            new_book = Book(book_title, book_author, book_isbn)
            user.add_book(library, new_book)
            input("Нажмите Enter, чтобы продолжить...")

        elif choice == "6" and isinstance(user, Admin):
            book_title = input("Введите название книги для удаления: ").strip()
            book = next((b for b in library.books if b.title.lower() == book_title.lower()), None)
            if book:
                user.remove_book(library, book)
            else:
                print("Ошибка: книга не найдена.")
            input("Нажмите Enter, чтобы продолжить...")

        else:
            print("Ошибка: выберите корректный вариант.")
            input("Нажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main_menu()