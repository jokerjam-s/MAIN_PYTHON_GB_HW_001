# Задача 1
#
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

# Длины сторон треугольника полагаем целочисленными значениями.
# Считаем что пользователь "не дурак", проверку правильности ввода не производим

# Кол-во сторон в треугольнике
TRANGLE_SIDES_COUNT = 3

# ключи для структуры информации о треугольнике
KEY_TRANGLE = "trangle"
KEY_ISOSCELES = "isosceles"
KEY_EQUILATE = "equilate"


def main():
    # стороны треугольника
    trangle_sides = {}
    message = "Это не треугольник"

    print("Введите длины сторон треугольника")
    trangle_sides['a'] = get_int("Сторона А: ")
    trangle_sides['b'] = get_int("Сторона B: ")
    trangle_sides['c'] = get_int("Сторона C: ")

    trangle_info = check_trangle(trangle_sides)

    if trangle_info.get(KEY_TRANGLE, False):
        message = "Это треугольник"
        # т.к. равносторонний треугольник есть разновидность равнобедренного -
        # достаточно вывести одну из характеристик "по старшинству"
        if trangle_info.get(KEY_EQUILATE, False):
            message += ", равносторонний"
        elif trangle_info.get(KEY_ISOSCELES, False):
            message += ", равнобедренный"
        else:
            message += ", разносторонний"

    print(message)


# Проверка фигуры.
# **sides - словарь сторон фигуры (key:value) => (имя:размер)
# возвращает словарь проверки фигуры на соответствие треугольнику
#    key    :  value
# KEY_TRANGLE : это треугольник или нет
# KEY_ISOSCELES : равнобедренный
# KEY_EQUILATE : равносторонний

def check_trangle(sides: dict) -> {}:
    result = {KEY_TRANGLE: False, KEY_ISOSCELES: False, KEY_EQUILATE: False}

    # если кол-во сторон не соответствует требуемому для треугольника - это не треугольник
    if len(sides) == TRANGLE_SIDES_COUNT:
        # для треугольника сумма 2х сторон всегда больше 3й
        # получим длину максимальной
        max_side = max(sides.values())

        # получим длины остальных сторон
        other_sides = [i for i in sides.values() if i < max_side]

        # кол-во прочих сторон за минусом максимальной составит TRANGLE_SIDES_COUNT-1, но
        # если две или все стороны треугольника одинаковы - размер множества прочих сторон может быть меньше (1 или 0)
        # тогда для недостающей стороны берем значение найденной максимальной
        sum_other_side = (TRANGLE_SIDES_COUNT - len(other_sides) - 1) * max_side + sum(other_sides)

        # проверяем соответствие длин
        if sum_other_side > max_side:
            result[KEY_TRANGLE] = True

        if result.get(KEY_TRANGLE):
            # две стороны одинаковы - равнобедренный
            result[KEY_ISOSCELES] = (len(other_sides) < 2 or other_sides[0] == other_sides[1])
            # все стороны равны - равносторонний
            result[KEY_EQUILATE] = (len(other_sides) == 0)

    return result

# Запрос численной величины
def get_int(message=None) -> int:
    if message is None:
        message = "Введите целое число: "

    return int(input(message))


# Старт
if __name__ == "__main__":
    main()
