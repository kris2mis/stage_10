# Проверить, является ли заданное натуральное число простым (prime number).
# Для справки: простые числа – эта натуральные (целые положительные) числа,
# которые имеют ровно два различных натуральных делителя – единицу и са-
# мого себя (ресурс: https://en.wikipedia.org/wiki/Prime_number). К примеру,
# числа 2, 3, 5, 7, 11, 13, 17, 19 и т.д. являются простыми.

# Другими словами, натуральное число p является простым, если оно отлично от 1
# и делится без остатка только на 1 и на само p

def prime_number(number):
    if number > 1:
        if number % 2 != 0 and number // number == 1:
            result = True
        else:
            result = False
    else:
        return -1
    return result


def main():
    number = int(input("Input your number: "))
    result = prime_number(number)
    msg = f"Is this a prime number?\n{result}"
    print(msg)


main()
