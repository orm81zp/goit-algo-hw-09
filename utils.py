import sys
from timeit import timeit


class CustomException(Exception):
    pass


def parse_arguments():
    """Парсить аргументи командного рядка"""

    coins = [50, 25, 10, 5, 2, 1]
    change = 11

    if len(sys.argv) > 1:
        try:
            change = int(sys.argv[1])
        except CustomException:
            print("Другим аргументом має бути число сума решти, наприклад: 113")

        if len(sys.argv) > 2:
            try:

                coins = [int(x) for x in sys.argv[2].split(",")]
            except CustomException:
                print(
                    "Першим аргументом мають бути цифри, розділені комою, наприклад: 50,25,10,5,2,1"
                )

    return coins, change


def print_result(coins, change, set_of_coins):
    print(f"Маємо набір монет {coins}")
    print(f"Сума решти {change}")

    count_of = len(set_of_coins.items()) - 1
    print("Набір монет для решти: ", end="")
    for index, set_of_coin in enumerate(set_of_coins.items()):
        coin, count = set_of_coin

        print(
            f"{coin}x{count}",
            end=f"{', ' if index < count_of else ''}",
        )

    print()


def print_title(title):
    print(title)
    print("-" * len(title))


def print_time_consume(func, number=100000):
    time_consume = timeit(lambda: func(), number=number)
    print(f"Затрачено часу на виконання: {time_consume:.6f}")
