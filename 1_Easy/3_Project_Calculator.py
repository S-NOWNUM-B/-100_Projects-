"""
Дата добавления файла:

Дата - 15.02.2025

Описания задачи:

Калькулятор — простая программа для выполнения базовых операций (сложение, вычитание, умножение, деление).
"""

class Znac:
    def __init__(self, num1=None, num2=None):
        self.num1 = num1
        self.num2 = num2

class Calculator(Znac):
    def __init__(self, num1=None, num2=None):
        super().__init__(num1, num2)

    def action_first(self):
        return self.num1 + self.num2

    def action_second(self):
        return self.num1 - self.num2

    def action_third(self):
        return self.num1 * self.num2

    def action_fourth(self):
        if self.num2 == 0:
            raise ZeroDivisionError("\nОШИБКА: Деление на 0 невозможно")
        return self.num1 / self.num2

def main_menu():
    while True:
        print("\n===== ГЛАВНОЕ МЕНЮ =====")
        print("1) Сложение")
        print("2) Вычитание")
        print("3) Умножение")
        print("4) Деление")
        print("5) Выйти из программы")

        choice = input("Введите номер команды: ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("\nВведите первое число: "))
                num2 = float(input("Введите второе число: "))
                c = Calculator(num1, num2)

                if choice == "1":
                    result = c.action_first()
                elif choice == "2":
                    result = c.action_second()
                elif choice == "3":
                    result = c.action_third()
                elif choice == "4":
                    result = c.action_fourth()

                print("\n====================")
                print(f"Ответ: {result}")
                print("====================")

            except ValueError:
                print("Ошибка: Введите корректные числа!")
            except ZeroDivisionError as e:
                print(e)  # Вывод ошибки при делении на 0

        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Ошибка: Введите число от 1 до 5!")

if __name__ == "__main__":
    main_menu()