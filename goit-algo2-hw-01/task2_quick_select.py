import random


def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах від 1 до довжини масиву")

    pivot = random.choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k <= len(lows):
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quick_select(highs, k - len(lows) - len(pivots))


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    result = quick_select(arr, k)
    print(f"{k}-й найменший елемент:", result)
