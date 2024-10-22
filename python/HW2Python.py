HW2Python
##1.Создайте программу, которая проверяет, является ли введенное пользователем число четным или нечетным, и выводит соответствующее сообщение.
def check_even_odd():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print(f"{number} - четное число.")
    else:
        print(f"{number} - нечетное число.")

check_even_odd()

##2.Реализуйте программу, которая определяет, является ли введенная пользователем строка палиндромом (читается одинаково слева направо и справа налево). Выведите соответствующее сообщение. s
def check_palindrome():
    string = input("Введите строку: ")
    if string == string[::-1]:
        print(f"{string} - палиндром.")
    else:
        print(f"{string} - не палиндром.")

check_palindrome()

##3.Реализуйте программу, которая определяет, является ли заданное число простым (имеет только два делителя: 1 и само число). Выведите соответствующее сообщение.
def check_prime():
    number = int(input("Введите число: "))
    if number <= 1:
        print(f"{number} - не простое число.")
        return
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} - не простое число.")
            return
    print(f"{number} - простое число.")

check_prime()

##4.Реализуйте программу, которая определяет, является ли заданная дата корректной (). Выведите соответствующее сообщение. Дата дана в формате “20.01.2002”
def check_date():
    date_str = input("Введите дату (дд.мм.гггг): ")
    day, month, year = map(int, date_str.split('.'))
    try:
        from datetime import datetime
        datetime(year, month, day)
        print("Дата корректная.")
    except ValueError:
        print("Дата некорректная.")

check_date()

##5.Напишите программу для нахождения всех совершенных чисел (чисел, равных сумме своих делителей, исключая само число) в заданном диапазоне. Диапазон от 0 до 1000
def perfect_numbers():
    perfects = []
    for num in range(1, 1001):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        if divisors_sum == num:
            perfects.append(num)
    print("Совершенные числа в диапазоне от 0 до 1000:", perfects)

perfect_numbers()

##6.Реализуйте программу для проверки, является ли заданное число числом Фибоначчи (число, которое является членом последовательности Фибоначчи). Заданное число 25
def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

number = 25
if is_fibonacci(number):
    print(f"{number} - число Фибоначчи.")
else:
    print(f"{number} - не число Фибоначчи.")

##7.Напишите программу, которая определяет, является ли заданное число совершенным числом (число, равное сумме своих делителей, исключая само число). Выведите сообщение с результатом.
def check_perfect_number():
    number = int(input("Введите число: "))
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    if divisors_sum == number:
        print(f"{number} - совершенное число.")
    else:
        print(f"{number} - не совершенное число.")

check_perfect_number()

##8.Создайте программу, которая определяет, в какой сезон года попадает заданная дата (месяц и день).
def season_of_date():
    date_str = input("Введите дату (дд.мм): ")
    day, month = map(int, date_str.split('.'))
    
    if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day < 21):
        print("Зима")
    elif (month == 3 and day >= 21) or (month <= 5) or (month == 6 and day < 21):
        print("Весна")
    elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day < 21):
        print("Лето")
    elif (month == 9 and day >= 21) or (month <= 11) or (month == 12 and day < 21):
        print("Осень")

season_of_date()
