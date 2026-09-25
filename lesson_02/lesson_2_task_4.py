def fizz_buzz(n):
    """
    Печатает числа от 1 до n, заменяя числа, кратные 3, словом "Fizz",
    числа, кратные 5, словом "Buzz", а числа, кратные как 3, так и 5, словом "FizzBuzz".
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


n_input = int(input("Введите число: "))
fizz_buzz(n_input)
