from utils import parse_arguments, print_result, print_title
import timeit


def find_coins_greedy(coins: list[int], change: int):
    if change == 0 or min(coins) > change:
        return {}

    count_coins = {}
    for coin in coins:
        count = change // coin
        if count > 0:
            count_coins[coin] = count
        change = change - coin * count
    return count_coins


if __name__ == "__main__":
    coins, change = parse_arguments()
    start_time = timeit.default_timer()
    result = find_coins_greedy(coins, change)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    print_title('Функція "find_coins_greedy"')
    print_result(coins, change, result)
    print(f"Час виконання: {execution_time:.9f} секунд")
