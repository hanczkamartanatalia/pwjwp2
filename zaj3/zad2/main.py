from typing import List


def average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Lista nie może być pusta.")
    return sum(numbers) / len(numbers)
try:
    result = average([1.5, 2.5, 3.5, 4.0])
    print(f"Średnia: {result}")
except ValueError as e:
    print(e)
