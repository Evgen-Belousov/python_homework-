def is_year_leap(y):
    """Определяет, является ли год високосным."""
    return y % 4 == 0


year = int(input("Выберите любой год: "))
result = is_year_leap(year)
print(f"Год {year}: {result}")
