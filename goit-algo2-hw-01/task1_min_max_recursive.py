def find_min_max(arr):
    # Базовий випадок: якщо масив має один елемент
    if len(arr) == 1:
        return (arr[0], arr[0])

    # Базовий випадок: якщо два елементи
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Рекурсивний випадок: розділяємо масив навпіл
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднуємо результати
    return (min(left_min, right_min), max(left_max, right_max))


if __name__ == "__main__":
    # Тестовий масив
    numbers = [3, 1, 9, -4, 7, 0, 5]
    min_val, max_val = find_min_max(numbers)
    print("Мінімум:", min_val)
    print("Максимум:", max_val)
