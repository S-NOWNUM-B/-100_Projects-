"""
Дата добавления файла:

Дата - 15.02.2025

Описания задачи:

Список покупок — создание списка покупок с методами добавления, удаления, отображения элементов.
"""

class ShoppingList:
    def __init__(self):
        self.item = {}

    def add_Item(self, item, quantity=1):
        if item in self.item:
            self.item[item] += quantity
        else:
            self.item[item] = quantity

    def __getitem__(self, item):
        return self.item.get(item, 0)

    def __str__(self):
        return f"В списке ваших покупок есть: {self.item}"

sh = ShoppingList()

sh.add_Item("Баннан", 3)
sh.add_Item("Яблоко", 7)

print(sh)