# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Считаем что пользователь "не дурак", проверку правильности ввода не производим

# Допустимый диапазон чисел для проверки
MIN_NUMBER = 0
MAX_NUMBER = 100000

def main():
    ask_digit = True
    result = "Число не является простым"

    while ask_digit:
        number = get_int()

        if number not in range(MIN_NUMBER, MAX_NUMBER + 1):
            print(f"Число должно быть не меньше {MIN_NUMBER} и не больше {MAX_NUMBER}")
            continue

        if isPrime(number):
            result = "Это простое число"

        ask_digit = False

    print(result)


# Проверка простоты числа
def isPrime(number):
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    return divider * divider > number


# Запрос численной величины
def get_int(message=None) -> int:
    if message is None:
        message = "Введите целое число: "

    return int(input(message))


# Старт
if __name__ == "__main__":
    main()
