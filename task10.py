# Натуральное число называют совершенным, если оно равно сумме всех своих
# делителей, не считая только его самого (например, 28=1+2+3+7+14 – совер-
# шенное число). Напишите программу, которая проверяет, является ли введён-
# ное натуральное число совершенным. Для проверки работоспособности про-
# граммы приводится список некоторых совершенных чисел: 6, 28, 496, 8128.

# ТОЖЕ СЛОЖНОЕ ЗАДАНИЕ, БЕЗ ПОМОЩИ НЕ ОБОШЛОСЬ

def check_perfect_number(n):
    # выводим делители числа и 1 (само число не нужно)
    a = {1}
    i = 2
    s = 1
    while i * i <= n:
        if n % i == 0:
            s = s + i + (n // i if i != n // i else 0)
            a.update({i, n // i})
        i += 1

    print(a)

    return s


def main():
    n = int(input("Input your number: "))

    s = check_perfect_number(n)
    if s == n:
        result = True
    else:
        result = False

    msg = f"Is {n} a perfect number?\nIt's {result}."
    print(msg)


main()



#ОБЪЯСНЕНИЕ
#
#
# numb = int(input("Введите целое число: "))
#
# # множество делителей заданного числа
# delitellist = {1}
#
# # первый делитель любого натурального числа
# sumlist = 1
#
# i = 2  # следующий возможный делитель заданного числа
#
# # вычислять, пока квадрат делителя не больше заданного числа
# # накопительная сумма делителей не больше заданного числа
# while i * i <= numb and sumlist <= numb:
#
#     # если заданное число делится без остатка на "делитель"
#     if (numb % i == 0):
#         # то к накопительной сумме делителей добавим
#         # "делитель" и частное от "число"//"делитель",
#         # если они не равны
#         # ("делитель" - 6; "число" - 36 -> 6 == 36//6 -> один делитель 6
#         # "делитель" - 6; "число" - 42 -> 6 != 42//6 -> два делителя 6, 7
#         sumlist += i + (numb // i if i != numb // i else 0)
#
#         # в множество делителей добавляем "делитель" и "частное"
#         # Если они одинаковы, то в множество "попадет" одно значение
#         delitellist.update({i, numb // i})
#
#     # увеличиваем "делитель" на 1
#     i += 1
#
# # если заданное число == сумме делителей
# if sumlist == numb:
#     print(*sorted(delitellist))
# else:
#     print(0)
