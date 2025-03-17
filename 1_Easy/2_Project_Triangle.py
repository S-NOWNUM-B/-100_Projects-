"""
Дата добавления файла:

Дата - 15.02.2025

Описания задачи:

Треугольник — класс для работы с треугольниками, метод для вычисления площади.
"""

from math import sqrt  # Импортируем функцию sqrt (квадратный корень) из модуля math


# Основной класс для треугольников, содержащий стороны и высоту
class Triangle:
    def __init__(self, a=None, b=None, c=None, h=None):
        self.a = a  # Сторона a
        self.b = b  # Сторона b
        self.c = c  # Сторона c
        self.h = h  # Высота h


# Класс для вычислений, наследуется от Triangle
class Calculate(Triangle):
    def __init__(self, a=None, b=None, c=None, h=None):
        super().__init__(a, b, c, h)  # Наследуем переменные из родительского класса

    # Метод вычисления площади равностороннего треугольника по стороне
    def rav_star_first(self):
        return (sqrt(3) / 4) * self.a ** 2

    # Метод вычисления площади равнобедренного треугольника по основанию и высоте
    def rav_tr_first(self):
        return (1 / 2) * (self.a * self.h)

    # Метод вычисления площади равнобедренного треугольника по стороне
    def rav_tr_second(self):
        return ((self.a ** 2) * sqrt(3)) / 4

    # Метод вычисления площади прямоугольного треугольника по катету и высоте
    def pr_tr_first(self):
        return (1 / 2) * (self.a * self.h)

    # Метод вычисления площади прямоугольного треугольника по двум катетам
    def pr_tr_second(self):
        return (1 / 2) * (self.a * self.b)

    # Метод вычисления площади треугольника по формуле Герона
    def pr_tr_third(self):
        p = (self.a + self.b + self.c) / 2  # Полупериметр
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # Формула Герона


# Главное меню программы
def menu():
    while True:
        print("\n===== ГЛАВНОЕ МЕНЮ =====")
        print("1) Рассчитать площадь равностороннего треугольника")
        print("2) Рассчитать площадь равнобедренного треугольника")
        print("3) Рассчитать площадь прямоугольного треугольника")
        print("4) Выйти из программы")

        choice = input("Введите номер команды: ")  # Ввод выбора

        if choice == "1":
            submenu_equilateral()
        elif choice == "2":
            submenu_isosceles()
        elif choice == "3":
            submenu_right()
        elif choice == "4":
            print("\nВыход из программы...")
            break  # Завершение работы программы
        else:
            print("\nНекорректный ввод, попробуйте снова.")


# Подменю для равностороннего треугольника
def submenu_equilateral():
    print("\n===== РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК =====")
    print("1) Площадь через длину стороны")
    print("2) Назад")

    choice = input("Выберите способ расчёта: ")

    if choice == "1":
        a = float(input("\nВведите сторону треугольника: "))  # Ввод стороны
        calc = Calculate(a=a)  # Создаём объект
        print("\n====================")
        print(f"Площадь: {calc.rav_star_first()}")  # Вывод результата
        print("====================")
    elif choice == "2":
        return  # Возврат в главное меню
    else:
        print("Некорректный ввод, попробуйте снова.")


# Подменю для равнобедренного треугольника
def submenu_isosceles():
    print("\n===== РАВНОБЕДРЕННЫЙ ТРЕУГОЛЬНИК =====")
    print("1) Площадь через основание и высоту")
    print("2) Площадь через сторону и угол")
    print("3) Назад")

    choice = input("Выберите способ расчёта: ")

    if choice == "1":
        a = float(input("\nВведите основание: "))
        h = float(input("Введите высоту: "))
        calc = Calculate(a=a, h=h)
        print("\n====================")
        print(f"Площадь: {calc.rav_tr_first()}")
        print("====================")
    elif choice == "2":
        a = float(input("\nВведите сторону: "))
        calc = Calculate(a=a)
        print("\n====================")
        print(f"Площадь: {calc.rav_tr_second()}")
        print("====================")
    elif choice == "3":
        return
    else:
        print("Некорректный ввод, попробуйте снова.")


# Подменю для прямоугольного треугольника
def submenu_right():
    print("\n===== ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК =====")
    print("1) Площадь через катет и высоту")
    print("2) Площадь через две стороны")
    print("3) Площадь через формулу Герона")
    print("4) Назад")

    choice = input("Выберите способ расчёта: ")

    if choice == "1":
        a = float(input("\nВведите катет: "))
        h = float(input("Введите высоту: "))
        calc = Calculate(a=a, h=h)
        print("\n====================")
        print(f"Площадь: {calc.pr_tr_first()}")
        print("====================")
    elif choice == "2":
        a = float(input("\nВведите первый катет: "))
        b = float(input("Введите второй катет: "))
        calc = Calculate(a=a, b=b)
        print("\n====================")
        print(f"Площадь: {calc.pr_tr_second()}")
        print("====================")
    elif choice == "3":
        a = float(input("\nВведите первую сторону: "))
        b = float(input("Введите вторую сторону: "))
        c = float(input("Введите третью сторону: "))
        calc = Calculate(a=a, b=b, c=c)
        print("\n====================")
        print(f"Площадь: {calc.pr_tr_third()}")
        print("====================")
    elif choice == "4":
        return
    else:
        print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    menu()  # Запуск главного меню