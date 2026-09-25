# Площадь квадрата


"""
Модуль для вычисления площади квадрата.
"""

import math


def square(side_length):
    """
    Вычисляет площадь квадрата по заданной длине стороны.
    """
    area = side_length**2
    if not side_length.is_integer():
        area = math.ceil(area)
    print(f"Площадь квадрата при стороне {side_length} равна: {area}")


side_length_input = float(input("Введите сторону квадрата: "))

square(side_length_input)
