# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
import random

# Диапазон загадываемых чисел
MIN_VALUE = 0
MAX_VALUE = 1000

# кол-во допустимых угадываний
TRYING_COUNT = 10


def main():
    # загадываем число
    number = random.randint(MIN_VALUE, MAX_VALUE)
    # номер текущей попытки
    trying_now = 0

    while trying_now < TRYING_COUNT:
        user_number = get_int(f"Введите число от {MIN_VALUE} до {MAX_VALUE} включительно: ")

        if user_number not in range(MIN_VALUE, MAX_VALUE+1):
            print("Неверное число")
            continue
        if user_number == number:
            print("Вы угадали")
            break
        elif user_number < number:
            print("Мое число больше")
        else:
            print("Мое число меньше")
        trying_now += 1
    else:
        print("Попытки закончились")


# Запрос численной величины
def get_int(message=None) -> int:
    if message is None:
        message = "Введите целое число: "

    return int(input(message))


# Старт
if __name__ == "__main__":
    main()
