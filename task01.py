# Написать программу «Heads or Tails?» (орёл или решка?), которая бы «подбра-
# сывала» условно монету, к примеру, 1000 раз и сообщала, сколько раз выпал
# орёл, а сколько – решка.

from random import randint

TRIES = 1000  # кол-во попыток


def count_sides():
    heads = 0  # сколько раз выпал "орел"
    for _ in range(TRIES):
        # 0 - решка, 1 - орел
        if randint(0, 1):
            heads += 1
    return heads


def main():
    heads = count_sides()
    tails = TRIES - heads  # сколько раз выпала "решка"
    print("Орёл: ", heads)
    print("Решка: ", tails)


main()