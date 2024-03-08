from utils import parse_arguments, print_result, print_title
import timeit


def find_min_coins(coins: list[int], change: int):
    if change == 0 or min(coins) > change:
        return {}
    min_coins = [0] + [float("inf")] * change
    min_coins[0] = 0
    last_used = [-1] * (change + 1)

    for coin in coins:
        for i in range(coin, change + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_used[i] = coin

    total = {}
    current = change
    while current > 0:
        coin = last_used[current]
        total[coin] = total.get(coin, 0) + 1
        current -= coin

    return total


if __name__ == "__main__":
    coins, change = parse_arguments()
    start_time = timeit.default_timer()
    result = find_min_coins(coins, change)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    print_title('Функція "find_min_coins"')
    print_result(coins, change, result)
    print(f"Час виконання: {execution_time:.9f} секунд")
