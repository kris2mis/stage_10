# Найти все элементы той части последовательности простых чисел, значение
# последнего элемента которой не превосходит введённого пользователем значения.

def find_sequence(n):
    a = []  # список от 0 до n
    for i in range(n + 1):
        a.append(i)

    a[1] = 0  # Вторым элементом является единица,которую не считают простым числом, поэтому она = 0

    i = 2  # начинаем с 3-го элемента
    while i <= n:  # Если значение ячейки до этого не было обнулено, в этой ячейке содержится простое число.
        if a[i] != 0:
            j = i + i  # первое кратное ему будет в два раза больше
            while j <= n:
                a[j] = 0  # это число составное, поэтому заменяем его нулем
                j = j + i  # переходим к следующему числу, которое кратно i (оно на i больше)
        i += 1

    a = a[:-1] #удалить последний элемент из списка
    # Превращая список во множество, избавляемся от всех нулей кроме одного.
    a = set(a)
    a.remove(0)  # удаляем
    print(a)


def main():
    n = int(input("Input your number: "))

    sequence = find_sequence(n)

    msg = f"The sequence of prime numbers: {sequence}"


main()