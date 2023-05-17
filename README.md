# Основы Python. ДЗ #1

<!-- TOC -->
* [Задача 1](#задача-1)
* [Задача 2](#задача-2)
* [Задача 3](#задача-3)
<!-- TOC -->

## Задача 1

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

**примеры выполнения**

![img.png](img/img_1-01.png)

![img.png](img/img_1-02.png)

![img.png](img/img_1-03.png)

![img.png](img/img_1-04.png)

## Задача 2

Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

**примеры выполнения**

![img.png](img/img_2-01.png)

![img.png](img/img_2-02.png)

![img.png](img/img_2-03.png)

## Задача 3

Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

**примеры выполнения**

![img.png](img/img_3-01.png)

![img.png](img/img_3-02.png)

![img.png](img/img_3-03.png)