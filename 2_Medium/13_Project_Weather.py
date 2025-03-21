"""
Дата добавления файла:

Дата - 17.02.2025

Описание задачи:

Погода — создание класса для отображения погоды в городе с методами для обновления и вывода.
"""

import random

class Weather:
    def __init__(self, city, temperatura):
        self.city = city
        self.temperatura = temperatura

    def getWeather(self):
        return f"На улице {self.temperatura}°C"

    def __str__(self):
        return f"В городе {self.city} сейчас {self.temperatura}°C"

t = Weather("Алматы", round(random.uniform(-30, 50), 1))

print(t.getWeather())
print(t)