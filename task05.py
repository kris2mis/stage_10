# Найти все простые делители заданного натурального числа.

# ЗАДАНИЕ СЛОЖНО СДЕЛАТЬ , ПРИШЛОСЬ ВОСПОЛЬЗОВАТЬСЯ ПОМОЩЬЮ
def find_divisors(n):
    a = []
    i = 2
    while i * i < n + 1:
        if n % i == 0:
            a.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n != 1:
        a.append(n)
    print(a)


def main():
    n = int(input("Input your number: "))

    find_divisors(n)
    # msg = f"Prime divisors of {n}: {divisors}"


main()


#ОБЪЯСНЕНИЕ
#
# def delit(n):
#     res = []
#     i = 2
#     # цикл до квадратного корня из "n"
#     # больше этого без остатка не делится, если только ...
#     # (об этом ниже)
#     while i * i < n + 1:
#         # если при делении остаток = 0, то добавляем "i" в список
#         if n % i == 0:
#             res.append(i)
#             # теперь делим исходное число на "i", пока не появится остаток
#             while n % i == 0:
#                 n //= i
#         # берем следующее "i"
#         i += 1
#     # если в конце "n" не равно единице, то значит остался один(!)
#     # делитель, больший кв. корня из исходного "n"
#     # добавляем в список
#     if n != 1:
#         res.append(n)
#     return res