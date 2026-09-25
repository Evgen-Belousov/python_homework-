# # Два делителя
# n = int(input("tab num: "))


# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if (i % 4 == 0) :
#             print(f"{i} Делится и на 2, и на 4")
#         elif (i % 2 == 0):
#             print(f"{i} Делится на 2, но не на 4")
#         else:
#             print(i)


# check_divisibility(n)

# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print(f"{i} Делится и на 2, и на 4")
#             continue  # Переходим к следующему числу
#         if i % 2 == 0:
#             print(f"{i} Делится на 2, но не на 4")
#             continue  # Переходим к следующему числу
#         print(i)  # Если ни одно условие не сработало — просто печатаем число
