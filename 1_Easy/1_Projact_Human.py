"""
Дата добавления файла:

Дата - 15.02.2025

Описания задачи:

Класс “Человек” — создайте класс с атрибутами (имя, возраст) и методами (приветствие, изменение возраста).
"""

class Human:
    # Конструктор класса, инициализирующий объект с параметрами name и age
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    # Метод для инициализации данных экземпляра через ввод пользователя
    def add_human(self):
        self.name = input("Введите имя - ")  # Получение имени через стандартный ввод
        self.age = input("Введите возраст - ")  # Получение возраста через стандартный ввод
        print("Данные сохранены")

    # Метод для обновления имени экземпляра с проверкой на совпадение текущего значения
    def edit_name(self, new_name):
        if new_name != self.name:  # Валидация: новое имя должно отличаться от текущего
            self.name = new_name  # Присвоение нового имени
            print("Новое имя сохранено")
        else:
            print("ОШИБКА: Данное имя уже зарегистрировано")

    # Метод для обновления возраста экземпляра с проверкой на совпадение текущего значения
    def edit_age(self, new_age):
        if new_age != self.age:  # Валидация: новый возраст должен отличаться от текущего
            self.age = new_age  # Присвоение нового возраста
            print("Новый возраст зарегистрирован")
        else:
            print("ОШИБКА: Данный возраст уже зарегистрирован")

    # Метод для предоставления строкового представления объекта
    def __str__(self):
        return f"Вас зовут - {self.name} и вам {self.age} лет"

# Основная функция, реализующая консольный интерфейс взаимодействия с пользователем

def main():
    h = Human()  # Создание экземпляра класса Human

    while True:  # Организация бесконечного цикла для работы с меню
        print("\n=== МЕНЮ ===")
        print("1) Добавить информацию о человеке")
        print("2) Вывести информацию о человеке")
        print("3) Изменить имя")
        print("4) Изменить возраст")
        print("5) Выйти")

        # Получение команды от пользователя с нормализацией регистра и удаления лишних пробелов
        choice = input("Введите номер команды или саму команду - ").lower().strip()

        if choice == "1" or choice == "добавить информацию о человеке":
            h.add_human()  # Вызов метода инициализации данных экземпляра

        elif choice == "2" or choice == "вывести информацию о человеке":
            print(h)  # Вывод строкового представления объекта

        elif choice == "3" or choice == "изменить имя":
            new_name = input("Введите новое имя: ").strip()
            h.edit_name(new_name)  # Вызов метода для обновления имени экземпляра

        elif choice == "4" or choice == "изменить возраст":
            new_age = input("Введите новый возраст: ").strip()
            h.edit_age(new_age)  # Вызов метода для обновления возраста экземпляра

        elif choice == "5" or choice == "выйти":
            print("До свидания!")
            break  # Завершение работы программы

        else:
            print("ОШИБКА: Вы ввели некорректную команду, попробуйте ещё раз.")

# Проверка, является ли файл исполняемым скриптом, а не импортированным модулем
if __name__ == "__main__":
    main()  # Запуск главной функции