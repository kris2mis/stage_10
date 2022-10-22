# Найти НОД и НОК двух натуральных чисел.


# # НОД
#
# def find_nod(a, b):
#     while a > 0 and b > 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
#
#
# def main():
#     a = int(input("Input a: "))
#     b = int(input("Input b: "))
#
#     result = find_nod(a, b)
#
#     msg = f"The least common divisor (nod) - {result}."
#
#     print(msg)
#
#
# main()


# НОК


def find_nok(a, b):
    m = max(a, b)
    while a > 0 and b > 0:
        if m % a == 0 and m % b == 0:
            return m
            # break
        else:
            m += 1


def main():
    a = int(input("Input a: "))
    b = int(input("Input b: "))

    result = find_nok(a, b)

    msg = f"The least common multiple (nok) - {result}."

    print(msg)


main()
