# # Квартал


# def quarter_of_year(month):
#     if month < 1 or month > 12:
#         return "Некорректное значение!"
#     if 1 <= month <= 3:
#         return "1 квартал"
#     elif month <= 6:
#         return "2 квартал"
#     elif month <= 9:
#         return "3 квартал"
#     else:
#         return "4 квартал"


# assert quarter_of_year(1) == "1 квартал", "Ошибка: Январь должен быть в 1 квартале!"
# assert quarter_of_year(3) == "1 квартал", "Ошибка: Март должен быть в 1 квартале!"
# assert quarter_of_year(4) == "2 квартал", "Ошибка: Апрель должен быть во 2 квартале!"
# assert quarter_of_year(12) == "4 квартал", "Ошибка: Декабрь должен быть в 4 квартале!"
# assert (
#     quarter_of_year(0) == "Некорректное значение!"
# ), "Ошибка: 0 - некорректное значение!"
# assert (
#     quarter_of_year(13) == "Некорректное значение!"
# ), "Ошибка: 13 - некорректное значение!"

# print("Все тесты прошли успешно!")
# month = int(input("Введите месяц: "))
# print(quarter_of_year(month))

# # def quarter_of_year(month):
# #     if 1 <= month <= 3:
# #         return "I квартал"
# #     if 4 <= month <= 6:
# #         return "II квартал"
# #     if 7 <= month <= 9:
# #         return "III квартал"
# #     if 10 <= month <= 12:
# #         return "IV квартал"
# #     return "Неверный номер месяца"

# # month = int(input("Введите номер месяца (1-12): "))
# # print(quarter_of_year(month))
