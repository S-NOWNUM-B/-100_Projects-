"""
Дата добавления файла:

Дата - 15.02.2025

Описания задачи:

Треугольник — класс для работы с треугольниками, метод для вычисления площади.
"""

from math import sqrt


class Triangle:
    def __init__(self, a=None, b=None, c=None, h=None):
        self.a = a
        self.b = b
        self.c = c
        self.h = h


class Calculate(Triangle):
    def __init__(self, a=None, b=None, c=None, h=None):
        super().__init__(a, b, c, h)

    def rav_star_first(self):
        return (sqrt(3) / 4) * self.a ** 2

    def rav_tr_first(self):
        return (1 / 2) * (self.a * self.h)

    def rav_tr_second(self):
        return ((self.a ** 2) * sqrt(3)) / 4

    def pr_tr_first(self):
        return (1 / 2) * (self.a * self.h)

    def pr_tr_second(self):
        return (1 / 2) * (self.a * self.b)

    def pr_tr_third(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


def menu():
    while True:
        print("\n===== ГЛАВНОЕ МЕНЮ =====")
        print("1) Рассчитать площадь равностороннего треугольника")
        print("2) Рассчитать площадь равнобедренного треугольника")
        print("3) Рассчитать площадь прямоугольного треугольника")
        print("4) Выйти из программы")

        choice = input("Введите номер команды: ")

        if choice == "1":
            submenu_equilateral()

        elif choice == "2":
            submenu_isosceles()

        elif choice == "3":
            submenu_right()

        elif choice == "4":
            print("\nВыход из программы...")
            break
        else:
            print("\nНекорректный ввод, попробуйте снова.")


def submenu_equilateral():
    print("\n===== РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК =====")
    print("1) Площадь через длину стороны")
    print("2) Назад")

    choice = input("Выберите способ расчёта: ")

    if choice == "1":
        a = float(input("\nВведите сторону треугольника: "))
        calc = Calculate(a=a)
        print("\n====================")
        print(f"Площадь: {calc.rav_star_first()}")
        print("====================")

    elif choice == "2":
        return
    else:
        print("Некорректный ввод, попробуйте снова.")


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
    menu()