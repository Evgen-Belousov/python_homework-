"""
Модуль для определения сезона по номеру месяца.
"""


def month_to_season(month_number):
    """
    Возвращает сезон по номеру месяца.
    """
    i = month_number
    if i < 1 or i > 12:
        return "Такого месяца пока не придумали: "
    if i in [12, 2, 1]:
        return "Зима"
    if i <= 5:
        return "Весна"
    if i <= 8:
        return "Лето"
    return "Осень"


month_number_input = int(input("Enter the month: "))
print(month_to_season(month_number_input))
