# Найти все элементы последовательности чисел Фибоначчи до указанного
# пользователем порядкового номера

#         index :     0 1 2 3 4 5  6  7  8  9  10
# Fibonacci numbers:  0 1 1 2 3 5  8  13 21 34 55

def fibonacci(index):
    a =[0,1]
    first = 0
    second = 1

    if index < 2:
        return index

    for i in range(2, index + 1):
        third = first + second
        first = second
        second = third
        a.append(third)

    return a


def main():
    index = int(input("Input index: "))
    element = fibonacci(index)

    msg = f"Fibonacci sequence until [{index}] --> {element}."

    print(msg)


main()